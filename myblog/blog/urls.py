from django.urls import path

from . import views

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<int:pk>-<str:slug>/', views.EntryDetail.as_view(), name='entry_detail'),
]