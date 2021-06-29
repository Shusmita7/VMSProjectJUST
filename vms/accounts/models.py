from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, codename, email, full_name, dept_sec, designation, contact_no, is_active=True, is_staff=False,
                    is_admin=False, is_superuser=False, password=None):
        if not email:
            raise ValueError('Users must have an Email Address')
        if not codename:
            raise ValueError("Users must have a Username")
        if not password:
            raise ValueError('Users must have a Password')
        if not full_name:
            raise ValueError('Users must have a Full Name')
        if not designation:
            raise ValueError("Users must have a Designation")
        if not dept_sec:
            raise ValueError("Users must have a Department or Section")
        if not contact_no:
            raise ValueError("Users must have a Contact Number")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            codename=codename,
            dept_sec=dept_sec,
            designation=designation,
            contact_no=contact_no,
        )

        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, codename, email, full_name, dept_sec, designation, contact_no, password):
        user = self.create_user(
            email=self.normalize_email(email),
            codename=codename,
            full_name=full_name,
            dept_sec=dept_sec,
            designation=designation,
            contact_no=contact_no,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, codename, email, full_name, dept_sec, designation, contact_no, password):
        user = self.create_user(
            email=self.normalize_email(email),
            codename=codename,
            full_name=full_name,
            dept_sec=dept_sec,
            designation=designation,
            contact_no=contact_no,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email Address', max_length=100, unique=True, blank=False)
    codename = models.CharField(verbose_name='Username', max_length=100, blank=False, null=True, unique=True)
    full_name = models.CharField(verbose_name='Full Name', max_length=150, blank=False, null=True)
    dept_sec = models.CharField(verbose_name='Department or Section', max_length=100, blank=False, null=True)
    designation = models.CharField(verbose_name='Designation', max_length=100, blank=False, null=True)
    contact_no = models.CharField(verbose_name='Contact Number', max_length=11, blank=False, null=True, unique=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined..', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Logged in', auto_now=True)
    profile_image = models.ImageField(max_length=255, null=True, blank=True, default='defaultuser.png',
                                      upload_to='')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['codename', 'full_name', 'dept_sec', 'designation', 'contact_no']

    objects = UserManager()

    def get_email(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_codename(self):
        return self.codename

    def get_dept_sec(self):
        return self.dept_sec

    def get_designation(self):
        return self.designation

    def get_contact_no(self):
        return self.contact_no

    def __str__(self):
        return self.email

    # def get_profile_image_filename(self):
    #     return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin

    @property
    def is_active(self):
        """Is the user active?"""
        return self.active

    @property
    def is_superuser(self):
        """Is the user a superuser?"""
        return self.superuser
