from cProfile import Profile
from django.contrib import admin
from django.contrib.auth.models import User
from .models import StaffProfile,StudentProfile,TISNStudentProfile
# Register your models here.


# class ProfileAdmin(admin.StackedInline):
#     model = Profile

# # this class define which department columns will be shown in the department admin web site.
# class UsersAdmin(admin.ModelAdmin):
#     inlines = [ProfileAdmin]
#     # a list of displayed columns name.
#     list_display = ['pf_number','department']
#     class Meta:
#        model = User
# admin.site.register(User, UsersAdmin)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ['pf_number','names','position','department','directorate','status','images']

    class Meta:
        model = StaffProfile
        

admin.site.register(StaffProfile, StaffProfileAdmin)

class TISNStudentProfileAdmin(admin.ModelAdmin):
    list_display = ['admission_number','names','course','start_date','end_date','status','images']

    class Meta:
        model = TISNStudentProfile
admin.site.register(TISNStudentProfile, TISNStudentProfileAdmin)

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['trainee_number','names','department','directorate','start_date','end_date','status','images']

    class Meta:
        model = StudentProfile
admin.site.register(StudentProfile, StudentProfileAdmin)