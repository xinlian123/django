from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "home.html")

def readme(request):
    return render(request, "readme.html")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddic = {}

    for word in wordlist:
        if word in worddic:
            worddic[word]  += 1
        else:
            worddic[word] = 1
    countWord = len(fulltext.split())
    return render(request, "count.html", {'count':countWord, 'fulltext':fulltext, 'worddic':worddic.items()})
