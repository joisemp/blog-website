from django.shortcuts import render

def blogHome(request):
    return render(request, 'blog_home.html', {})
