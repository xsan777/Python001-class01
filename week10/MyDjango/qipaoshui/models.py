from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Qipaoshui(models.Model):
    id = models.BigAutoField(primary_key = True)
    date = models.CharField(max_length = 30)
    n_star = models.IntegerField()
    sum_i = models.IntegerField()
    link = models.CharField(max_length=40)
    estimate = models.CharField(max_length=200)
    sentiment = models.DecimalField(max_digits=11,decimal_places = 10)

 
 
# class UserProfile(AbstractUser):
#     nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
#     birthday = models.DateField(verbose_name="生日", blank=True, null=True)
#     mobile = models.CharField(max_length=11, verbose_name="手机", default="")
#     address = models.CharField(max_length=50, verbose_name="地址", default="")
#     image = models.ImageField(verbose_name="用户头像", upload_to="users/%Y/%m", default="")
 
#     class Meta:
#         verbose_name = "用户信息"
#         verbose_name_plural = verbose_name
 
#     def __str__(self):
#         return self.username
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class MyBackend(ModelBackend):
    # def authenticate(self, request, username=None, password=None, **kwargs):
    #     User = get_user_model()
    #     try:
    #         user = User.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
    #         if user:
    #             return user
    #     except Exception as e:
    #         return None
    def authenticate(self, request, username=None, password=None, phone=None, email=None):
        User = get_user_model()
        if username and password:
            # user = super(MyBackend, self).authenticate(request, username=username, password=password)
            user = super().authenticate(request, username=username, password=password)
            print('=====----账号-----=====')
            if user:
                return user
        elif email and password:
                print('=====----邮箱-----=====')
                user = User.objects.filter(Q(email=email )).first()
                # print(user)
                if user:
                    print('=====----密码-----=====')
                    if user.check_password(password) and self.user_can_authenticate(user):
                        return user
                    else:
                        print('======', user.check_password(password))