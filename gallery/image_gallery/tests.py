import os
import re
from django.test import TestCase
from .models import get_image_path


class ImagePathTest(TestCase):
    def test_image_path(self):
        """
        Test image path in the format images/[random uuid].[file extension]
        (for example, images/f278c317-a946-4802-868e-42ddde3d3f56.png, etc).

        test_list - list of files in the format [image name].[file extension]
        (for example, image.jpg, image.png, etc).

        """
        test_list = [
            "image.jpg",
            "picture.png",
            "random_image.jpeg",
        ]
        for pattern in test_list:
            uuid_image = get_image_path(None, pattern)
            file_extension = os.path.splitext(pattern)[1]
            regex = re.compile(
                '^images/[0-9A-F]{{8}}-[0-9A-F]{{4}}-4[0-9A-F]{{3}}-'
                '[89AB][0-9A-F]{{3}}-[0-9A-F]{{12}}{extension}$'.format(extension="\\" + file_extension),
                flags=re.IGNORECASE
            )
            self.assertTrue(re.fullmatch(regex, uuid_image))
