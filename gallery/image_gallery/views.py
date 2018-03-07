from .models import ImageModel
from .forms import ImageForm
from django.views.generic import CreateView, TemplateView


class ImageView(TemplateView):
    """
    Image view.
    Has 1 attribute:
    1. template_name - path to template for this view.

    Also has 2 override method:
    1. get_quesryset - returns 6 ImageModel objects, sorted by datetime.
    2. get_context_data - set context for template and returns it.
    In context add key "object_list", which is dictionary with keys:
    path - path to image url, size - image size in bytes,
    name - image name, time - date, when image uploaded.

    """
    template_name = 'gallery/photos.html'

    def get_queryset(self):
        """
        Get ImageModel objects.

        """
        return ImageModel.objects.all().order_by('-datetime')[:6]

    def get_context_data(self, **kwargs):
        """
        Set context data for template.

        """
        context = super().get_context_data(**kwargs)
        context['object_list'] = [{
                'path': obj.path_to_image.url,
                'size': obj.size,
                'name': obj.name,
                'time': obj.datetime.strftime('%d %B %Y in %H:%M'),
            } for obj in self.get_queryset()]
        return context


class DownloadView(CreateView):
    """
    Download view.
    Has 3 attributes:
    1. form_class - form class, which download image.
    2. template_name - path to template for this view.
    3. success_url - url, which is redirected in case of success.

    Also has 1 override method:
    1. form_valid - set image size to form and returns this method.

    """
    form_class = ImageForm
    template_name = 'gallery/download.html'
    success_url = '/'

    def form_valid(self, form):
        """
        Set size to form and returns this method.
        """
        # set size in bytes form model image object
        form.instance.size = self.request.FILES['path_to_image'].size
        return super().form_valid(form)
