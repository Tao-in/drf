from django.views import View
'''
RESTful风格：增加  post
            删除 delete
            修改  put
            查询  get
'''

class BookListView(View):
    #获取所有的书籍
    def get(self,request):
        pass

    #新增一本书籍
    def post(self,request):
        pass

class BookView(View):


    #获取指定的书籍
    def get(self,request):
        pass


    #修改指定的书籍
    def put(self,request):
        pass

    #删除指定的书籍
    def delete(self,request):
        pass