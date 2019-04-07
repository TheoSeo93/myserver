
from django.urls import path, include
from restaurant import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('menusection/', views.SectionList.as_view()),
    path('menusection/<int:pk>', views.SectionDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
