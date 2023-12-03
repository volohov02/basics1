from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogapp'

urlpatterns = [
    path('', views.VacancyListView.as_view(), name='index'),
    path('create/', views.VacancyCreateView.as_view(), name='create'),
    path('contact/', views.ContactCreateView().contact_view, name='contact'),
    path('skill-list', views.SkillsListView.as_view(), name='skills_list'),
    path('skill-detail/<int:pk>/', views.SkillsDetailView.as_view(), name='skill_detail'),
    path('post/<int:id>/', views.VacancyDetailView.as_view(), name='post'),
    path('skill-create/', views.SkillsCreateView.as_view(), name='skill_create'),
    path('skill-update/<int:pk>/', views.SkillsUpdataView.as_view(), name='skill_update'),
    path('skill-delete/<int:pk>/', views.SkillsDeleteView.as_view(), name='skill_delete'),
]

if settings.DEBUG:
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))