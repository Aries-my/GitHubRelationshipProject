from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(users)
admin.site.register(follow_nodes)
admin.site.register(follow_edges)
admin.site.register(Commit_nodes)
admin.site.register(Collaborate_nodes)
