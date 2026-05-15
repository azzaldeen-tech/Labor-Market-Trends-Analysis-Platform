from companies.models import Job, JobApplication


class CompanyService:

    def get_jobs_count(self, company_id,active=True):
        return Job.objects.filter(company_id=company_id, is_active=active).count()
    def get_active_jobs_count(self, company_id):
        return self.get_jobs_count(company_id,True)
    def get_non_active_jobs_count(self, company_id):
        return self.get_jobs_count(company_id,False)

    def get_pending_applications(self, company_id):
        return JobApplication.objects.filter(job__company_id=company_id,
                                             status=JobApplication.Status.PENDING).count()

    @staticmethod
    def get_dashboard_stats(self,company_id):
        service=self()
        return {
            "jobs_count": service.get_active_jobs_count(company_id),
            "apps_count": service.get_pending_applications(company_id),
            # "last_update": timezone.now()
        }