from django.contrib import admin

from .models import Add_Food, employe_signup, Order, resturent_signup, User_signup

# Register your models here.
admin.site.register(User_signup)
admin.site.register(resturent_signup)
admin.site.register(employe_signup)
admin.site.register(Add_Food)
admin.site.register(Order)