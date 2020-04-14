from django.contrib import admin


from index.models import *

admin.site.register(UserInfo)
admin.site.register(Permission)
admin.site.register(Role)
