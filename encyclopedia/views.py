from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect

from . import util

import random
# print(util.list_entries(), "\n\n\n")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def singlePage(request, title):

    response = util.get_entry(title)
    if response is None:
        return HttpResponse("Nothing found")
    else:
        return HttpResponse(response)

def search(request):

    entry = request.GET['q']
    response = util.get_entry(entry)
    # print(response, "\n\n")
    if response is not None:
        return HttpResponse(response)
    results = []
    queries = util.list_entries()
    print(queries, "\n\n\n")
    for query in queries:
        if entry.lower() in query.lower():
            results.append(query)
    return render(request, 'encyclopedia/searchResults.html', {"entry": entry, "results": results})

def createPage(request):
    return render(request, 'encyclopedia/createPage.html')

def savePage(request):
    
    title = request.POST['title']
    contents = request.POST['content']

    return HttpResponse(title)

def randomPage(request):

    queries = util.list_entries()
    title = random.choice(queries)

    return HttpResponseRedirect(reverse('ency:singlePage', args=(title,)))