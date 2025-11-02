from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]


handler404 = "myapp.views.errors_views.custom_404"
handler500 = "myapp.views.errors_views.custom_500"
