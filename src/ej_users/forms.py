from captcha.fields import ReCaptchaField
from django import forms


class EJSignupForm(forms.Form):
    full_name = forms.CharField(max_length=120, label='Nome')
    captcha = ReCaptchaField(label='')

    field_order = ['full_name', 'email', 'password1', 'password2', 'capcha']

    def signup(self, user):
        full_name = self.cleaned_data['full_name']
        user.first_name, _, user.last_name = full_name.partition(' ')
        user.save()