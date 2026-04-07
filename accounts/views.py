from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

from django.http import JsonResponse


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data=json.loads(request.body)

        username=data.get('username')
        password=data.get('password')
        
        User.objects.create_user(
            username=username, password=password )




        return JsonResponse({'message': 'user created'})
    
    return JsonResponse({'message': 'error, only post working'})