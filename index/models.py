# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import DO_NOTHING


class Admin(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'admin'


class Album(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    broadcast = models.CharField(max_length=20)
    chapter_count = models.IntegerField()
    content = models.TextField()
    score = models.SmallIntegerField()
    publish_time = models.DateTimeField()
    img_src = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'album'


class Article(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    publish_time = models.DateField(auto_now_add=True)
    content = models.TextField()
    pics = models.ImageField(upload_to='article_pic')
    cate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'article'


class Pic(models.Model):
    pics = models.ImageField(upload_to='article_pic')
    article_id = models.ForeignKey(to=Article, on_delete=DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pic'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chapter(models.Model):
    title = models.CharField(max_length=20)
    size = models.DecimalField(max_digits=6, decimal_places=2)
    url = models.CharField(max_length=20)
    time_long = models.SmallIntegerField()
    album_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chapter'


class Count(models.Model):
    title = models.CharField(max_length=20)
    counts = models.IntegerField()
    last_time = models.DateTimeField()
    course_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'count'


class Course(models.Model):
    title = models.CharField(max_length=20)
    cate = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Rotation(models.Model):
    title = models.CharField(max_length=20)
    publish_time = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    img_url = models.ImageField(upload_to='pic')

    class Meta:
        managed = False
        db_table = 'rotation'


class User(models.Model):
    name = models.CharField(max_length=20)
    religions_name = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=40)
    status = models.IntegerField()
    img_src = models.ImageField(upload_to='userimg')
    regist_time = models.DateField(auto_now_add=True)
    details = models.TextField()
    address = models.CharField(max_length=40)
    email = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user'
