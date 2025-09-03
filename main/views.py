from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406417992',
        'name': 'Mahesa Gerrardybhumi',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
