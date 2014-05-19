from django.contrib import admin
from tagsys.models import Check, Tag, Device, Location

class CheckAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields': ['notes', 'status']}),
		('More Information',	{'fields': ['time', 'user', 'tag']}),
	]

	list_display = ('notes', 'tag','time', 'user', 'status')
	list_filter = ['time', 'user', 'tag', 'status']

class TagAdmin(admin.ModelAdmin):
	fields = ['location','description','created','modified','last_user','tag_id','type']
	
	list_display = ('description','location','created','modified','last_user','id','tag_id')
	list_filter = ['location']

class DeviceAdmin(admin.ModelAdmin):
	fields = ['type','characteristics','frequency']
	
	list_display = ('type','characteristics','frequency')

class LocationAdmin(admin.ModelAdmin):
	fields = ['location']

admin.site.register(Check, CheckAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Location, LocationAdmin)
