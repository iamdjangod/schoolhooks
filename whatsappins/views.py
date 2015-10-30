from django.shortcuts import render
from forms import UserProfileForm
from django.contrib.auth.models import User


# Create your views here.

def about(request):

    return render(request,
            'registration/about.html',
            {} )


