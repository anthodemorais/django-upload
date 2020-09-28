from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *

# Create your views here.
def index(request):
    docs = Document.objects.all()
    return render(request, "home.html", {'imgs' : docs})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # redirect to login after successful signup
    template_name = 'registration/signup.html'

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = Document(name=form.cleaned_data.get('name'), document=form.cleaned_data.get('document'), user=request.user)
            doc.save()
            return redirect('home')
    else:
        if request.user.is_authenticated:
            form = DocumentForm()
        else:
            return redirect('home')
    return render(request, 'upload.html', { 'form': form })