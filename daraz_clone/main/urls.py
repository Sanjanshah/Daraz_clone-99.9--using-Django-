from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
           
    # ... your existing patterns ...
     path('', views.home, name='home'),
    
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)