from django.conf import settings
from django.contrib import admin
from django.urls import path, include

import accounts.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth.socialaccount.urls")),
    # path('auth-receiver', accounts.views.auth_receiver, name='auth_receiver'),
    path("", include("pages.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
