from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=13)

    def clean_first_name(self):
        nm = self.cleaned_data.get('first_name')
        if not nm:
            raise forms.ValidationError('name mut be required')
        if not nm.isalpha():
            raise forms.ValidationError('name mut alphabate')

        return nm
    

    def clean_last_name(self):
        lnm = self.cleaned_data.get('last_name')
        if not lnm:
            raise forms.ValidationError('l name mut be required')
        if not lnm.isalpha():
            raise forms.ValidationError('l name mut alphabate')

        return lnm


    
    

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if '@' not in email or '.' not in email:
            raise forms.ValidationError('invalid email')
        
        return email


    def phone(self):
        phn=self.cleaned_data.get('mobile')
        if len(phn)>13 or len(phn)<10:
            raise forms.ValidationError('invalid phone')
        
        return phn
