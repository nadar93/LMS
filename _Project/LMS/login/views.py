from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from login.models import Role,LMSUser


def index(request):
   # here is your code
        
    return render(request, 'classmanagement/index.html', {
        'course': course,
    })




