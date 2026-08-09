from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed

from .forms import PersonForm

# Create your views here.
# like creating routes here

def hello_world_view(request):
    return HttpResponse('Hello World')
# this takes http request and send http response
# defining a view is not enough
# we need to add the path to which this view belongs to in core/urls.py
# so we create urls.py in this dir and do mapping with urls.py in core

def hello_python_view(request):
    return HttpResponse('Hello Python')
# keep this as default endpoint -> /

# we dont actually just return http responses, we usually render html documents

def hello_html_view(request):
    # return render('todos/hello.html') - this gives error bcz we also need to pass request when we are using render
    return render(request, 'todos/hello.html')

# we now pass a parameter in view
def hello_path(request, name):
    return HttpResponse(f'Hello {name}!')
# but how do we get the name from url
# for that we add in path

# query parameter
# no parameter in function
def hello_query(request):
    # mysite.com/serach?whatever=gnfhbhjbfwsdnajkn&q=bhjbgjhbgsjhgn&name=fsfn
    return HttpResponse(f'Your query was {request.GET.get("q")}')
# GET is the method we use and also the dictionary containing our query parameter
# we can retrieve info we pass after ? using get function and name like q=, whatever=, name=
# so we are retrieving these from the request

# to redirect
def special_view(request):
    # do some stuff 
    # then we can jst redirect hem to already existing endpoint 
    return redirect('hello_html')

# FOR POST REQUESTS
# sending data to server means not as parameter or query parameter but as request object
def post_example(request):
    # if this view only wants to post requests and deny get requests then we add ttis in if condition
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        job = request.POST.get('job')
        # so with these now we can look up for the person in a db using this info or do some stuff with them
        # but for now we just send http response that tells ok you sent this info
        return HttpResponse(f'You posted: {name}, {age}, {job}')
    else:
        # we can raise an exception here but for now we pass
        # pass
        return HttpResponseNotAllowed(['POST'])


# to submit post req
def submit_example(request):
    return render(request, 'todos/submit.html')

# using forms in convinient way
def post_django_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        # validation check
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            job = form.cleaned_data['job']
            return HttpResponse(f'You posted: {name}, {age}, {job}')
        else:
            return HttpResponseNotAllowed(['POST'])


# we are going to pass empty form object as context to rendering
def submit_django_form(request):
    form = PersonForm
    return render(request, 'todos/submit_django_form.html', {'form': form})
# we are passing a from dict here

# to pass smtg to the html doc we are rendering
def template_view(request):
    context = {
        "name": "Navya",
        "age" : 18,
        "skills": ["Python", "Docker", "Django"]
    }
    return render(request, 'todos/template_demo.html', context)