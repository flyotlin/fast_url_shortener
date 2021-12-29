from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import url_shortener

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
    print("short url is:", shortUrl)
    return redirect('https://www.facebook.com/')
