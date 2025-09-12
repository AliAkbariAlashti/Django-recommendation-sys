from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from .forms import UserInterestsForm, NewUserForm

# Create your views here.


class recommender(View):
    def get(self, request):
        return HttpResponse("hello world")
    
    
def home(request):
    form = UserInterestsForm()
    
    if request.method == 'POST':
        form = UserInterestsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        
    return render(request, 'UserInterestsForm.html', {'form' : form})


def newuser(request):
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        
    return render(request, 'NewUserForm.html', {'form' : form})

