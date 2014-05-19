from tagsys.models import Check, Tag, Device, Location
from rest_framework import serializers

class CheckSerializer(serializers.ModelSerializer):
	class Meta:
		model = Check
		fields = ('id','notes','status','tag','time','user')

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id','tag_id','location','description','created','modified','last_user','type')

class DeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Device
		fields = ('id','type','characteristics','frequency')

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('id','location')
