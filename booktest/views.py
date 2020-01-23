import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.exceptions import *
from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import BookInfo
'''
RESTful风格：增加  post
            删除 delete
            修改  put
            查询  get
序列化器的综合使用：
            设置序列化的data参数,可以进行反序列化，
            调用is_vaild,进行数据校验，
        2，调用序列化的save方法进行数据保存
           新增数据不用设置序列化的instance参数，instance即模型类的对象
           
           通过序列化的data属性获取序列化的结果
           
APIView是drf视图的基类，继承自django.View
1,加强版的请求对象，获取请求对象更加方便
2，加强版的响应对象，根据请求头中Accept字段自动包装响应数据
3，封装了异常处理，常见http错误自动包装响应数据
4，支持扩展功能，认证/权限/限流

GenericAPIView
    继承自APIView
1，封装了操作序列化器和数据库查询的属性和方法，便于对常见的视图逻辑进行代码抽取
  操作序列化器：
属性：  serializer_class 指定视图使用的序列化器类
方法： get_serializer(self)返回序列化器对象
  操作数据库查询
属性：  queryset：指定视图集使用的查询集
方法：  get_queryset(self)  返回视图使用的查询集
        get_objects(sekf)  返回视图使用的指定模型对象


           
'''

class BookListView(ListCreateAPIView):
#ListCreateAPIView继承了ListModelMixin和CreateModelMixin两个扩展类
    serializer_class = BookInfoSerializer#指定该视图使用的序列化器类
    queryset = BookInfo.objects.all()#指定该视图使用的查询集
    def get_serializer_class(self):#自定义序列化器类
        if self.request.method=='GET':#如果请求方法为get
            return BookInfoGetSerializer
        # super() 函数是用于调用父类(超类)的一个方法
        return super().get_serializer_class()
    def get_queryset(self):
        if self.request.mothod=='GET':
            return self.queryset[:3]
        return super().get_queryset()



class BookView(RetrieveUpdateDestroyAPIView):
# RetrieveUpdateDestroyAPIView继承了
# RetrieveModelMixin,
# UpdateModelMixin,
# DestroyModelMixin

    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()
