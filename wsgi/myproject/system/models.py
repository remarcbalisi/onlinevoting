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
    is_voted = models.BooleanField(default=False)

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
    candidate_id = models.ManyToManyField('Candidate')
    election_id = models.ForeignKey('Election', blank=True, null=True)
    user_id = models.ForeignKey('User', blank=True, null=True)
    date_time_voted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.user_id, self.election_id)

    def vote_init(self):
        self.date_time_voted = timezone.now()

        # expiry = models.DateTimeField(default=datetime.now + timedelta(days=30))

class Candidate(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    position_id = models.ForeignKey('Position', blank=True, null=True)
    election_id = models.ForeignKey('Election', blank=True, null=True)
    college_id = models.ForeignKey('College', blank=True, null=True)
    party_id = models.ForeignKey('Party', blank=True, null=True)


    def __str__(self):
        return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)

class Party(models.Model):

    party_name = models.CharField(max_length=50, null=True, unique=True)
    election_id = models.ForeignKey('Election', blank=True, null=True)

    def __str__(self):
        return self.party_name

class Position(models.Model):
    position_name = models.CharField(max_length=20, unique=True)
    slot = models.IntegerField()

    def __str__(self):
        return self.position_name

class Election(models.Model):
    year = models.IntegerField(unique=True)
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

class Bulletin(models.Model):
    bulletin_info = models.CharField(max_length=300, null=True, unique=True)

    def __str__(self):
        return self.bulletin_info

class Tally(models.Model):
    vote_count = models.IntegerField()
    election_id = models.ForeignKey(Election, null=True, blank=True)
    user_id = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return "%s count: %s" %(self.user_id, self.vote_count)