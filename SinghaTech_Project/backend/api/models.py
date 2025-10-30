from django.db import models
import datetime
from django.core.validators  import MinValueValidator, MaxValueValidator

class Treatment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class TreatOption(models.Model):
    treatment = models.ForeignKey(Treatment,on_delete=models.CASCADE,related_name='options')
    country = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    items = models.JSONField()

    def __str__(self):
        return f"{self.treatment.name} - {self.country}"
    

class DoctorName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DoctorInfo(models.Model):
    name = models.ForeignKey(DoctorName, related_name='doctorDetail', on_delete=models.CASCADE )
    image = models.ImageField(upload_to= 'doctors/')
    specialization = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)

class DoctorEducation(models.Model):
    name = models.ForeignKey(DoctorName, on_delete=models.CASCADE, related_name='doctorEducation')
    fromyear = models.PositiveIntegerField()
    toyear = models.PositiveIntegerField()
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    Discription = models.TextField()

class DoctorExperience(models.Model):
    name = models.ForeignKey(DoctorName, on_delete=models.CASCADE, related_name='doctorExperience')

    currentYear = datetime.date.today().year
    fromyear = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(currentYear)
        ]
    )

    toyear = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(currentYear)
        ]
    )

    position = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    discription = models.TextField()


class DoctorCertificate(models.Model):
    name = models.ForeignKey(DoctorName, on_delete=models.CASCADE, related_name='doctorCertificate')

    certificate = models.JSONField()

class DoctorLanguage(models.Model):
    name = models.ForeignKey(DoctorName, on_delete=models.CASCADE, related_name='doctorLanguage')

    languages = models.JSONField()

class DoctorExperties(models.Model):
    name = models.ForeignKey(DoctorName, on_delete=models.CASCADE, related_name='doctorExperties')

    experties = models.JSONField()

class DoctorContact(models.Model):
    name = models.ForeignKey(DoctorName, on_delete=models.CASCADE, related_name='doctorContact')

    phone = models.PositiveIntegerField()
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)