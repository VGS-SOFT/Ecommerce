"""
Definition of views.
"""
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import GetImgPath
# from django.contrib.auth.decorators import login_required
# from .models import Productdetails

def home(request):
    """ Render Custom Html Page """
    assert isinstance(request, HttpRequest)
    return render(
        request, 'index.html'
    )

# @login_required('/auth/login')
# Check the image
def imagetry(id):
    row = GetImgPath(id)
    for i in row:
         data = i
    return JsonResponse({"img":data})




    
