from django.urls import re_path

from .views import UpdateView


urlpatterns = [
    re_path(
        r'^$',
        UpdateView.as_view(),
        name='select2_outside_admin',
    ),
]
