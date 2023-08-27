from django.forms import ModelForm
from django import forms
from .models import *

# USER AUTHENTICATION


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})



class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})




class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GradeForm, self).__init__(*args, **kwargs)

        # Custom sorting function to order grades with '+' sign higher than the rest
        def custom_sort_key(grade):
            return (grade.name[:-1], grade.name[-1] if grade.name[-1] == '+' else 'z')

        grades = Grade.objects.all()
        sorted_grades = sorted(grades, key=custom_sort_key)

        # Update the choices of the 'name' field
        self.fields['name'].choices = [(grade.name, grade.name) for grade in sorted_grades]

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})




