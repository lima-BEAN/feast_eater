from django import forms
from .models import Food

class KitchenForm(forms.Form):
    k_name = forms.CharField(max_length=50, required=True, label='name')
    open_time = forms.CharField(max_length=10, required=True)
    close_time = forms.CharField(max_length=10, required=True)
    image = forms.ImageField(required=False)
    WORKING_DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday',  'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    working_days = forms.MultipleChoiceField(choices=WORKING_DAYS, required=True, widget=forms.CheckboxSelectMultiple)

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
        exclude = ['kitchen']
