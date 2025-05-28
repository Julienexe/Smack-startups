from .models import Stall, Category
from django import forms    

class StallForm(forms.ModelForm):
    class Meta:
        model = Stall
        #all fields except created_at and updated_at
        # created_at and updated_at are automatically set by Django
        # when the model is saved, so we don't need to include them in the form
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'categories': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'name': 'Stall Name',
            'description': 'Description',
            'image': 'Stall Image',
            'categories': 'Categories',
            'cohort_name': 'Cohort Name',
            'cohort_year': 'Years when You Attended SMACK',
            'phone_number': 'Mobile Phone',
            'email': 'Email',
            'specifics': 'Product Specifics',
            'links': 'Links',
            'other_details': 'Any Other Details',
        }