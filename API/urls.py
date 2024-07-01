"""
URL configuration for API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter

router1=DefaultRouter()
router2=DefaultRouter()


router1.register("employeeA",views.ViewSetEmployeeDetails,basename="employeeA")
router2.register("employeeB",views.ViewSetEmployeeData,basename="employeeB")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("employee/",views.MixinsEmployeeData.as_view()),
    path("employee/<int:pk>",views.MixinsEmployeeDetails.as_view()),
    path("employee_data/",views.GenericsEmployeeData.as_view()),
    path("employee_data/<int:pk>",views.GenericsEmployeeDetails.as_view()),
    
    path("api/m1",include(router1.urls)),
    path("api/m2",include(router2.urls)),

]
