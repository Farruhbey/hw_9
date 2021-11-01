from django.forms import ModelForm
from shablon.models import *

class CreateGullarForm(ModelForm):

    class Meta:
        fields = ('nomi','rasmi', 'narxi','kategoriya')
        model = Gullar

class CreateKategoriyaForm(ModelForm):

    class Meta:
        fields = ('nomi',)
        model = Kategoriya