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
        label='Password',
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        strip=False,
        help_text='Enter the same password as before.',
    )

    grade = forms.ChoiceField(
        widget=forms.Select,
        choices=GRADE_CHOICES,
    )

    department = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = User
        fields = ('student_id', 'name', 'grade', 'department', 'phone_number')

    def clean_student_id(self):
        regex = r'^s\d\d\d\d\d\d$'
        student_id = self.cleaned_data.get('student_id')
        if not re.match(regex, student_id):
            raise forms.ValidationError('学籍番号が正しくありません.')
        return student_id

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
