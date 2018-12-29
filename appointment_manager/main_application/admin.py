from django.contrib import admin

from .models import * 

admin.site.register(user)
admin.site.register(office)
admin.site.register(address)
admin.site.register(contact)
admin.site.register(appointmenet)
admin.site.register(rating)



# Register your models here.
