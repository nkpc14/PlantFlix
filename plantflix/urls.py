from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('users/', include('useraccount.urls')),
    path('course/', include('course.urls')),
    path('quiz/', include('quiz.urls')),
    path('manage/', include('management.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/reg/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
