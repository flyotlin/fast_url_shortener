from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.cache import cache
from . import url_shortener
from .models import Urls

def index(request):
    """
    GET Request. Render the index html page.
    """
    return render(request, "url_handler/index.html", {
        "visible": False, 
        "long_url": ""
    })

def create(request):
    """
    POST Request. Create short url according to long url from request body.
    """
    long_url = request.POST["long_url"]
    short_url = url_shortener.hash(long_url)

    # (short_url, long_url) not in local redis do the following
    if cache.get(short_url) != long_url:
        # if (short_url, long_url) not in centralized MySQL, write to MySQL
        mySqlResult = Urls.objects.all().filter(short_url=short_url)
        if mySqlResult.count() == 0:
            Urls.objects.create(short_url=short_url, long_url=long_url)
        # write to redis
        cache.set(short_url, long_url, nx=True, timeout=None)   # never expires

    return render(request, "url_handler/index.html", {
        "visible": True, 
        "short_url": short_url,
        "long_url": long_url,
    })

def redirect_url(request, shortUrl):
    """
    GET Request. Redirect the specific short url 
    param to the corresponding long url.
    """

    # if (short_url, long_url) in redis, redirect by redis data
    longUrl = cache.get(shortUrl)
    if longUrl != None:
        response = redirect(longUrl)
        response.headers['Via'] = 'redis'
        return response

    # if (short_url, long_url) in MySQL, update redis, and redirect by MySQL data
    mySqlResult = Urls.objects.all().filter(short_url=shortUrl)
    if mySqlResult.count() != 0:
        longUrl = mySqlResult[0].long_url
        cache.set(shortUrl, longUrl, nx=True, timeout=None)
        response = redirect(longUrl)
        response.headers['Via'] = 'mysql'
        return response

    # return not found
    return render(request, "url_handler/error.html")
