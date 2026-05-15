from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages as django_messages
from django.utils.translation import gettext_lazy as _

from companies.Utils.services import get_filtered_applications, get_job_simple_applications
from companies.models import Job, JobApplication
from core.Utils.JobServices import JobServices
from core.app_links import AppLinks
from core.helpers import  get_current_date
from core.models import Skill
from members.decorators import member_required
from members.forms import MemberProfileForm
from members.models import MemberProfile

app_name = 'members'

# @member_required
# @login_required
# def statistics(request):
#     jobs_count=JobServices.get_jobs_count()

@member_required
@login_required
def dashboard_view(request):

    return render(request, f'{app_name}/dashboard.html')\

@member_required
@login_required
def profile_view(request):

    profile, created = MemberProfile.objects.get_or_create(user=request.user)
    skills_list = Skill.objects.all().values('id', 'name')

    if request.method == "POST":
        form = MemberProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(AppLinks.Dashboards.MEMBER)
    else:
        form = MemberProfileForm(instance=profile)

    return render(request, f'{app_name}/profile/form.html',{
        'skills_list': skills_list,
        'form':form,
    })


@member_required
@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    has_applied = JobApplication.objects.filter(job=job, member=request.user.profile).exists()
    return  render(request,f"{app_name}/jobs/detail.html",{
        'job':job,
        'has_applied':has_applied
    })


@member_required
@login_required
def job_join(request, pk):
    job = get_object_or_404(Job, pk=pk)
    next_url = request.META.get('HTTP_REFERER')
    fallback_url = redirect(f"{app_name}:advertised_jobs").url
    destination = next_url if next_url else fallback_url
    if not hasattr(request.user, 'profile'):
        django_messages.error(request, _('يرجى إكمال ملفك الشخصي أولاً.'))
        return redirect(destination)

    member = request.user.profile
    exists = JobApplication.objects.filter(job=job, member=member).exists()

    if exists:
        django_messages.warning(request, _('لقد قمت بطلب الانضمام لهذه الوظيفة مسبقاً.'))
    else:
        JobApplication.objects.create(
            job=job,
            member=member,
        )
        django_messages.success(request, _('تم ارسال طلب الانضمام للوظيفة بنجاح.'))

    return redirect(destination)


@login_required
def cancel_job_join(request, pk):
    job = get_object_or_404(Job, pk=pk)
    next_url = request.META.get('HTTP_REFERER')
    fallback_url = redirect(f"{app_name}:advertised_jobs").url
    destination = next_url if next_url else fallback_url
    if hasattr(request.user, 'profile'):
        member = request.user.profile
        application = JobApplication.objects.filter(job=job, member=member).first()
        if application:
            application.delete()
            django_messages.success(request, _('تم إلغاء طلب الانضمام للوظيفة بنجاح.'))
        else:
            django_messages.warning(request, _('أنت غير مسجل في هذه الوظيفة أصلاً.'))
    else:
        django_messages.error(request, _('لا تملك ملف تعريف عضو لإتمام هذه العملية.'))

    return redirect(destination)


@member_required
@login_required
def advertised_jobs(request):
    # current_date=get_current_date()

    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    applied_jobs_ids = []
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        applied_jobs_ids = JobApplication.objects.filter(member=request.user.profile)\
            .values_list('job_id', flat=True)

    context = {
        'jobs': jobs,
        'applied_jobs_ids': applied_jobs_ids,
    }


    return render(request, f'{app_name}/jobs/advertised_jobs.html', context)\


@member_required
@login_required
def job_applications(request):
    member=request.user.profile
    # my_filter = {'job__company': company}
    job_applications = get_filtered_applications(member=member)
    simplified_apps = get_job_simple_applications(job_applications)
    return render(request, f'{app_name}/jobs/job_applications.html',
                  {'job_applications': simplified_apps})
@login_required
@member_required
def applied_jobs(request):


    applied_jobs = []

    if request.user.is_authenticated and hasattr(request.user, 'profile'):

        # جلب أرقام الوظائف التي قدم عليها هذا المستخدم فقط
        job_ids = JobApplication.objects.filter(member=request.user.profile).values_list('job', flat=True)

        # 2. جلب الوظائف التي تنتمي لهذه القائمة
        applied_jobs = Job.objects.filter(id__in=job_ids).order_by('-created_at')

        context = {
            'jobs': applied_jobs,
        }


    return render(request, f'{app_name}/jobs/applied_jobs.html', context)

@login_required
@member_required
def search_jobs(request):

    query = request.GET.get('search', '').strip()
    jobs=JobServices.search_jobs(query)

    return render(request, f'{app_name}/partials/search_job_results.html', {'jobs': jobs})

