from django.shortcuts import render


def index(request):
    """
    renders index page
    """
    return render(request, 'home/index.html')


def about(request):
    """
    renders about page
    """
    return render(request, 'home/about.html')


def privacy_policy(request):
    """
    renders privacy policy page
    """
    return render(request, 'home/privacy.html')
