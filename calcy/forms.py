from django import forms

class CalcyForm(forms.Form):
    OPERATOR_CHOICES = [
        ('+', 'Addition'),
        ('-', 'Subtraction'),
        ('*', 'Multiplication'),
        ('/', 'Division'),
    ]

    value1 = forms.IntegerField(label='First Value')
    value2 = forms.IntegerField(label='Second Value')
    operation = forms.ChoiceField(choices=OPERATOR_CHOICES, label='Operation')
