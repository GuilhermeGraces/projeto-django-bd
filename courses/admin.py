from django.contrib import admin

from courses.models import Course, Person 

admin.site.register(Person)
admin.site.register(Course)