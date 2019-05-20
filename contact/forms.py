from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text='200 characters max.')#name of sender
    email = forms.EmailField(required=True)#email of sender
    comment = forms.CharField(required=True, widget=forms.Textarea)#comment