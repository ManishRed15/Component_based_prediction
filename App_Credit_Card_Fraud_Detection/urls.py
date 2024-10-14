from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('base/',views.base,name='base'), 
    path('View_Customer/',views.View_Customer,name='View_Customer'), 
    path('Admin_login/',views.Admin_login,name='Admin_Login'), 
    path('Fraudulent_Customers/',views.Fraudulent_Customers,name='Fraudulent_Customers'),
    path('Generate_Payment_link/',views.Generate_Payment_link,name='Generate_Payment_link'),
    path('verify/',views.verify,name='verify'),
    path('Logout/',views.Logout,name='Logout'),
    path('User_Login/',views.User_Login,name='User_Login'), 
    path('User_Registeration/',views.User_Registeration,name='User_Registeration'),
    path('Create_Payment_Link/',views.Create_Payment_Link,name='Create_Payment_Link'),
    path('View_Details/<str:user_name>',views.View_Details,name='View_Details'),
    path('Update_status/<int:id>',views.Update_status,name='Update_status'),
    path('Flag_update/',views.Flag_update,name='Flag_update'),
    #url(r'^View_Details/(?P<user_name>\w+)/$', views.View_Details, name='View_Details'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


