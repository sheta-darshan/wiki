from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.urls import reverse



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "encyclopedia/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]

            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "encyclopedia/add.html", {
                "form": form
            })

    return render(request, 'encyclopedia/add.html', {
        "form": NewTaskForm()
    })


def greet(request, name):
    return render(request, "encyclopedia/greet.html", {
        "name": name.capitalize()
    })
