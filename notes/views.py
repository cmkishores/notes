from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Note

class NotesListView(ListView):
	model = Note
	template_name = 'notes.html'
	context_object_name = 'notelist'

class DetailNoteView(DetailView):
	model = Note
	template_name = 'note_detailed.html'


# Create your views here.
