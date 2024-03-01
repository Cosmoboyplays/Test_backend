from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('hub.urls', namespace='hub')),
    # path('user/', include('users.urls', namespace='user')),
]
