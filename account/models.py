from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'departments'
        ordering = ['id']

    def __str__(self):
        return self.short_name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, student_id, name, password, **extra_fields):
        if not student_id:
            raise ValueError('学籍番号は必須です.')
        user = self.model(student_id=student_id, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, student_id, name, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(student_id, name, *extra_fields)

    def create_superuser(self, student_id, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(student_id, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=9, unique=True,
                                  help_text='学生番号を入力してください. (ex. s16312786)')
    name = models.CharField(max_length=100, help_text='名前を入力してください.')
    grade = models.CharField(max_length=2, help_text='学年を選択してください.')
    department = models.ManyToManyField(Department, help_text='所属している局・部門を選択してください.')
    phone_number = models.CharField(max_length=13, blank=True, help_text='電話番号を入力してください.')

    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='ユーザが管理サイトにアクセスできるかを指定する.',
    )

    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='有効なユーザとして扱うかを指定する.',
    )

    objects = UserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name
