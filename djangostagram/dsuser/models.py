from django.db import models

# Create your models here.


class Dsuser(models.Model):
    user_id = models.CharField(max_length=50, verbose_name='아이디')
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록일')

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'dsuser'
        managed = True
        verbose_name = '사용자'
        verbose_name_plural = '사용자s'