from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그명")
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="생성일자")


    class Meta:
        db_table="태그"
        verbose_name = "태그"
        verbose_name_plural = "태그s"

    def __str__(self):
        return self.name