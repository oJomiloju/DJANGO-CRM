from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, Homework


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	





# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    class_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Class Name", "class":"form-control"}), label="")
    professor = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Professor", "class":"form-control"}), label="")
    classroom = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Class Room", "class":"form-control"}), label="")
    days = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Monday, Tuesday...", "class":"form-control"}), label="")
    start_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={"placeholder":"Start Time", "class":"form-control"}), label="")
    end_time = forms.TimeField(required=True, widget=forms.TimeInput(attrs={"placeholder":"End Time", "class":"form-control"}), label="")
    credits = forms.DecimalField(required=True, widget=forms.NumberInput(attrs={"placeholder":"Credits", "class":"form-control"}), label="")
    semester = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Semester", "class":"form-control"}), label="")
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={"placeholder":"Description", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)


class AddHomeworkForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Title", "class":"form-control"}), label="")
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={"placeholder":"Description", "class":"form-control"}), label="")
    due_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"placeholder":"Due Date", "class":"form-control"}), label="")
    percentage_of_grade = forms.DecimalField(required=True, widget=forms.NumberInput(attrs={"placeholder":"Percentage of Grade", "class":"form-control"}), label="")
    submission_status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input"}), label="Submission Status")
    submission_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"placeholder":"Submission Date", "class":"form-control"}), label="")
    grade_received = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={"placeholder":"Grade Received", "class":"form-control"}), label="")
    attachments = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={"class":"form-control"}), label="Attachments")

    class Meta:
        model = Homework
        fields = '__all__'