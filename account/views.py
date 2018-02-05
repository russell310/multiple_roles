from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import CreateView, ListView
from .forms import TeacherSignUpForm, StudentSignUpForm
from .models import User, Teacher, Student
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import student_required, teacher_required
# Create your views here.


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teacher_dashboard')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student_dashboard')


@method_decorator([login_required, student_required], name='dispatch')
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher.html'


@method_decorator([login_required, teacher_required], name='dispatch')
class StudentListView(ListView):
    model = Student
    template_name = 'student.html'