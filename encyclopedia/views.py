import markdown2
import secrets
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from .forms import entryForm
from . import util
from markdown2 import Markdown

def search(request):
    if request.method == 'GET':
        query = request.GET.get("q", "")
        if util.get_entry(query) == None:
          
            list = util.list_entries()

         
            list_len = len(list)
            results = []

            for i in range(list_len):
                if query.lower() in list[i].lower():
                    results.append(list[i])
                    i += 1
                else:
                    i += 1
            print(results)
            if len(results) == 0:
                return render(request, "encyclopedia/nonExistingEntry.html", {
                    "entryTitle": query,
                    
                })
            else:
                return render(request, "encyclopedia/index.html", {
                        "entries": results
                    })
        else:
            return HttpResponseRedirect(reverse("entry", kwargs={'entry': query}))
    else:
        return render(request, "encyclopedia/nonExistingEntry.html")


def entry(request, entry):
    markdowner = Markdown()
    
    if util.get_entry(entry) is None:
        return render(request, "encyclopedia/nonExistingEntry.html", {
            "entryTitle": entry    
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(util.get_entry(entry)),
            "entryTitle": entry
        })



def edit(request, entry):
    entryPage = util.get_entry(entry)
    if entryPage is None:
        return render(request, "encyclopedia/nonExistingEntry.html", {
            "entryTitle": entry    
        })
    else:
        form = entryForm()
        form.fields["title"].initial = entry     
        form.fields["title"].widget = forms.HiddenInput()
        form.fields["content"].initial = entryPage
        form.fields["edit"].initial = True
        return render(request, "encyclopedia/newEntry.html", {
            "form": form,
            "edit": form.fields["edit"].initial,
            "entryTitle": form.fields["title"].initial
        })        

def random(request):
    entries = util.list_entries()
    randomEntry = secrets.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={'entry': randomEntry}))



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def newEntry(request):
    if request.method == "POST":
        form = entryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if(util.get_entry(title) is None or form.cleaned_data["edit"] is True):
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse("entry", kwargs={'entry': title}))
            else:
                return render(request, "encyclopedia/newEntry.html", {
                "form": form,
                "existing": True,
                "entry": title
                })
        else:
            return render(request, "encyclopedia/newEntry.html", {
            "form": form,
            "existing": False
            })
    else:
        return render(request,"encyclopedia/newEntry.html", {
            "form": entryForm(),
            "existing": False
        })    