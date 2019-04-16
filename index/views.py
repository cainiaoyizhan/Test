import random

import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.



def index(request):
    if request.method == 'GET':
        if 'username' in request.session and 'password' in request.session:
            # 如果用户登录过，从其他按钮连接过来，返回'欢迎...'页面
            username = request.session['username']
            return render(request,'index.html',{'user':1,'username':username})
        else:
            return render(request,'index.html',{'user':''})
    elif request.method == 'POST':
        username = request.POST['username']
        user = User.objects.filter(username=username)
        # user = User.objects.filter(username=username).first()

        if user:
            # 用户存在，判断密码，存session，返回首页，locals传递user
            result = check_password(request.POST['password'], user[0].password)
            if result:
                request.session['username'] = username
                request.session['password'] = request.POST['password']
                return render(request,'index.html',locals())
            else:
                return render(request,'index.html',{'mess':'密码不正确','user':''})
        else:
            # 用户不存在，返回首页，传递user为空
            return render(request,'index.html',{'mess':'用户名不正确','user':''})

def register(request):
    if request.method == 'GET':
        return render(request,'reg.html')
    elif request.method == 'POST':
        user = User()
        user.username = request.POST['username']
        query_user = User.objects.filter(username=user.username)
        # 验证用户名是否存在,ajax前端验证
        if query_user:
            return render(request,'reg.html',{'Message':'该用户名已存在'})
        else:
            # user.password = request.POST['password']
            # apassword = request.POST['apassword']
            # 前端验证
            # if user.password == apassword:
            user.name = request.POST['name']
            user.phone = request.POST['phone']
            user.email = request.POST['email']
            user.address = request.POST['address']
            user.password = make_password((request.POST['password']), None, 'pbkdf2_sha1')
            user.save()
            return redirect('/')
            # else:
            #     return render(request,'reg.html',{'errMsg':'两次密码不一致'})
def check_username(request):
    username = request.POST.get('username')
    query_user = User.objects.filter(username=username)
    if query_user:
        return HttpResponse('该用户名已存在')
    else:
        return HttpResponse('ok')

def logout(request):
    sessions = request.session
    del sessions['username']
    del sessions['password']
    user = ''
    return render(request,'index.html',{'user':user})



def search(request):
    # 查询数据库中所有商品详情信息
    product_details = Product_detail.objects.all()
    # 根据商品详情查询商品
    return render(request, 'search.html',locals())

def product(request):
    # 不管用户是否登录，查询出数据库中所有商品
    products = Product.objects.all()
    product_list = []
    for product in products:
        product_list.append(product)
    return render(request, 'product.html', locals())

def shopcar(request):
    if request.method == 'GET':
        # 如果用户在登录状态，购物车才有数据
        if 'username' in request.session:
            username = request.session['username']
            user = User.objects.filter(username=username)[0]
            # 通过用户查找购物车
            cart = user.cart_set.all()[0]
            #　通过购物车查找所有商品
            products = cart.product_set.all()

            # 存放商品的列表
            product_list = []
            for product in products:
                # 商品isDelete是否为０
                if product.isDelete == 0:
                    product_list.append(product)
            return render(request,'shopcar.html',{'product_list':product_list,'username':username})
        else:
            return render(request,'shopcar.html',{'username':''})
    # post请求：提交到订单页面,将购物车信息保存进数据库
    elif request.method == 'POST':
        pass

# 处理删除购物车中的商品
def isDelete(request,id):
    url = request.META.get('HTTP_REFERER','/shopcar')
    # 删除商品，修改isDelete字段
    product = Product.objects.filter(id=id)[0]
    product.isDelete = 1
    product.save()
    return redirect(url)

# 向购物车添加商品,一次只能添加一个商品
def add_product(request,id):
    # 在search.html页面判断商品是否选中,一次添加多个商品(后续完成)
    # 加入商品前，将商品的isDelete改为０
    product = Product.objects.filter(id=id)[0]
    product.isDelete = 0
    product.save()
    # 从product_d.html页面或search.html点击加入购物车提交到此地址,添加商品后应返回源地址
    url = request.META.get('HTTP_REFERER','/')
    return redirect(url)

