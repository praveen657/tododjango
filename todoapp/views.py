from django.shortcuts import render
from .models import Item
# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView,DeleteView
from django.urls import reverse_lazy 

class HomePageView(ListView):
	model = Item
	template_name = 'todoapp/home.html'

class TaskCreateView(CreateView): # new
	model = Item
	template_name = 'todoapp/createtask.html'
	fields = ["task"]
	success_url = reverse_lazy('home')

class TaskDeleteView(DeleteView): # new
	model = Item
	template_name = 'todoapp/delete.html'
	success_url = reverse_lazy('home')