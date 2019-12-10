# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
#
# def home(request):
#     names = ['a', 'b', 'c', 'd']
#     d={
#         'names':names,
#         'college':'kathford'
#     }
#
#     return render(request,'home.html',d)
#
# def bootcamp(request):
#     return HttpResponse('<h1>Hello from bootcamp</h1>')

from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4

# Create your views here.

def home(request):
    page = requests.get('https://fabpedigree.com/james/mathmen.htm')
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    li=[]

    for name in soup.select('ol a'):
        li.append(name.string)
    d={
        'name':li
    }
    print(li)
    return render(request,'home.html',d)


def bootcamp(request):
    return HttpResponse('<h1>Hello from bootcamp</h1>')

