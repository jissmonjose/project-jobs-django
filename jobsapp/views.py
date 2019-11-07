from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import AddJobs, ApplyJob
from .register import RegisterForm
from django.contrib import messages
from django.shortcuts import redirect


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


# registration - user
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Account Created for {username}")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'jobsapp/register.html', {'form': form})
