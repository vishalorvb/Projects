from django.urls import include, path
from BRMapp import views
from django.conf.urls import url
urlpatterns=[
    url('view-book',views.viewBooks),
    url('edit-book',views.editBook),
    url('delete-book',views.deleteBook),
    url('search-book',views.searchBook),
    url('new-book', views.newBook),
    url('add', views.add),
    url('search', views.search),
    url('edit', views.edit),
    url('login', views.userLogin),
    url('logout', views.userLogout),
   
]