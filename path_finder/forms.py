from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class CountryCodeForm(forms.Form):
    code = forms.CharField(label='Country Code', 
                            max_length=3, 
                            widget=forms.TextInput(attrs={'placeholder': '(i.e. PAN)'}))

    def validate(self, value):
        super().validate(value)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'country-code-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-6'
        self.helper.form_action = 'index'
        self.helper.add_input(Submit('submit', 'Submit', css_id = 'my-submit', css_class='btn btn-primary'))
