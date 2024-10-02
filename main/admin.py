from django.contrib import admin

from main.models import Faculty, Subject, Answer, FeedBack


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_faculty', 'subject', 'is_anonymous', 'file_name', 'by']
    list_display_links = ['id', 'get_faculty', 'subject', 'file_name']
    search_fields = ['id', 'file_name', 'subject__name']
    list_filter = ['subject__faculty__name']

    def get_faculty(self, obj):
        return obj.subject.faculty.name


class SubjectInlineAdmin(admin.TabularInline):
    model = Subject


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    inlines = [
        SubjectInlineAdmin
    ]

    list_display = ['name', 'short_name', 'created_on']
    list_display_links = ['name']
    search_fields = ['name']


class AnswerInlineAdmin(admin.TabularInline):
    model = Answer


@admin.register(Subject)
class FacultyAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInlineAdmin
    ]

    list_display = ['name', 'created_on']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['subject', 'owner', 'created_on']
    list_display_links = ['subject', 'owner']
