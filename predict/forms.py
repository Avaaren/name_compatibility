from django import forms

from .models import Relationship

class RelationshipForm(forms.ModelForm):

    class Meta:
        model = Relationship
        fields = ('male_name', 'female_name')

    def __init__(self, *args, **kwargs):
        super(RelationshipForm, self).__init__(*args, **kwargs)
        self.fields['male_name'].widget = forms.TextInput(attrs={
            'id': 'man-search-field',
            'placeholder': 'Man'})
        self.fields['female_name'].widget = forms.TextInput(attrs={
            'id': 'woman-search-field',
            'placeholder': 'Woman'})