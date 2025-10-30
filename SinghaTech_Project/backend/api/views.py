from rest_framework import viewsets

from .models import Treatment, DoctorName
from .serializer import TreatmentSerialize,DoctorSerializer

class TreatmentView(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerialize

class DoctorView(viewsets.ModelViewSet):
    queryset = DoctorName.objects.all().prefetch_related('doctorDetail', 'doctorEducation','doctorExperience','doctorExperties','doctorCertificate', 'doctorLanguage', 'doctorContact')
    serializer_class = DoctorSerializer