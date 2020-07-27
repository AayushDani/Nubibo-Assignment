from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    priority_options = (
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),   
    )
    priority = forms.CharField(
        widget=forms.Select(choices=priority_options, attrs={'class': 'form-control'})
    )
    
    status_options = (
        ('PENDING', 'PENDING'),
        ('ON_PROGRESS', 'ON_PROGRESS'),
        ('COMPLETED', 'COMPLETED'),
        ('SUSPENDED', 'SUSPENDED'),
    )
    status = forms.CharField(
        widget=forms.Select(choices=status_options, attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control kinda-rounded', 'placeholder': "Enter the description for your task..."})
    )
