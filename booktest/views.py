import json

from django.http import JsonResponse, HttpResponse
from django.views import View

from .serializers import BookInfoSerializer
from .models import *

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

        #序列化多个对象,序列化多个对象时要设置many为True
        serializer=BookInfoSerializer(books,many=True)
        #一对多的正向查询
        hero=HeroInfo.objects.first()#first按主键的排序从小到打，last从大到小，get指定取出
        print(hero.hname)
        print(hero.get_hgender_display())#获取性别的展示值

        #一对多的反向查询
        # book=BookInfo.objects.first()
        # print(book.heroinfo_set.all())
        #序列化多个对象时，serializer.data 为列表，里面元素为字典
        return JsonResponse(serializer.data,safe=False)#如果返回是列表需要设置safe参数为false



        # 新增一本书籍
    def post(self,request):
        #获取参数
        json_bytes = request.body
        json_str = json_bytes.decode('utf-8')
        book_dict = json.loads(json_str)
        print(book_dict)
        btitle=book_dict.get('btitle')
        bpub_date=book_dict.get('bpub_date')
        # Tooo 校验参数
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
