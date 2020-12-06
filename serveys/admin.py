from django.contrib import admin
from .models import Type_answer, Type_surveys, Questions, Surveys, Conditions, Parameters, Method_survey


@admin.register(Type_surveys)
class Type_surveysAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Type_answer)
class Type_answerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "slug")
    list_filter = ("question",)
    search_fields = ("question",)
    prepopulated_fields = {"slug": ("question",)}


@admin.register(Surveys)
class SurveysAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", "create", "type_s")
    search_fields = ("name", "type_s")



@admin.register(Conditions)
class ConditionsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Method_survey)
class Method_surveyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Parameters)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ("survey", "method")
    search_fields = ("survey",)
