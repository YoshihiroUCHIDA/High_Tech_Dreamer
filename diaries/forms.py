from django import forms
from diaries.models import Diary
from datetime import date, datetime

# --------------------------------------------------
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        
        # 送信フィールド
        fields = '__all__'
        
        # ラベル表示の編集
        labels = {
            'subject_id': '科目コース',
            'student_id': '生徒',
        }
        
        # タグの属性
        widgets = {
            'range': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'subject_id': forms.Select(attrs={'class': 'form-control'}),
            'homework': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date': forms.NumberInput(attrs={'type': 'date', 'class': 'form-control','max':date.today()}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'teacher_id': forms.Select(attrs={'class': 'form-control'}),
            'student_id': forms.Select(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),            
        }
