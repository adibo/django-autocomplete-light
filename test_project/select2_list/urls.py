from django.conf.urls import re_path

from .views import Select2ListViewAutocomplete


urlpatterns = [
    re_path(
        'test-autocomplete/$',
        Select2ListViewAutocomplete.as_view(),
        name='select2_list',
    ),
]
