from django.shortcuts import render
from .models import Editor
from .forms import EditorForm

# Create your views here.
def index(request):
    form = EditorForm()
    return render(request , 'app/index.html',{'form':form})