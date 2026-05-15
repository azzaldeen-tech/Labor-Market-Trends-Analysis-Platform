from companies.Utils.services import CompanyService


def company_stats(request):
    profile=request.user.profile()
    if profile:
        company_id = profile.id
        return {
            'dashboard_stats': CompanyService.get_dashboard_stats(company_id)
        }
    return {}