from dal import autocomplete

from django.urls import re_path

from .models import TModel


urlpatterns = [
    re_path(
        'test-autocomplete/$',
        autocomplete.Select2QuerySetView.as_view(model=TModel),
        name='select2_fk',
    ),
]
