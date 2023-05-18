# from dal import autocomplete

from django.conf.urls import re_path
# from django.contrib.auth.models import Group
from django.views import generic

from .forms import TForm
from .models import TModel


urlpatterns = [
    re_path(
        'test/(?P<pk>\d+)/$',
        generic.UpdateView.as_view(
            model=TModel,
            form_class=TForm,
        )
    ),
]
urlpatterns.extend(TForm.as_urls())
