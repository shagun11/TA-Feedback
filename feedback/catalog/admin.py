# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Course, TAssistant, Feedback


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'term', 'year')
    fields = ('name', 'term', 'year', 'user')
    list_filter = ('name', 'term')
    search_fields = ('name', 'user', 'year',)

    def has_delete_permission(self, request, obj=None):
        return False


class TAssistantAdmin(admin.ModelAdmin):
    fields = ('name', 'course')
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        return False


class FeedbackAdmin(admin.ModelAdmin):
    fields = ('ta', 'course', 'text', 'add_details', 'st_details', 'date')
    list_display = ('ta', 'course', 'add_details', 'date')
    list_filter = ('ta_id', 'course_id', 'date')
    search_fields = ('text', 'date',)

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(FeedbackAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        course_id = Course.objects.get(user__id=request.user.id)
        return qs.filter(course=course_id)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Course, CourseAdmin)
admin.site.register(TAssistant, TAssistantAdmin)
admin.site.register(Feedback, FeedbackAdmin)