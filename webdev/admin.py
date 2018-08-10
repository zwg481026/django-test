from django.contrib import admin
from webdev.models import Event,Member

# Register your models here.
# list_display:定义在列表中显示哪些字段 
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    search_fields = ['name'] # 搜索栏
    list_filter = ['status'] # 过滤器

class MemberAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname','phone'] # 搜索栏
    list_filter = ['sign']               # 过滤器

admin.site.register(Event,EventAdmin)
admin.site.register(Member,MemberAdmin)