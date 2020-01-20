from rest_framework.serializers import *


class BookInfoSerializer(Serializer):
    '''定义一个书籍序列化器类'''
    id=IntegerField()
    btitle=CharField()
    bpub_date=DateField()
    bread=IntegerField()
