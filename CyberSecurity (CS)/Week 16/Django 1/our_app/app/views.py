from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def welcome(request):
    name = request.GET['name']
    email = request.GET['email']
    birthday = request.GET['birthday']
    context_data = {
        'name': name,
        'email': email,
        'birthday': birthday,
    }
    return render(request, 'welcome.html', context=context_data)