from django.db import models
from django.contrib.postgres.fields import ArrayField

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=16)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=35)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Foodavailability(models.Model):
    food_availability_id = models.AutoField(primary_key=True)
    avail_days = ArrayField(models.BooleanField(), size=7, blank=True) 
    avail_times = ArrayField(models.BooleanField(), size=3, blank=True)
    food = models.ForeignKey('Fooditems', models.DO_NOTHING)
    location = models.ForeignKey('Locations', models.DO_NOTHING)
    

    class Meta:
        managed = True
        db_table = 'foodavailability'
        #unique_together = (('food', 'location'),)


class Fooditems(models.Model):
    food_id = models.CharField(primary_key=True, max_length=20)
    food_name = models.CharField(max_length=60, blank=False)
    food_description = models.CharField(max_length=400, blank=True)
    avg_rating = models.IntegerField(null=True)

    class Meta:
        managed = True
        db_table = 'fooditems'


class Locations(models.Model):
    location_id = models.CharField(primary_key=True, max_length=21)
    location_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    location_pic = models.BinaryField(blank=True)
    opening_hours = ArrayField(models.TimeField(), size=7)
    closing_hours = ArrayField(models.TimeField(), size=7)

    class Meta:
        managed = True
        db_table = 'locations'

class Ratings(models.Model):
    rating_value = models.IntegerField()
    description = models.CharField(max_length=500, blank=True, null=True)
    user = models.OneToOneField('AuthUser', models.DO_NOTHING, primary_key=True)
    food = models.ForeignKey(Fooditems, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'ratings'
        unique_together = (('user', 'food'),)