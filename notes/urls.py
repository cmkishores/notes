from django.urls import path
from .views import NotesListView,DetailNoteView

urlpatterns= [
	path('notes/',NotesListView.as_view(),name='notes'),
	path('notes/<int:pk>/',DetailNoteView.as_view(),name='detailed'),
]