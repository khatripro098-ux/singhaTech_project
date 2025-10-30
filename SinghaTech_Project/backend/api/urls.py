from django.urls import path, include
from .views import TreatmentView,DoctorView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'treatment',TreatmentView)
router.register(r'doctor', DoctorView)

urlpatterns = [
    path('', include(router.urls)),
] 



