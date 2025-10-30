from django.contrib import admin

from .models import Treatment, TreatOption, DoctorInfo , DoctorName , DoctorEducation , DoctorExperience, DoctorExperties, DoctorContact, DoctorCertificate,DoctorLanguage

class TreatmentOptionInline(admin.StackedInline):
    model = TreatOption
    extra = 3

@admin.register(Treatment)

class TreatmentInline(admin.ModelAdmin):
    inlines = [TreatmentOptionInline]


class DoctorInfoInline(admin.StackedInline):
    model = DoctorInfo
    extra = 1

class DoctorEducationInline(admin.StackedInline):
    model = DoctorEducation
    extra = 1

class DoctorExperienceInline(admin.StackedInline):
    model = DoctorExperience
    extra = 1

class DoctorExpertiesInline(admin.StackedInline):
    model = DoctorExperties
    extra = 1

class DoctorCertificateInline(admin.StackedInline):
    model = DoctorCertificate
    extra = 1

class DoctorContactInline(admin.StackedInline):
    model = DoctorContact
    extra = 1

class DoctorLanguageInline(admin.StackedInline):
    model = DoctorLanguage
    extra = 1


@admin.register(DoctorName)
class DoctorInline(admin.ModelAdmin):
    inlines = [DoctorInfoInline,
                DoctorEducationInline,
                DoctorExperienceInline,
                DoctorExpertiesInline,
                DoctorCertificateInline,
                DoctorContactInline,
                DoctorLanguageInline]


