from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login_view',views.login_view,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('home',views.home,name='home'),
    path('registration_tailwebs',views.registration_tailwebs,name='registration_tailwebs'),
    path('success_view',views.success_view,name='success_view'),
    path('details_view',views.details_view,name='details_view'),
    path("edit_student/<int:student_id>/", views.edit_student, name="edit_student"),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student')

]