from django.conf.urls import url
from . import views


urlpatterns = [

    url('api/GetAllEmployers', views.employer_list),
    url('api/Employer/(?P<pk>[0-9]+)$', views.employer_detail),
    url('api/DeleteEmployer/(?P<pk>[0-9]+)$', views.employer_delete),
    url('api/UpdateEmployer/(?P<pk>[0-9]+)$', views.employer_update),
    url('api/AllEmployersWithContact', views.employerWithContact_list),
    url('api/CreateEmployer', views.employer_create),
    url('api/WriteToExcel', views.write_to_excel),

]