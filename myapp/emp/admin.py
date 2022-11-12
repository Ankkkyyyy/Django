from django.contrib import admin

from .models import Emp,Testimonial

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
     # tuple hai yeahsbh
    list_display=('name','working','emp_id','phone') # for showing the list in tabular way
    list_editable = ('working','emp_id') # for editing the fields

    #for searching data with help of name..
    search_fields=('name',) 

    #for filtering data lyk
    list_filter=('working',)

    
   


admin.site.register(Emp,EmpAdmin)

admin.site.register(Testimonial)