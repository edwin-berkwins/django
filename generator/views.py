from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    generatedpassword = ''
    length = int(request.GET.get('length'))

    createpassword = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('alphanum'):
        createpassword.extend('0123456789')

    if request.GET.get('symbols'):
        createpassword.extend('~!@#$%^&*()')

    if request.GET.get('capital'):
        createpassword.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    for i in range(length):
        generatedpassword += random.choice(createpassword)

    return render(request, 'generator/password.html', {'password' : generatedpassword })
