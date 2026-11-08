from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.inicio, name='inicio'),
    path('blog/', include('blog.urls')),
]