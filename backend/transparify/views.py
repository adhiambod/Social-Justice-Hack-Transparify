from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Renders the homepage

def about_us(request):
    return render(request, 'about_us.html')  # Renders the about page

def mission_vision(request):
    return render(request, 'mission_vision.html')  # Renders the mission and vision page
