# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AppCheck(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_pk = models.IntegerField()
    time = models.DateTimeField()
    user = models.CharField(max_length=64)
    notes = models.CharField(max_length=256)
    status = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'app_check'

class AppDevice(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=64)
    characteristics = models.CharField(max_length=64)
    frequency = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'app_device'

class AppLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'app_location'

class AppTag(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_id = models.CharField(max_length=32)
    type_pk = models.IntegerField()
    location = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_user = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'app_tag'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
	return self.location

    class Meta:
        db_table = 'locations'

class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=64)
    characteristics = models.CharField(max_length=64)
    frequency = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
	return self.type

    class Meta:
        db_table = 'devices'

class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_id = models.CharField(max_length=32, blank=True)
    #type_id = models.IntegerField()
    type = models.ForeignKey('Device', related_name='+id')
    location = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    description = models.CharField(max_length=100)
    last_user = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
	return self.location + ' - ' + self.description

    class Meta:
        db_table = 'tags'

class Check(models.Model):
    id = models.IntegerField(primary_key=True)
    #tag_id = models.BigIntegerField()
    tag = models.ForeignKey('Tag', related_name='+id')
    time = models.DateTimeField()
    user = models.CharField(max_length=64)
    notes = models.CharField(max_length=256, blank=True)
    picture = models.TextField(blank=True)
    STATUS_CHOICES = (
	('good','Good'),
	('warning','Warning'),
	('broke','Bad'),
    )
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    class Meta:
        db_table = 'checks'
