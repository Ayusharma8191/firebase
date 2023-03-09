from django.shortcuts import render, redirect
from django.http import HttpResponse
from firebase_authrize import db_models
from firebase_admin import auth
import json
import cv2
import requests
from django.views.decorators.clickjacking import xframe_options_sameorigin


rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={db_models.web_api_key}"

@xframe_options_sameorigin
def index(request):
    return render(request, 'login.html')


@xframe_options_sameorigin
def login(request):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    payload = json.dumps({
        "email":request.POST.get('email'),
        "password":request.POST.get('pass')
    })
    r = requests.post(rest_api_url,
                    headers=headers,
                    data=payload)
    if r.status_code == 200:
        request.session['uid'] = request.POST.get('email')
        return render(request, 'home.html')
    else:
        return HttpResponse("Error creating <a href='/'>Go Back</a>")


def logout(request):
    request.session['uid'] = '' 
    return redirect('index')



def signup(request):
    if request.method=='POST':
        auth.create_user(email=request.POST.get('email'),password=request.POST.get('password'))
        return redirect('index')
    else:
        return render(request,'signup.html')
