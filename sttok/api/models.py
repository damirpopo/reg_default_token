from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("вы не вели маил")
        if not username:
            raise ValueError("вы не вели логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='api_users',
        related_query_name='api_user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='api_users',
        related_query_name='api_user',
    )



class Author(models.Model):
    authors = models.CharField(max_length=50)

    def __str__(self):
        return self.authors

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    new = models.BooleanField(default=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    productList = models.ManyToManyField(Product)


class Order(models.Model):
    numbersrder = models.IntegerField()
    allprice = models.IntegerField()

