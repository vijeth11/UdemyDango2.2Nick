from django.http import HttpResponse
from django.shortcuts import render
import operator

defaultPage = '<h1>Your Order is comming Soon</h1>'

def homePage(request):
    index = """
    <h1>Welcome to paneer home</h1>
    <br>
    <h3> Paneer dishes </h3>
    <ul>
      <li><a href='paneerchilli'>Paneer Chilli</a></li>
      <li><a href='paneer65'> Paneer 65 </a></li>
    </ul>
    """
    return render(request,'home.html',{'itemNames':['Paneer Chilli','Paneer 65'],'itemsUrl':['paneerchilli','paneer65']})

def panerrchilli(request):
    return HttpResponse(defaultPage)

def paneer65(request):
    return HttpResponse(defaultPage)

def wordcount(request):
    return render(request,'wordcount.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()
    worddictionary = {}
    for word in wordcount:
        if word in worddictionary:
            worddictionary[word]=worddictionary[word]+1
        else:
            worddictionary[word] = 1
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordcount),'worddictionary':sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)})

def about(request):
    return render(request,'about.html')