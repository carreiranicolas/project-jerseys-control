from django.shortcuts import render, redirect
from .forms import CamisaForm


# Create your views here.

def home(request):
    return render(request, 'inventory/home.html')



def registrar(request):
    if request.method == 'POST':
        form = CamisaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = CamisaForm()
    
    return render(request, 'inventory/registrar.html', {'form': form})