def order(request):
    if request.method == 'GET':
        return render(request,'order.html')


def price_view(request):
    return render(request,'price.html')

def diploma_view(request):
    return render(request,'diploma.html')

def payway_view(request):
    return render(request,'payway.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')

# def save_img(img):
#     # 保存图片到指定目录下
#     ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
#     print(img)
#     print(str(img))
#     print(img.read())
#     ext = str(img).split('/')[-1]
#     filename = ftime + '.jpg'
#     print(filename)
#     # 拼接保存文件路径,文件夹需手动创建，不会自动生成
#     img_name = 'media/head_images/' + filename
#     # 读写保存头像到文件
#     with open(img_name, 'wb') as f:
#         print('ttttttttttttttttt')
#         f.write(img.read())


def user_view(request):
    # get请求不需要保存头像
    if request.method == 'GET':
        url = request.META.get('HTTP_REFERER','/')
        username = request.session.get('username','')
        if username:
            query_user = User.objects.filter(username=username)[0]
            # 第一次登录用户的默认头像
            img = query_user.img
        # 如果没有登录,不显示用户名，不显示头像
        if username == '':
            return render(request,'user.html')
        # 如果登录了
        else:
            return render(request,'user.html',{'username':username,'img':img})
    elif request.method == 'POST':

        username = request.session['username']
        # user和user_details是一对一关系，所以只能添加一次和修改,不能添加多次
        query_user = User.objects.filter(username=username)[0]
        user_detail = User_details()
        user_detail.email = request.POST.get('email',None)
        user_detail.datetime = request.POST.get('datetime',None)
        user_detail.telephone = request.POST.get('telephone',None)
        user_detail.phone = request.POST.get('phone',None)
        user_detail.qq = request.POST.get('qq',None)
        # 判断用户是否上传头像,每get一次图片，系统就自动保存一次
        if request.FILES:
            user_detail.img = request.FILES.get('image')
            # user表中Img字段应同步修改,为什么保存到headImages路径下？
            query_user.img = user_detail.img
            query_user.save()
        else:
            user_detail.img = query_user.img
        # 如果是第一次点击确定，则正常执行下边语句，如果是第二次执行user_detail.user = query_user时触发异常,
        try:
            user_detail.user = query_user
            user_detail.save()
            return render(request, 'user.html',{'img':user_detail.img})

        except:
            print('++++++++++++++')
            username = request.session['username']
            query_user = User.objects.filter(username=username)[0]
            # 查询出用户为query_user在user_details表中的记录,并对其进行修改
            query_user_detail = User_details.objects.filter(user=query_user)[0]
            query_user_detail.email = request.POST.get('email',None)
            query_user_detail.datetime = request.POST.get('datetime', None)
            query_user_detail.telephone = request.POST.get('telephone', None)
            query_user_detail.phone = request.POST.get('phone', None)
            query_user_detail.qq = request.POST.get('qq', None)

            # 判断用户是否上传头像
            if request.FILES:
                query_user_detail.img = request.FILES.get('image')
            else:
                query_user_detail.img = query_user.img
            query_user_detail.save()
            return render(request,'user.html',{'img':query_user_detail.img})


def address(request):
    return render(request,'address.html')

def book(request):
    return render(request,'book.html')

def product_d(request,id):
    # 不管这个商品的isDelete是否为１，都修改成０
    product = Product.objects.filter(id=id)[0]
    product.isDelete = 0
    product.save()

    return render(request,'product_d.html',{'product':product})

def repwd(request):
    if request.method == "GET":
        return render(request, 'repwd.html')

    elif request.method == 'POST':
        # 登录之后才能修改密码
        if 'username' in request.session:
            username = request.session['username']
            user = User.objects.get(username=username)
            password = user.password
            old_password = request.get('old_password')
            if password != old_password:
                return render(request,'repwd.html',{'errMsg':'原密码错误！'})
            else:
                new_password = request.POST.get('new_password')
                user.password = new_password
                user.save()
                return render(request,'repwd.html')
        else:
            return render(request,'repwd.html',{'errMsg':'请您先登录！'})







