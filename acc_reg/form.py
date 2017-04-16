from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(label="User name", max_length=20)
	password = forms.CharField(label="Pass word", max_length=20, widget=forms.PasswordInput)
	email = forms.EmailField(label="Email", max_length=40)

class LoginForm(forms.Form):
	username = forms.CharField(label="User name", max_length=20)
	password = forms.CharField(label="Pass word", max_length=20, widget=forms.PasswordInput)