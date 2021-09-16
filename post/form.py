from django import forms

class AddAutorsForm(forms.Form):
    Nick = forms.CharField(label = 'Nick')
    email = forms.EmailField(label = 'e-mail')

    def clean(self):
        cleaned_data = super().clean()
        Nick = cleaned_data.get('Nick')
        email = cleaned_data.get('email')

        if not (Nick or email):
            raise forms.ValidationError('Nie podano wymaganych danych')
        else:
            raise forms.ValidationError('Bujaj sie')