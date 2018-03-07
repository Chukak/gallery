from django import forms
from .models import ImageModel


class ImageForm(forms.ModelForm):
    """
    Image form.
    Set form for upload images.

    Metaclass has 3 attributes:
    1. model - ImageModel object.
    2. fields - fields, which include.
    3. widgets - dictionary of widgets.

    """
    class Meta:
        model = ImageModel
        fields = ['path_to_image', 'name']
        # widgets for fields
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control custom'}),
        }
