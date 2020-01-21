import json
from django.http import JsonResponse, HttpResponse
from django.views import View
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
           
'''

class BookListView(View):
    #获取所有的书籍
    def get(self,request):
        books = BookInfo.objects.all()
        #
        serializer=BookInfoSerializer(books,many=True)
        return JsonResponse(serializer.data,safe=False)#如果返回是列表需要设置safe参数为false



        # 新增一本书籍
    def post(self,request):
        #获取参数
        book_dict=json.loads(request.body)
        #创建序列化器，进行反序列化处理时设置data为请求参数的字典
        serializer=BookInfoSerializer(data=book_dict)
        # is_valid() 执行校验（数据的完整性， 数据的合法性，自定义的需求校验）
        result=serializer.is_valid()
        '''
        校验的结果：result
        校验的错误信息：serializer.errors
        校验成功后的数据：serializer.validated_data
        '''
        if result==False:
            return JsonResponse({'detail':serializer.errors},status=400)
        #新增数据
        book=serializer.save()
        #返回结果
        return JsonResponse(serializer.data,status=201)




class BookView(View):
    #获取指定的书籍
    def get(self,request,pk):
        try:
            book=BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail':'book not exist'},status=404)
        serializer=BookInfoSerializer(book)
        return JsonResponse(serializer.data,status=201)
    #修改指定的书籍
    def put(self,request,pk):
        #获取书籍
        book_dict=json.loads(request.body)

        #查询书籍
        try:
            book=BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail':'book not exist'},status=404)
        serializer=BookInfoSerializer(book,data=book_dict)
        result=serializer.is_valid()
        if  result==False:
            return JsonResponse({'errno':'参数错误'},status=400)
        book=serializer.save()
        return JsonResponse(serializer.data,status=201)
    #删除指定的书籍
    def delete(self,request,pk):
        #查询指定的书籍
        try:
            book=BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail':'书籍不存在'},status=404)
        book.delete()
        return HttpResponse(status=204)
