import django
from django.conf import settings
from django.conf.urls import include, re_path
from django.contrib import admin

import views


urlpatterns = [
    re_path(r'^$', views.IndexView.as_view()),

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/', views.LoginView.as_view()),

    re_path(r'^secure_data/', include('secure_data.urls')),
    re_path(r'^linked_data/', include('linked_data.urls')),
    re_path(r'^rename_forward/', include('rename_forward.urls')),
    re_path(r'^forward_different_fields/',
        include('forward_different_fields.urls')),
    re_path(r'^select2_nestedadmin/', include('select2_nestedadmin.urls')),

    re_path(r'^select2_foreign_key/', include('select2_foreign_key.urls')),
    re_path(r'^select2_list/', include('select2_list.urls')),
    re_path(r'^select2_generic_foreign_key/',
        include('select2_generic_foreign_key.urls')),
    re_path(r'^select2_many_to_many/',
        include('select2_many_to_many.urls')),
    re_path(r'^select2_one_to_one/', include('select2_one_to_one.urls')),

    re_path(r'^select2_outside_admin/', include('select2_outside_admin.urls')),
    re_path(r'^select2_taggit/', include('select2_taggit.urls')),
    re_path(r'^nested_admin/', include('nested_admin.urls')),
]

if django.VERSION < (2, 0, 0):
    # pending upstream support
    urlpatterns += [
        re_path(r'^select2_tagging/', include('select2_tagging.urls')),
        re_path(r'^select2_gm2m/', include('select2_gm2m.urls')),
        re_path(r'^select2_generic_m2m/', include('select2_generic_m2m.urls')),
    ]

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls)), ]
