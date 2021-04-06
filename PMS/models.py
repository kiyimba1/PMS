from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MemberManager(BaseUserManager):
    def create_user(self, first_name, last_name, national_id_number, phone_number, district, email, date_of_birth, password=None):
        if not national_id_number:
            raise ValueError('Users must have a NIN')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            national_id_number=national_id_number,
            phone_number=phone_number,
            district=district,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            id_number=national_id_number
        )
        user.set_password(national_id_number)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, national_id_number, phone_number, district, date_of_birth, password=None):
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')
        # return self.create_user(email, password, **extra_fields)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            national_id_number=national_id_number,
            phone_number=phone_number,
            district=district,
            date_of_birth=date_of_birth,
            id_number=national_id_number,
        )
        user.set_password(password)
        user.is_admin = True
        # user.is_staff = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100, unique=True)
    national_id_number = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.CharField(
        max_length=100, unique=True, blank=True, null=True)
    district = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'national_id_number'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'phone_number', 'district', 'date_of_birth']

    objects = MemberManager()

    def __str__(self):
        return self.id_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
