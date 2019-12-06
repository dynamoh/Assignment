from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None,student=True,manager=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.student = student
        user.manager = manager
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password,student=True,manager=False):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.student = False
        user.manager = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,student=True,manager=False):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.student = False
        user.manager = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    student =models.BooleanField(default=True)
    manager =models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['student','manager'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_student(self):
        "Is the user a student?"
        return self.student

    @property
    def is_manager(self):
        "Is the user a manager?"
        return self.manager

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    objects = UserManager()


class Constants:

    PREFERENCE = (
        ('Web Dev', 'Web Dev'),
        ('Mobile app dev', 'Mobile app dev'),
        ('UI/UX', 'UI/UX')
    )

    SKILLS = (
        ('Node','Node'),
        ('Flutter','Flutter'),
        ('Django','Django'),
        ('Swift','Swift'),
        ('Adobe XD','Adobe XD')
    )


class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='projectapp/images',default="")
    year_of_study = models.IntegerField(default=1)
    preference = models.CharField(max_length=50,choices=Constants.PREFERENCE)
    skills = models.CharField(max_length=50,choices=Constants.SKILLS)
    projects_count = models.IntegerField(default=0)


    def __str__(self):
        return self.name
