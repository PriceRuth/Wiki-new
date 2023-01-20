from django.shortcuts import render
from markdown2 import Markdown

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
        return render(request, "encyclopedia/not_found.html")
    else:
        return render(request, "encyclopedia/entry.html")
