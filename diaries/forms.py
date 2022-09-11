from django import forms
from diaries.models import Diary

# --------------------------------------------------
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'
        widgets = {
            'date': forms.SelectDateWidget
        }
