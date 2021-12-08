from django.shortcuts import render
from .models import Skill,Projects
# Create your views here.
def Homepage(request):
    skill=Skill.objects.all()
    project= Projects.objects.all()
    context={
        'skill': skill,
        'project':project
    }
    return render(request,'index.html',context)