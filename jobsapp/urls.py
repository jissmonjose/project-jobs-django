from .views import JobsListing, JobsDetail, JobsApply
from django.urls import path

# urlpatterns
urlpatterns = [
    path('', JobsListing.as_view(), name='list_of_jobs'),
    path('jobs/<int:pk>', JobsDetail.as_view(), name='details_of_job'),
    path('jobs/apply/<int:pk>', JobsApply.as_view(), name='apply_to_job'),
]
