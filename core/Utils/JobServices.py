
from django.contrib.auth.decorators import login_required

from core.models import Skill


class SkillServices:

    @login_required
    def search_skills(query):

        if query:
            skills = Skill.objects.filter(
                Q(name__icontains=query) |
                Q(category__name__icontains=query)
            ).distinct()[:20]  # تحديد العدد لسرعة الاستجابة
        else:
            skills = Skill.objects.all()[:20]
        return skills