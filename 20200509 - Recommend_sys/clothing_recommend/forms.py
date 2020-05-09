# -*- coding:utf-8 -*-
from django import forms


class RecommendForm(forms.Form):
    style = forms.CharField()
    popular = forms.CharField()
    pattern = forms.CharField()

