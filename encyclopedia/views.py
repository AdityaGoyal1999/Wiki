from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect

from . import util
from markdown2 import Markdown
import random
# print(util.list_entries(), "\n\n\n")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def singlePage(request, title):

    response = util.get_entry(title)
    if response is None:
        return render(request, "encyclopedia/error.html")
    else:
        markdowner = Markdown()
        return render(request, 'encyclopedia/singlePage.html',{"contents": markdowner.convert(response), "title": title})

def search(request):

    entry = request.GET['q']
    response = util.get_entry(entry)
    if response is not None:
        return HttpResponseRedirect(reverse('ency:singlePage', args=(entry,)))
    results = []
    queries = util.list_entries()
    print(queries, "\n\n\n")
    for query in queries:
        if entry.lower() in query.lower():
            results.append(query)
    return render(request, 'encyclopedia/searchResults.html', {"entry": entry, "results": results})

def createPage(request):
    return render(request, 'encyclopedia/createPage.html', {'error': None})

def savePage(request):
    
    title = request.POST['title']
    contents = request.POST['content']
    queries = util.list_entries()
    if title in queries:
        return render(request, 'encyclopedia/createPage.html', {'error': 'The title already exists.'})
    else:
        util.save_entry(title, contents)
        return HttpResponseRedirect(reverse('ency:singlePage', args=(title,)))

def editPage(request, title):

    response = util.get_entry(title)
    return render(request, 'encyclopedia/editPage.html', {"title": title, "contents": response})


# Edit this
def editPageSave(request):

    
    contents = request.POST['content']
    title = request.POST['title']
    queries = util.list_entries()
    util.save_entry(title, contents)
    return HttpResponseRedirect(reverse('ency:singlePage', args=(title,)))

def randomPage(request):

    queries = util.list_entries()
    title = random.choice(queries)

    return HttpResponseRedirect(reverse('ency:singlePage', args=(title,)))