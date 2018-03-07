from django import forms
from django.contrib import admin
from image_gallery.models import ImageModel


class AdminForm(forms.ModelForm):
    """
    Admin form.
    Has metaclass with model and includes fields for form:
    1. path_to_image - path to image.
    2. name - image name.
    3. datetime - date, when image uploaded.

    """
    class Meta:
        model = ImageModel
        fields = ["path_to_image", "name", "datetime"]


@admin.register(ImageModel)
class AdminModel(admin.ModelAdmin):
    """
    Admin model with decorator.
    Has 2 attributes:
    1. form - admin form.
    2. list_display - fields, which displayed in form.

    Also has 1 override method
    1. save_model - set size to form.

    """
    form = AdminForm
    list_display = ("name", "datetime", "size")

    def save_model(self, request, obj, form, change):
        form.instance.size = request.FILES["path_to_image"].size
        return super().save_model(request, obj, form, change)
