from django.db import models

# Create your models here.
# 测试发布表
class Event(models.Model):
    name = models.CharField(max_length=100)             # 发布标题
    limit = models.IntegerField()                       # 参加人数
    status = models.BooleanField()                      # 状态
    address = models.CharField(max_length=200)          # 地址
    start_time = models.DateTimeField('events time')    # 发布时间
    create_time = models.DateTimeField(auto_now=True)   # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name

# 参与人员表
class Member(models.Model):
    # 创建外键
    event = models.ForeignKey('Event','on_delete=models.CASCADE,')    # 关联发布表ID
    realname = models.CharField(max_length=64)                        # 姓名
    phone = models.CharField(max_length=16)                           # 手机号码
    email = models.EmailField()                                       # 邮箱
    sign = models.BooleanField()                                      # 签到状态
    create_time = models.DateTimeField(auto_now=True)                 # 创建时间（自动获取当前时间）

# 内部类，定义模型类的行为特征
class Meta:
    # 设置2个字段为联合主键
    unique_together = ("event", "phone")

def __str__(self):
    return self.realname
    
