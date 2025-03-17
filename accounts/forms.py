from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=True, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        email = cleaned_data.get('email')

       
        if password != password_confirm:
            self.add_error('password_confirm', 'رمزهای عبور همخوانی ندارند')

        
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'این ایمیل قبلاً ثبت شده است')
        return cleaned_data
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

