from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('book.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]