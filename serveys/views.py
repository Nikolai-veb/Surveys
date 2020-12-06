from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from .forms import SurveysForm, ConditionsForms, ParametersForm
from .models import Conditions, Parameters, Type_answer, Type_surveys, Surveys, Method_survey


class SurveysListView(ListView):
    """Список опросов"""
    model = Surveys
    template_name = "surveys/surveys_list.html"
    context_object_name = "surveys"


class SurveysView(CreateView):
    """Оброботчик формы создания опроса"""
    model = Surveys
    form_class = SurveysForm
    template_name = "surveys/surveys.html"
    success_url = reverse_lazy("condition")


class ConditionView(CreateView):
    """Оброботчик формы создания условий"""
    model = Conditions
    form_class = ConditionsForms
    template_name = "surveys/create_condition.html"
    success_url = reverse_lazy("parameters")


class ParametersView(CreateView):
    """Оброботчик формы создания условий"""
    model = Parameters
    form_class = ParametersForm
    template_name = "surveys/create_parameters.html"
    success_url = reverse_lazy("parameters")
