from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))    
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    plans = (
        ('Free', 'Free'),
        ('Premium', 'Premium')
    )

    plan = forms.CharField(
        widget=forms.Select(choices=plans, attrs={'class': 'form-control'})
    )


class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))    
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    plans = (
        ('Free', 'Free'),
        ('Premium', 'Premium')
    )

    plan = forms.CharField(
        widget=forms.Select(choices=plans, attrs={'class': 'form-control'})
    )
    