from django.urls import path
from contacts import views

app_name='contacts'
urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),

    #CRUD Contacts
    path('contact/<int:id>/detail', views.contact, name="contact"),
    # path('contacts/<int:id>/update', views.update_contact, name="update_contact"),
    # path('contacts/<int:id>/delete', views.delete_contact, name="detele_contact"),
    path('contact/create', views.create, name="create"),
]