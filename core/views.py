# from django.shortcuts import render

import threading
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, redirect

from accounts.models import CustomUser
from core.Utils.JobServices import JobServices
from core.Utils.statistical_analysis import get_statistical_analysis


# from core.Utils.services import start_sync_scraper

# @login_required
def home(request):
    # result=get_statistical_analysis()
    return render(request, 'core/home.html')

def labor_market_trends(request):
    result=get_statistical_analysis()
    return render(request, 'core/labor_market_trends.html',result)

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

# @login_required
# def live_jobs_view(request):
#     query = request.GET.get('q', '')  # جلب كلمة البحث من مربع النص في المتصفح
#     results = []
#
#     if query:
#         # تشغيل السكرابر وجلب النتائج مباشرة للمتصفح
#         results = start_sync_scraper(query)
#
#     return render(request, 'core/search_results.html', {
#         'jobs': results,
#         'query': query
#     })

# @login_required
# def trigger_scraper_view(request):
#     if request.method == "POST":
#         query = request.POST.get('q', 'Software Engineer')
#
#         # تشغيل في مسار خلفي (Thread) لكي لا تتجمد الصفحة
#         def bg_task():
#             start_sync_scraper(query)
#
#         thread = threading.Thread(target=bg_task)
#         thread.start()
#
#         messages.info(request, f"بدأت عملية السحب لـ '{query}'. ستظهر النتائج في الجدول خلال لحظات.")
#         return redirect('jobs_list')  # أو أي صفحة تريدها
#
#     return render(request, 'scraper_control.html')

@login_required
def search_skills(request):

    query = request.GET.get('search', '').strip()
    skills=JobServices.search_skills(query)
    # إذا كان الطلب من Tom Select (AJAX)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'json' in request.path:
        # print("****************************")
        results = [{'id': s.id, 'name': s.name} for s in skills]

        return JsonResponse({'results': results})

    # للاستخدامات الأخرى بـ HTMX التي تحتاج HTML
    return render(request, f'core/partials/skill_list_results.html', {'skills': skills})\

@login_required
def search_jobs(request):

    query = request.GET.get('search', '').strip()
    jobs=JobServices.search_jobs(query)
    # إذا كان الطلب من Tom Select (AJAX)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'json' in request.path:
        # print("****************************")
        results = [{'id': s.id, 'title': s.title} for s in jobs]

        return JsonResponse({'results': results})

    # للاستخدامات الأخرى بـ HTMX التي تحتاج HTML
    return render(request, f'core/partials/search_job_results.html', {'jobs': jobs})