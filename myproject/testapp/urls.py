from django.urls import include, path
from testapp import views
from django.conf.urls import url
urlpatterns=[
    url('show',views.show),
    url('views',views.view)

]