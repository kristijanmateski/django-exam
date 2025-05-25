from django import forms
from app.models import Izlozhba


class IzlozhbaForm(forms.ModelForm):
    class Meta:
        model = Izlozhba
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(IzlozhbaForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
