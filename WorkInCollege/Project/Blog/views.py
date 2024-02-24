from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Data
import json




@csrf_exempt
def main(request):

    if request.method == "POST":
        bodyUnicode = request.body.decode('utf-8')
        jsonBody= json.loads(bodyUnicode)
        createNewUser = Data(login = jsonBody['login'], password = jsonBody['password'])
        createNewUser.save()
    #elif request.method == 'GET':




    

    return render(request, 'index.html')

def me(request):
    return render(request, 'meBlog.html')

