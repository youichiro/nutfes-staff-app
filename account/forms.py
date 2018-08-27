import re
from django import forms
from django.contrib.auth import password_validation
from .models import User, Department


GRADE_CHOICES = (
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('B3', 'B3'),
    ('B4', 'B4'),
    ('M1', 'M1'),
    ('M2', 'M2'),
    ('D1', 'D1'),
    ('D2', 'D2'),
    ('D3', 'D3'),
)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='パスワード(確認)',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        help_text='上のパスワードと同じパスワードを入力してください.',
    )

    grade = forms.ChoiceField(
        label='学年',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=GRADE_CHOICES,
    )

    department = forms.ModelMultipleChoiceField(
        label='局・部門',
        queryset=Department.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True,
        help_text='複数選択できます.',
    )

    class Meta:
        model = User
        fields = ('student_id', 'name', 'grade', 'department', 'phone_number')
        labels = {
            'student_id': '学生番号',
            'name': '名前',
            'phone_number': '電話番号'
        }
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_student_id(self):
        regex = r'^s\d\d\d\d\d\d\d\d$'
        student_id = self.cleaned_data.get('student_id')
        if not re.match(regex, student_id):
            raise forms.ValidationError('学籍番号が正しくありません.')
        return student_id

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if ' ' in name or '　' in name:
            raise forms.ValidationError('空白を入れずに入力してください.')
        return name

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('パスワードが一致しません.')
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            self.save_m2m()  # ManyToManyフィールドの保存
        return user
