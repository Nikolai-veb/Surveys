from django import forms
from .models import Conditions, Parameters, Surveys


class ConditionsForms(forms.ModelForm):
    """Форма создания условий"""

    class Meta:
        model = Conditions
        fields = ("name",)

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
        }


class ParametersForm(forms.ModelForm):
    """Форма создания параметров"""

    class Meta:
        model = Parameters
        fields = ("survey", "method", "condition", "deadlines_start", "deadlines_stop")

        widgets = {
            "survey": forms.Select(attrs={"class": "form-control border"}),
            "method": forms.Select(attrs={"class": "form-control border"}),
            "condition": forms.Select(attrs={"class": "form-control border"}),
            "deadlines_start": forms.DateInput(attrs={"class": "form-control border"}),
            "deadlines_stop": forms.DateInput(attrs={"class": "form-control border"}),

        }


class SurveysForm(forms.ModelForm):
    """Форма создания опросов"""

    class Meta:
        model = Surveys
        fields = ("name", "questions", "type_s")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "question": forms.Select(attrs={"class": "form-control border"}),
            "type_s": forms.Select(attrs={"class": "form-control border"}),

        }
