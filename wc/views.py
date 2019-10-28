import operator

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            # Add to dictionary
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sorted_words =  sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {"fulltext": fulltext, "count": len(word_list),"sorted_words" : sorted_words})

def about(request):
    return render(request, "about.html")