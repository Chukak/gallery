from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from image_gallery.views import DownloadView, ImageView

"""
Urls configuration.
1. ^admin/ - admin site. url - admin/
2. ^$ - homepage site
3. ^download/ - download page, url - download/

Also set static and media files.

"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ImageView.as_view(), name='gallery'),
    url(r'^download/', DownloadView.as_view(), name='download'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # get staticfiles path
