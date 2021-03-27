from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, full_name, dept_sec, designation, contact_no, is_active=True, is_staff=False,
                    is_admin=False, password=None):
        if not username:
            raise ValueError("Users must have a Username")
        if not email:
            raise ValueError('Users must have an Email Address')
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
            username=username,
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

    def create_staffuser(self, username, email, full_name, dept_sec, designation, contact_no, password):
        user = self.create_user(
            username,
            email,
            full_name,
            dept_sec,
            designation,
            contact_no,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, full_name, dept_sec, designation, contact_no, password):
        user = self.create_user(
            username,
            email,
            full_name,
            dept_sec,
            designation,
            contact_no,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# def get_profile_image_filepath(self):
#     return f'profile_images/{self.pk}/{"profile_image.png"}'
#
#
# def get_default_profile_image():
#     return "accounts/images/defaultuser.png"


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='Username', max_length=100, blank=True, null=True, unique=True)
    email = models.EmailField(verbose_name='Email Address', max_length=100, unique=True, )
    full_name = models.CharField(verbose_name='Full Name', max_length=150, blank=True, null=True)
    dept_sec = models.CharField(verbose_name='Department or Section', max_length=100, blank=True, null=True)
    designation = models.CharField(verbose_name='Designation', max_length=100, blank=True, null=True)
    contact_no = models.CharField(verbose_name='Contact Number', max_length=11, blank=True, null=True, unique=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined..', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Logged in', auto_now=True)
    profile_image = models.ImageField(max_length=255, null=True, blank=True, default='defaultuser.png',
                                      upload_to='')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'dept_sec', 'designation', 'contact_no']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % self.pk

    def get_email(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_username(self):
        return self.username

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


class user_type(models.Model):
    is_teacher = models.BooleanField(default=False)
    is_chairman = models.BooleanField(default=False)
    is_vadmin = models.BooleanField(default=False)
    is_vsubadmin = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_teacher:
            return User.get_email(self.user) + " - is_teacher"
        elif self.is_chairman:
            return User.get_email(self.user) + " - is_chairman"
        elif self.is_vadmin:
            return User.get_email(self.user) + " - is_vadmin"
        elif self.is_vsubadmin:
            return User.get_email(self.user) + " - is_vsubadmin"
        else:
            return User.get_email(self.user) + " - is_accountant"
