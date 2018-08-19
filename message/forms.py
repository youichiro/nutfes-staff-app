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
    importance = forms.ChoiceField(choices=IMPORTANCE_CHOICES, widget=forms.Select)

    class Meta:
        model = Message
        fields = ('text', 'importance')


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('text', )
