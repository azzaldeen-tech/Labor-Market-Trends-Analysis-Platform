from django.shortcuts import render

app_name = 'members'

def dashboard_view(request):
    return render(request, f'{app_name}/dashboard.html')
