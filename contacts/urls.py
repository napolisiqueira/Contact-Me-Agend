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
    path('contact/<int:contact_id>/update/', views.update, name="update"),
    path('contact/<int:contact_id>/delete/', views.delete, name="delete"),
    
    
    path('user/create', views.register, name="register"),
    path('user/login', views.login_view, name="login"),
    path('user/logout', views.logout_view, name="logout"),
    path('user/update', views.user_update, name='user_update'),
    
]