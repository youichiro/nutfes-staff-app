from django.db import models
from account.models import User, Department


class Shift(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    day = models.CharField(max_length=10)
    weather = models.CharField(max_length=10)
    shift_id = models.IntegerField()
    t0600 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t0630 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t0700 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t0730 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t0800 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t0830 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t0900 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t0930 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1000 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1030 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1100 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1130 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1200 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1230 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1300 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1330 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1400 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1430 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1500 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1530 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1600 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1630 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1700 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1730 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1800 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1830 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1900 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1930 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t2000 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t2030 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t2100 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t2130 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t2200 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t2230 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t2300 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t2330 = models.CharField(max_length=100, null=True, blank=True, default=None)

    class Meta:
        db_table = 'shifts'
        unique_together = ('user', 'day', 'weather')

    def __str__(self):
        return '{}({}{})'.format(self.user, self.day, self.weather)

    def get_user(self):
        return User.objects.filter(name=self.user).first() or None

    def get_department(self):
        return Department.objects.filter(short_name=self.department).first() or None
