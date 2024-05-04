from django.forms import ModelForm
from .models import Phones


class PhoneForm(ModelForm):
    class Meta:
        model = Phones
        fields = '__all__'
