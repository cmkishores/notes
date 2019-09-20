from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Note
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class NotesListView(ListView):
	model = Note
	template_name = 'notes.html'
	context_object_name = 'notelist'

class DetailNoteView(DetailView):
	model = Note
	template_name = 'note_detailed.html'

class AddNotesView(CreateView):
	model = Note
	template_name = 'addnote.html'
	fields = ['title','detail']

class EditNotesView(UpdateView):
	model = Note
	template_name = 'editnote.html'
	fields = ['title','detail']

class DeleteNoteView(DeleteView):
	model = Note
	template_name = 'deletenote.html'
	success_url = reverse_lazy('notes')

# Create your views here.
