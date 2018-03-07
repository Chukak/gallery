import os
import uuid
from django.db import models
from django.utils.timezone import now


def get_image_path(instance, file):
    """
    Set image path. Use uuid and end of file (for example, uuid.jpg).
    Uuid - random 14-bit sequence, .jpg - file extension (for example, .jpg, .png, etc).

    Take two arguments:
    1. instance - model object.
    2. file - file, which uploaded.

    Returns path in the format - "images/[random uuid].[file extension]"

    """
    return "images/{0}{1}".format(uuid.uuid1(), os.path.splitext(file)[1])


class ImageModel(models.Model):
    """
    Image model.
    Has 4 attributes:
    1. path_to_image - path to image in dir, get path from get_image_path func.
    2. datetime - date, when image uploaded.
    3. size - size of image in bytes.
    4. name - name of image, max length - 80.

    Also have 1 override method:
    1. __str__ - returns image name.

    """
    path_to_image = models.ImageField(upload_to=get_image_path, verbose_name="Path to image")
    datetime = models.DateTimeField(default=now, db_column="time_load", verbose_name="Time to load")
    size = models.IntegerField(db_column="size", verbose_name="Size in bytes")
    name = models.CharField(db_column="image_name", verbose_name="Name image", max_length=80)

    class Meta:
        """
        Model metaclass
        """
        verbose_name = "Image model"

    def __str__(self):
        """
        Returns image name in the format "Image: image_name".

        """
        return "Image: " + self.name
