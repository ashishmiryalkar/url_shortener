from django.urls import path
from .views import UrlShortener
from django.views.generic import TemplateView

urlpatterns = [
    path('create/',TemplateView.as_view(template_name='create_short_url.html')),
    path('create_short_url_api/',UrlShortener.as_view())
]