from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

# 登录
# 对路径进行重定向（HttpResponseRedirect）
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # 登录
        if username == 'admin' and password == '123456':
            response = HttpResponseRedirect('/test_manage/')
            request.session['user'] = username # 将session信息记录到浏览器
            return response
        else:
            return render(request, 'index.html', {'error': '用户名或密码错误，请重新输入！'})

# 测试发布管理后台
@login_required
def test_manage(request):
    username = request.session.get('user', '') # 读取浏览器session
    return render(request, "test_manage.html", {"user":username})