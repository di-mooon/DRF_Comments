import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_urls

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('comments.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += doc_urls
