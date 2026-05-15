from django.db.models import Count

from django.db.models.functions import TruncDate

import json
from django.shortcuts import render

from companies.models import Job
from core.models import Skill, SkillCategory


def get_top_skills():
    # نستخدم required_skills وهو الـ related_name في علاقة ManyToMany
    top_skills = Skill.objects.annotate(
        jobs_count=Count('required_skills')
    ).order_by('-jobs_count')[:10]  # جلب أفضل 10 مهارات

    # تحويل البيانات لتناسب Chart.js
    labels = [skill.name for skill in top_skills]
    data = [skill.jobs_count for skill in top_skills]

    return labels, data





def get_top_categories():

    top_categories = SkillCategory.objects.annotate(
        jobs_count=Count('jobs')
    ).order_by('-jobs_count')

    labels = [cat.name for cat in top_categories]
    data = [cat.jobs_count for cat in top_categories]

    return labels, data



def get_jobs_timeline():
    timeline_data = Job.objects.annotate(
        date=TruncDate('created_at')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date')

    # تحويل التاريخ إلى نص ليقبله JavaScript
    labels = [item['date'].strftime("%Y-%m-%d") for item in timeline_data]
    data = [item['count'] for item in timeline_data]

    return labels, data



def get_statistical_analysis():
    # مهارات
    s_labels, s_data = get_top_skills()
    # قطاعات
    c_labels, c_data = get_top_categories()
    # زمن
    t_labels, t_data = get_jobs_timeline()

    return {
        's_labels': json.dumps(s_labels),
        's_data': json.dumps(s_data),
        'c_labels': json.dumps(c_labels),
        'c_data': json.dumps(c_data),
        't_labels': json.dumps(t_labels),
        't_data': json.dumps(t_data),
    }
