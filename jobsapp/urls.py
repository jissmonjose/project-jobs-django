from .views import JobsListing, JobsDetail, JobsApply, register_user
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

# urlpatterns
urlpatterns = [
    path('', JobsListing.as_view(), name='list_of_jobs'),
    path('jobs/<int:pk>', JobsDetail.as_view(), name='details_of_job'),
    path('jobs/apply/<int:pk>', JobsApply.as_view(), name='apply_to_job'),
    path('register/', register_user, name='register'),
    path('login/', LoginView.as_view(template_name='jobsapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='jobsapp/logout.html'), name='logout'),
]
