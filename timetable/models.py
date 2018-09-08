from django.db import models


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=10)
    weather = models.CharField(max_length=10)
    sheet_id = models.IntegerField()
    place = models.CharField(max_length=30)
    t1000 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1015 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1030 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1045 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1100 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1115 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1130 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1145 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1200 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1215 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1230 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1245 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1300 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1315 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1330 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1345 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1400 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1415 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1430 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1445 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1500 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1515 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1530 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1545 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1600 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1615 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1630 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1645 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1700 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1715 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1730 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1745 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1800 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1815 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1830 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1845 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1900 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1915 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1930 = models.CharField(max_length=100, null=True, blank=True, default=None)
    t1945 = models.CharField(max_length=100, null=True, blank=True, default=None)

    class Meta:
        db_table = 'timetables'
        unique_together = ('day', 'weather', 'place')

    def __str__(self):
        return '{}({}{})'.format(self.place, self.day, self.weather)