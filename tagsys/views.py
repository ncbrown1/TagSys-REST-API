from django.shortcuts import render
from rest_framework import viewsets
from tagsys.serializers import CheckSerializer, TagSerializer, DeviceSerializer, LocationSerializer
from tagsys.models import Check, Tag, Device, Location

class CheckViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows checks to be viewed or edited
	"""
	queryset = Check.objects.all()
	serializer_class = CheckSerializer

class TagViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows tags to be viewed or edited
	"""
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class DeviceViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows devices to be viewed or edited
	"""
	queryset = Device.objects.all()
	serializer_class = DeviceSerializer

class LocationViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows locations to be viewed or edited
	"""
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
