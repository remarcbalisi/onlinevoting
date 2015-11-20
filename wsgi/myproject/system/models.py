from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from time import time
from django.utils import timezone

from django.contrib.auth.models import BaseUserManager

# CUSTOM USER AUTH
###############################################################################

class UserManager(BaseUserManager):

    def create_user(self, id_number, password, **kwargs):
        user = self.model(
            id_number=id_number,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_number, password, **kwargs):
        user = self.model(
            id_number=id_number,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_admin=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return UserManager

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'id_number'

    id_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    contact_number = models.CharField(max_length=30, null=True, blank=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def get_full_name(self):
        return self.id_number
    def get_short_name(self):
        return self.id_number

    objects = UserManager()

###############################################################################
###############################################################################
###############################################################################
###############################################################################

class Vote(models.Model):
    candidate_id = models.ForeignKey('Candidate', blank=True, null=True)
    election_id = models.ForeignKey('Election', blank=True, null=True)

class Candidate(models.Model):
    firstname = models.CharField(max_length=45, null=True)
    middle_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45, null=True)
    position_id = models.ForeignKey('Position', blank=True, null=True)
    election_id = models.ForeignKey('Election', blank=True, null=True)
    college_id = models.ForeignKey('College', blank=True, null=True)
    party_id = models.ForeignKey('Party', blank=True, null=True)

    def __str__(self):
        return "%s %s %s" % (firstname, middle_name, last_name)

class Party(models.Model):
    party_name = models.CharField(max_length=30, null=True, unique=True)
    election_id = models.ForeignKey('Election', blank=True, null=True)

    def __str__(self):
        return self.party_name

class Position(models.Model):
    position_name = models.CharField(max_length=20, null=True, unique=True)

    def __str__(self):
        return self.position_name

class Election(models.Model):
    year = models.IntegerField(null=True, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % (self.year)

    def election_init(self):
        self.is_active = True

    def election_stop(self):
        self.is_active = False

class College(models.Model):
    college_name = models.CharField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.college_name
