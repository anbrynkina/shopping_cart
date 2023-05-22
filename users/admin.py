from django.contrib import admin
from users.models import User
# Register your models here.

# adding this for User to appear in admin panel
admin.site.register(User)