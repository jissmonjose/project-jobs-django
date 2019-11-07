from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import AddJobs, ApplyJob


# Create your views here.


class JobsListing(ListView):
    model = AddJobs
    context_object_name = 'jobs'


class JobsDetail(DetailView):
    model = AddJobs
    context_object_name = 'jobs_detail'


class JobsApply(CreateView):
    model = ApplyJob
    fields = ('name', 'email', 'phone')


