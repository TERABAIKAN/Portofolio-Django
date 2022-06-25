from this import d
from django.shortcuts import redirect, render
from .models import About, Project, Contact
from .forms import FormContact

def index(request):
 about = About.objects.get(id=1)
 project = Project.objects.all()
 
 context = {
     'about': about,
     'Project': project,
     'form': FormContact()
 }
 return render(request,'index.html',context)

def send_contact(request):
    if request.POST:
        form = FormContact(request.POST)
        if form.is_valid():
          form.save()
          return redirect("/#contact")
        return redirect("/#contact")