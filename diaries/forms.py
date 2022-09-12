from django import forms
from diaries.models import Diary

# --------------------------------------------------
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'
        labels = {
            'subject_id': '科目コース',
            'student_id': '生徒',
            'teacher_id': '担当講師',
        }
        
        widgets = {
            'range': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3}),
            'subject_id': forms.Select(attrs={'class': 'form-control'}),
            'homework': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3}),
            'date': forms.NumberInput(attrs={
                'type': 'date', 
                'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3}),
            'teacher_id': forms.Select(attrs={'class': 'form-control'}),
            'student_id': forms.Select(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3}),            
        }
