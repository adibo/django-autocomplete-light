from dal import autocomplete

from django.urls import re_path
from django.contrib.auth.models import Group
from django.views import generic

from .forms import TForm
from .models import TModel


urlpatterns = [
    re_path(
        '^select2-generic-m2m/$',
        autocomplete.Select2QuerySetSequenceView.as_view(
            queryset=autocomplete.QuerySetSequence(
                Group.objects.all(),
                TModel.objects.all(),
            )
        ),
        name='select2_generic_m2m',
    ),
    re_path(
        'test/(?P<pk>\d+)/$',
        generic.UpdateView.as_view(
            model=TModel,
            form_class=TForm,
        )
    ),
]
