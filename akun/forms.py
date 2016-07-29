from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form_field', 'size': '20'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_field', 'size': '20'}))

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Username'

	def confirm_login_allowed(self, user):
		if user.username == '':
			raise forms.Validation('username tidak boleh kosong')

