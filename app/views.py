from django.shortcuts import render
from .serializers import EmpSerializer
from .models import Employee
from rest_framework import mixins,generics,viewsets
# Create your views here.


# Using Mixins:----------------------------

class MixinsEmployeeData(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializer
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)
    
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
class MixinsEmployeeDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializer
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,**kwargs)


# Using Generics:-----------------

class GenericsEmployeeData(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializer
    
class GenericsEmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializer
    
# Using ViewSets:-------------

class ViewSetEmployeeDetails(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializer
    
class ViewSetEmployeeData(viewsets.ReadOnlyModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializer           