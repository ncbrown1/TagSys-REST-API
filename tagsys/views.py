from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework import viewsets
from tagsys.serializers import CheckSerializer, TagSerializer, DeviceSerializer, LocationSerializer
from tagsys.models import Check, Tag, Device, Location

class CheckViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows checks to be viewed or edited
	"""
	queryset = Check.objects.all().reverse()
	serializer_class = CheckSerializer

class TagViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows tags to be viewed or edited
	"""
	queryset = Tag.objects.all().reverse()
	serializer_class = TagSerializer

class DeviceViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows devices to be viewed or edited
	"""
	queryset = Device.objects.all().reverse()
	serializer_class = DeviceSerializer

class LocationViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows locations to be viewed or edited
	"""
	queryset = Location.objects.all().reverse()
	serializer_class = LocationSerializer

def index(request):
	return render_to_response('tagsys/index.html')

#@login_required(login_url="/api-auth/login/")
#def rounds(request):
#	context = RequestContext(request)
#	return render_to_response('tagsys/rounds.html')
