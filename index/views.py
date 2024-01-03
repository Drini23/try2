from django.shortcuts import render
from django.http import response
import requests
from bs4 import BeautifulSoup
import re

# Create your views here.

def index(request):
    
    webpage_response = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages")
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    
    return render(request,'index/index.html', {"soup": soup.get_text()[5:15]})