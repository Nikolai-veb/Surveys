from django import forms
from .models import Conditions, Parameters, Surveys


class ConditionsForms(forms.ModelForm):
    """Форма создания условий"""

    class Meta:
        model = Conditions
        fields = ("name",)


class ParametersForm(forms.ModelForm):
    """Форма создания параметров"""

    class Meta:
        model = Parameters
        fields = ("survey", "method", "condition", "deadlines_start", "deadlines_stop")


class SurveysForm(forms.ModelForm):
    """Форма создания опросов"""

    class Meta:
        model = Surveys
        fields = ("name", "questions", "type_s")
