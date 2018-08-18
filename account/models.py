from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, student_id, name, grade, department, phone_number, password):
        if not student_id:
            raise ValueError('学籍番号は必須です.')
        user = self.model(student_id=student_id, name=name, grade=grade,
                          department=department, phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, **fields):
        return self._create_user(*fields)

    def create_superuser(self, **fields):
        return self._create_user(*fields)


class User(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=7, unique=True,
                                  help_text='学生番号を入力してください. (ex. s163127)')
    name = models.CharField(max_length=100, help_text='名前を入力してください.')
    grade = models.CharField(max_length=2, help_text='学年を選択してください.')
    department = models.ManyToManyField(Department, help_text='所属している局・部門を選択してください.')
    phone_number = models.CharField(max_length=13, blank=True, help_text='電話番号を入力してください.')

    objects = UserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name']

