from django.contrib import admin

from companies.models import Assessment, Company, Metric


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    pass


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    pass


class AssessmentInline(admin.TabularInline):
    model = Assessment
    extra = 1


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (AssessmentInline, )
