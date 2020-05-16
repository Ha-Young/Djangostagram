from django.db import models

# Create your models here.


class Post(models.Model):
    writer = models.ForeignKey("dsuser.Dsuser", verbose_name="작성자", on_delete=models.CASCADE)
    img_url = models.CharField(verbose_name='이미지 주소', max_length=512)
    description = models.TextField(verbose_name='내용')
    tags = models.ManyToManyField("tag.Tag", verbose_name="태그")
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    def __str__(self):
        return self.description

    class Meta:
        db_table = '글'
        managed = True
        verbose_name = '글'
        verbose_name_plural = '글s'