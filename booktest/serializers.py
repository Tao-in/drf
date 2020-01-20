from rest_framework.serializers import *


class BookInfoSerializer(Serializer):
    '''定义一个书籍序列化器类'''

    #进行反序列化处理时，考虑到数据的完整性。设置read_only为True，表示此参数字段只进行序列化处理
    id=IntegerField(read_only=True)
    btitle=CharField()
    bpub_date=DateField()
    bread=IntegerField(read_only=True)
