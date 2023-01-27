from django.shortcuts import render
import markdown
from . import util

def convert_md(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    converted_html = convert_md(title)
    if converted_html == None:
        return render(request, "encyclopedia/error.html", {"message": "Sorry, this entry does not exist."})
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": converted_html
        })

def search(request):
    if request.method == "POST":
        search_entry = request.POST['q']
        converted_html = convert_md(search_entry)
        if converted_html is not None:
             return render(request, "encyclopedia/entry.html",{
            "title": search_entry,
            "content": converted_html
            })
        else:
            all_entries = util.list_entries()
            suggested_entries = []
            for entry in all_entries:
                if search_entry.lower() in entry.lower():
                    suggested_entries.append(entry)
            return render(request, "encyclopedia/search.html", {
                "suggested_entries" : suggested_entries
            })
        
            
def create_new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")