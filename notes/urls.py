from django.urls import path

from . import views

urlpatterns = [
    path('notes',views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>',views.detail, name='notes.detail'),
    path('notes/create',views.NotesCreateView.as_view(), name='notes.create'),
    path('notes/<int:pk>/edit',views.NotesUpdateView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete',views.NotesDeleteView.as_view(), name='notes.delete'),
    
]