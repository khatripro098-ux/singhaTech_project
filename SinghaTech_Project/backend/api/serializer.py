from .models import Treatment,TreatOption, DoctorInfo, DoctorName , DoctorEducation, DoctorExperience,DoctorExperties, DoctorContact, DoctorCertificate, DoctorLanguage

from rest_framework import serializers

class TreatoptionSerialize(serializers.ModelSerializer):
    class Meta : 
        model = TreatOption
        fields = ['country','price','items']

class TreatmentSerialize(serializers.ModelSerializer):
    options = TreatoptionSerialize(many=True)
    class Meta :
        model = Treatment
        fields = ['id', 'name', 'options']


class DoctorSerializerinfo(serializers.ModelSerializer):
    class Meta:
        model = DoctorInfo
        fields = ['image','specialization','experience','hospital']


class DoctorEducationserializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorEducation
        fields = ['fromyear','toyear','course','university','Discription']

class DoctorExperienceSerializer(serializers.ModelSerializer):
    class Meta :
        model = DoctorExperience
        fields = ['fromyear','toyear','position','institute','discription']

class DoctorExpertiesSerializer(serializers.ModelSerializer):
    class Meta :
        model = DoctorExperties
        fields = ['experties']

class DoctorContactSerializer (serializers.ModelSerializer):
    class Meta :
        model = DoctorContact

        fields = ['phone','email','location']

class DoctorCertificateSerializer(serializers.ModelSerializer):
    class Meta :
        model = DoctorCertificate

        fields = ['certificate']

class DoctorLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorLanguage
        fields = ['languages']


class DoctorSerializer(serializers.ModelSerializer):
    doctorDetail = DoctorSerializerinfo(many=True,read_only =True)
    doctorEducation = DoctorEducationserializer(many=True, read_only = True)
    doctorExperience = DoctorExperienceSerializer(many=True, read_only=True)
    doctorExperties = DoctorExpertiesSerializer(many=True, read_only=True)
    doctorCertificate = DoctorCertificateSerializer(many=True, read_only=True)
    doctorContact = DoctorContactSerializer(many=True,read_only= True)
    doctorLanguage = DoctorLanguageSerializer(many=True, read_only=True)


    class Meta:
        model = DoctorName
        fields = ['id','name','doctorDetail','doctorEducation','doctorExperience','doctorExperties','doctorCertificate','doctorContact','doctorLanguage']