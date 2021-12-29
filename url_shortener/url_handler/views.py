from django.shortcuts import redirect, render
from django.http import HttpResponse
import hashlib, base58

def add_url(request):
    return render(request, "url_handler/index.html", {
        "visible": False, 
        "long_url": ""
    })

def create_short_url(request):
    long_url = request.POST["long_url"]
    short_url = url_shortener(long_url)

    return render(request, "url_handler/index.html", {
        "visible": True, 
        "short_url": short_url,
        "long_url": long_url,
    })

def redirect_url(request, shortUrl):
    print("short url is:", shortUrl)
    return redirect('https://www.facebook.com/')

# Url shortener utility function.
# Use sha256 and base58 to encode long_url
def url_shortener(long_url):
    sha256 = hashlib.sha256()
    sha256.update(str.encode(long_url))
    sha256_hex_str = int(sha256.hexdigest(), 16)
    sha256_lsb_64num = int(bin(sha256_hex_str)[-64:], 2)

    short_url_byte_num = str(sha256_lsb_64num).encode()
    short_url = base58.b58encode(short_url_byte_num).decode()[:8]

    return short_url

