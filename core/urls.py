from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

app_name = 'core'
urlpatterns = [
    path('', home_view, name="index"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
