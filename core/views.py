# from django.shortcuts import render
import asyncio

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib import messages
import threading

from core.Utils.services import start_sync_scraper


def home(request):
    return render(request, 'core/home.html')

@login_required
def toggle_theme(request):
    user = request.user
    user.is_dark_mode = not user.is_dark_mode
    user.save()
    return JsonResponse({'status': 'success', 'is_dark_mode': user.is_dark_mode})

@login_required
def search_users(request):
    query = request.GET.get('search', '') # تأكد أن name="search" في الـ input
    if query:
        users = CustomUser.objects.filter(username__icontains=query)
    else:
        users = []

    # التغيير هنا: نرسل قالب النتائج فقط
    return render(request, 'core/partials/user_list_results.html', {'users': users})

@login_required
def live_jobs_view(request):
    query = request.GET.get('q', '')  # جلب كلمة البحث من مربع النص في المتصفح
    results = []

    if query:
        # تشغيل السكرابر وجلب النتائج مباشرة للمتصفح
        results = start_sync_scraper(query)

    return render(request, 'core/search_results.html', {
        'jobs': results,
        'query': query
    })
def trigger_scraper_view(request):
    if request.method == "POST":
        query = request.POST.get('q', 'Software Engineer')

        # تشغيل في مسار خلفي (Thread) لكي لا تتجمد الصفحة
        def bg_task():
            start_sync_scraper(query)

        thread = threading.Thread(target=bg_task)
        thread.start()

        messages.info(request, f"بدأت عملية السحب لـ '{query}'. ستظهر النتائج في الجدول خلال لحظات.")
        return redirect('jobs_list')  # أو أي صفحة تريدها

    return render(request, 'scraper_control.html')