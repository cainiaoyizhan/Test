# 用于验证码的操作

import os
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image,ImageDraw,ImageFont
import random
# 用于操作内存文件
import io
def randcolor():
    return random.randrange(0,255),255,random.randrange(0,255)

def verifycode(request):
    bgcolor = '#FFA'
    width = 100
    height = 30
    # 创建画布对象
    img = Image.new('RGB',(width,height),bgcolor)
    str1 = 'ABCDE12F3G4H5I6JK7LM8NOP9QRS0TUVWXYZ'
    # 创建画笔对象
    draw = ImageDraw.Draw(img)
    rand_str = ''

    # 生成四个字母
    # for i in range(0,4):
    #     rand_str += str1[random.randrange(0,len(str1))]
    font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf',23)
    # draw.text((5,2),rand_str,font=font,fill=randcolor())

    # 生成算式
    num_1 = {"1":'壹',"2":"贰","3":"叁","4":"肆","5":"伍","6":"陆","7":"柒","8":"捌","9":"玖"}
    num_2 = random.randint(1,50)
    sign = ['+','-']
    num_1_n = random.randrange(1,10)
    num_1_s = str(num_1_n)
    first_s = num_1[num_1_s]
    third_s = str(num_2)
    sign_n = random.randrange(0,2)
    second_s = sign[sign_n]
    if sign_n == 0:
        last = num_1_n + num_2
    else:
        last = num_2 - num_1_n
    last_s = str(last)
    fontcolors = ['yellow','green','orange','pink','red','violet']
    draw.text((5, 2), '?', font=font, fill=random.sample(fontcolors, 1)[0])
    draw.text((20, 2), second_s, font=font, fill=random.sample(fontcolors, 1)[0])
    draw.text((35, 2), first_s, font=font, fill=random.sample(fontcolors, 1)[0])
    draw.text((60, 2), '＝', font=font, fill=random.sample(fontcolors, 1)[0])
    draw.text((75, 2), last_s, font=font, fill=random.sample(fontcolors, 1)[0])

    # 点
    for i in range(100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        draw.point(xy,fill=(random.randrange(0,255),255,random.randrange(0,255)))

    # 线
    for i in range(5):
        x1 = random.randrange(0,width)
        y1 = random.randrange(0,height)
        x2 = random.randrange(0,width)
        y2 = random.randrange(0,height)
        draw.line((x1,y1,x2,y2),fill=randcolor())

    # 圆弧
    for i in range(5):
        x = random.randrange(0,width)
        y = random.randrange(0, height)
        draw.arc((x,y,x+8,y+8),0,360,fill=randcolor())
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = io.BytesIO()
    img.save(buf,'png')

    return HttpResponse(buf.getvalue(),'image/png')
