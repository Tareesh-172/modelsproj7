from django.shortcuts import render
from .forms import RegisterForm
from .models import RegisterModel
# Create your views here.


def refView(request):
    if request.method=='GET':
        form=RegisterForm()
        return render (request, 'input.html', {'form':form})
    
    else:
        if request.method=='POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                form.save()
        return render (request, 'input.html', {'form':form})
    