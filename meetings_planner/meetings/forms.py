from django.db import models
from datetime import time
from django.forms import ModelForm, DateInput, TimeInput, TextInput
from datetime import date
from django.db import models
from .models import Meeting

from django.core.exceptions import ValidationError


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start_time': TimeInput(attrs={"type": "time"}),  
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "4"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meetings cannot be in the past")
        return d



