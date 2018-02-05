from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Teacher, Student, User


class TeacherSignUpForm(UserCreationForm):
    subject = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        Teacher.objects.create(user=user, subject=self.cleaned_data.get('subject'))
        return user


class StudentSignUpForm(UserCreationForm):
    fathers_name = forms.CharField(required=True)
    mothers_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        Student.objects.create(
            user=user,
            fathers_name=self.cleaned_data.get('fathers_name'),
            mothers_name=self.cleaned_data.get('mothers_name'),
        )
        return user

