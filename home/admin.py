from django.contrib import admin
from .models import Articles ,Published , Generalpage,Propheticpage,Spiritualpage,Socialpage ,Featured, Count 
admin.site.register(Published)
admin.site.register(Count)
admin.site.register(Articles)
admin.site.register(Generalpage)
admin.site.register(Propheticpage)
admin.site.register(Spiritualpage)
admin.site.register(Socialpage)
admin.site.register(Featured)
