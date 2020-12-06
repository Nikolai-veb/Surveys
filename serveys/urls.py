from django.urls import path
from . import views

urlpatterns = [
    path("", views.SurveysListView.as_view(), name="surveys_list"),
    path("survey/", views.SurveysView.as_view(), name="surveys"),
    path("condition/", views.ConditionView.as_view(), name="condition"),
    path("parameters/", views.ParametersView.as_view(), name="parameters"),
]
