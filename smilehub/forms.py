from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,  # Makes this field required
        widget=forms.TextInput(attrs={
            'name': 'name',
            'id': 'name-id',
            'placeholder': 'Enter your name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        required=True,  # Makes this field required
        widget=forms.EmailInput(attrs={
            'name': 'email',
            'id': 'email-id',
            'placeholder': 'Enter your email',
            'required': 'required'
        })
    )
    message = forms.CharField(
        required=True,  # Makes this field required
        widget=forms.Textarea(attrs={
            'name': 'message',
            'id': 'message-id',
            'placeholder': 'Enter your message',
            'required': 'required',
            'rows': 5,  # Optional: set number of rows for the textarea
            'cols': 30  # Optional: set number of columns for the textarea
        })
    )
