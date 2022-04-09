from django.shortcuts import render
from .models import Item
# Create your views here.
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView
from django.urls import reverse_lazy 

class HomePageView(ListView):
	model = Item
	template_name = 'todoapp/home.html'

class TaskCreateView(CreateView): # new
	model = Item
	template_name = 'todoapp/createtask.html'
	fields = ["task","task_description"]
	success_url = reverse_lazy('home')

class TaskDeleteView(DeleteView): # new
	model = Item
	template_name = 'todoapp/delete.html'
	success_url = reverse_lazy('home')

class TaskSearchView(ListView):
    model = Item
    template_name = 'todoapp/home.html'
    queryset = Item.objects.all()
   
    def get_queryset(self):
        result = self.request.GET.get('search_term')
        return Item.objects.filter(task__icontains=result)

class TaskDetailView(DetailView):
	model = Item 
	template_name = 'todoapp/taskdescription.html'
