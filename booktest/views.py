import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.exceptions import *
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

           
'''

class BookListView(APIView):
    #获取所有的书籍
    def get(self,request):
        books = BookInfo.objects.all()
        #
        serializer=BookInfoSerializer(books,many=True)
        #drf的Response类型可以根据前端的需求（请求头的Accept字段）
        return Response(serializer.data)



        # 新增一本书籍
    def post(self,request):
        #获取参数
        book_dict=request.data
        # book_dict=json.loads(request.body)
        #创建序列化器，进行反序列化处理时设置data为请求参数的字典
        serializer=BookInfoSerializer(data=book_dict)
        # is_valid() 执行校验（数据的完整性， 数据的合法性，自定义的需求校验）
        result=serializer.is_valid(raise_exception=True)
        '''
        校验的结果：result
        校验的错误信息：serializer.errors
        校验成功后的数据：serializer.validated_data
        # '''
        # if result==False:
        #     return JsonResponse({'detail':serializer.errors},status=400)
        #新增数据
        book=serializer.save()
        #返回结果
        return Response(serializer.data,status=201)




class BookView(APIView):
    #获取指定的书籍
    def get(self,request,pk):
        try:
            book=BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise NotFound()
            # return JsonResponse({'detail':'book not exist'},status=404)
        serializer=BookInfoSerializer(book)
        return Response(serializer.data,status=201)
    #修改指定的书籍
    def put(self,request,pk):
        #获取书籍
        # book_dict=json.loads(request.body)
        book_dict=request.data

        #查询书籍
        try:
            book=BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise NotFound()
            # return JsonResponse({'detail':'book not exist'},status=404)
        serializer=BookInfoSerializer(book,data=book_dict)
        result=serializer.is_valid(raise_exception=True)
        # if  result==False:
        #     return JsonResponse({'errno':'参数错误'},status=400)
        book=serializer.save()
        return Response(serializer.data,status=201)
    #删除指定的书籍
    def delete(self,request,pk):
        #查询指定的书籍
        try:
            book=BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail':'书籍不存在'},status=404)
        book.delete()
        return HttpResponse(status=204)
