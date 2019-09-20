from django.urls import path
from .views import NotesListView,DetailNoteView,AddNotesView,EditNotesView,DeleteNoteView

urlpatterns= [
	path('notes/',NotesListView.as_view(),name='notes'),
	path('notes/<int:pk>/',DetailNoteView.as_view(),name='detailed'),
	path('notes/new/', AddNotesView.as_view(),name='addnotes'),
	path('notes/<int:pk>/edit',EditNotesView.as_view(),name='editnotes'),
	path('notes/<int:pk>/delete/',DeleteNoteView.as_view(),name='deletenotes')
]