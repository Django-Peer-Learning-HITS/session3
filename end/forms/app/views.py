from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    # check if there already exists a session

    if "tasks" not in request.session:

        # If not, create a new list
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        # Access the data that the user submitted
        form = NewTaskForm(request.POST)

        # Check the validity of the form
        if form.is_valid():
            # Fetch the task from the clean version of the form
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]

            # redirect the user to listen for tasks
            return HttpResponseRedirect(reverse('app:index'))
        else:
            # If the form is invalid, re-render the page with existing information
            return render(request, 'tasks/add.html', {
                'form': form})
    return render(request, 'tasks/add.html', {
        'form': NewTaskForm()
    })


class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')
