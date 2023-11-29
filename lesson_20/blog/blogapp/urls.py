from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('create/', views.create_post, name='create'),
    path('post/<int:id>', views.post, name='post')
]

if settings.DEBUG:
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))