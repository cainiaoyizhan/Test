from django.db import models

# Create your models here.
STATUS_CHOICES = {
    (0,'禁用'),
    (1,'正常'),
    (-1,'删除')
}

class User(models.Model):
    username = models.CharField('用户名',max_length=30)
    password = models.CharField('密码',max_length=200)
    name = models.CharField('姓名',max_length=30)
    phone = models.CharField(verbose_name='手机号',max_length=11)
    email = models.EmailField(verbose_name='邮箱',max_length=200)
    address = models.CharField('地址',max_length=200)
    # upload_to的值是图片保存的路径和保存到数据库的部分数据
    img = models.ImageField(verbose_name='用户头像',upload_to='head_images',default='upload/pic5.jpg')

class User_details(models.Model):
    eamil = models.EmailField(verbose_name='邮箱')
    datetime = models.CharField('出生日期',max_length=30,null=True)
    telephone = models.CharField('电话',max_length=20,null=True)
    phone = models.CharField('手机号',max_length=11,null=True)
    qq = models.CharField('qq',max_length=10,null=True)
    img = img = models.ImageField(verbose_name='用户头像',upload_to='headImages',default='pic5.jpg')
    user = models.OneToOneField(User,null=True,on_delete=True)


# 商品表
class Product(models.Model):
    huohao = models.CharField('货号', max_length=30,null=True)
    weight = models.CharField('金重', max_length=20,null=True)
    PT_weight = models.CharField('PT金重', max_length=20,null=True)
    zhushi = models.CharField('主石', max_length=20,null=True)
    fushi = models.CharField('副石', max_length=20,null=True)
    product_name = models.CharField('商品名称',max_length=30)
    product_price = models.FloatField(verbose_name='商品价格',null=True)
    total_price = models.IntegerField(verbose_name='总价',null=True)
    product_num = models.IntegerField(verbose_name='商品数量',null=True)
    product_img = models.ImageField(upload_to='images',null=True)
    isDelete = models.BooleanField('是否删除',default=0)
    # 一个商品一个详情
    product_detail = models.OneToOneField('Product_detail',null=True,on_delete=True)
    # 一个订单对应多个商品
    order = models.ForeignKey('Order',null=True,on_delete=True)
    # 一个购物车对应多个商品
    cart = models.ForeignKey('Cart',null=True,on_delete=True)

# 商品详情表
class Product_detail(models.Model):
    goods_num = models.CharField('货号', max_length=20)
    shape = models.CharField('形状', max_length=10)
    weight = models.CharField('重量', max_length=10)
    color = models.CharField('颜色', max_length=10)
    diameter = models.CharField('直径', max_length=30)

# 购物车表
class Cart(models.Model):
    num = models.IntegerField(verbose_name='商品数量')
    status = models.IntegerField(choices=STATUS_CHOICES,default=1)
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')

    # 一个用户对应多个购物车
    user = models.ForeignKey(User,null=True,on_delete=True)



# 订单表,用户购买记录
class Order(models.Model):
    order_num = models.CharField('订单号',max_length=32) #唯一 日期+随机+订单id
    order_time = models.DateTimeField() #订单发起时间
    order_status = models.IntegerField(choices=STATUS_CHOICES,default=1)
    total_price = models.FloatField()#订单总价
    # 一个用户对应多个订单
    user = models.ForeignKey(User,null=True,on_delete=True)






# 购物车需求
# 单独的购物车页面
# 购物车可以调整商品数量
# 商品页面可以添加至购物车
# 购物车可以删除商品
# 查看所选商品的信息及金额
# 匿名用户也可以使用购物车

