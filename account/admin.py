from django.contrib import admin


from account.models import User, Employee, Restaurant, Menu

admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Restaurant)
admin.site.register(Menu)
