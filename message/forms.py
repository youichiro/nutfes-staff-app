from django import forms
from .models import Message, Reply


IMPORTANCE_CHOICES = (
    ('なし', 'なし'),
    ('要確認', '要確認'),
    ('報告', '報告'),
    ('確認', '確認'),
    ('その他', 'その他'),
)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text', 'importance')
        labels = {'text': '', 'importance': '重要度'}
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'メッセージ'}),
            'importance': forms.Select(attrs={'class': 'form-control'}, choices=IMPORTANCE_CHOICES),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('text', )
