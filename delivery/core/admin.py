from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
 
from .models import User, Region, City, District, Position, Status, TBCenter, Consilium, DocPack
 
admin.site.register(User, UserAdmin)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Position)
admin.site.register(Status)
admin.site.register(TBCenter)
admin.site.register(Consilium)
admin.site.register(DocPack)
