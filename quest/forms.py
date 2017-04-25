from django.forms import ModelForm
from .models import Quest


class AddForm(ModelForm):
    class Meta:
        model = Quest
        fields = ['title', 'abstract', 'sub_task']