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
'''

class BookListView(View):
    #获取所有的书籍
    def get(self,request):
        books = BookInfo.objects.all()
        print(books)
        book_list=[]
        for book in books:
            book_dict={
                'id':book.id,
                'btitle':book.btitle,
                'bpub_date ':book.bpub_date ,
                'bread':book.bread,
                'bcomment':book.bcomment

            }
            book_list.append(book_dict)
        return JsonResponse(book_list,safe=False)#如果返回是列表需要设置safe参数为false



        # 新增一本书籍
    def post(self,request):
        #获取参数
        book_dict=json.loads(request.body)

        # TODO 校验参数
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
        btitle = serializer.validated_data.get('btitle')
        bpub_date = serializer.validated_data.get('bpub_date')
        #新增数据
        book=BookInfo.objects.create(btitle=btitle,bpub_date=bpub_date)
        #返回结果
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date ': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment

        }
        return JsonResponse(book_dict,status=201)




class BookView(View):


    #获取指定的书籍
    def get(self,request,pk):
        try:

            book=BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail':'book not exist'},status=404)
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date ': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })



    #修改指定的书籍
    def put(self,request,pk):
        #获取书籍
        book=json.loads(request.body)
        btitle=book.get('btitle')
        bpub_date=book.get('bpub_date')
        #TODO 校验参数
        #查询书籍
        try:
            book=BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail':'book not exist'},status=404)

        book.btitle=btitle
        book.bpub_date=bpub_date
        book.save()

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date ': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment

        })





    #删除指定的书籍
    def delete(self,request,pk):
        #查询指定的书籍
        try:
            book=BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'detail':'书籍不存在'},status=404)
        book.delete()
        return HttpResponse(status=204)
