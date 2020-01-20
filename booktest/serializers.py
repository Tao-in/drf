from rest_framework.serializers import *


class BookInfoSerializer(Serializer):
    '''定义一个书籍序列化器类'''
    #进行反序列化处理时，考虑到数据的完整性。设置read_only为True，表示此参数字段只进行序列化处理
    #read_only：表示该字段只进行序列化处理
    #write_only:表示该字段只进行反序列化处理、
    #required：该参数默认为True，表示必须传入
    #default：表示该字段的默认值，只当required参数为false时default才有用
    #error_messages={}：表示为字段设置默认的错误信息
    #label='' ：表示该字段在html中页面的字段名
    #max_length/min_length 只能用于CharField字段，表示字段的长度限制
    id=IntegerField(read_only=True)
    btitle=CharField()
    bpub_date=DateField()
    bread=IntegerField(read_only=True)
    #max_value/min_value 只能用于限制数字类型长度字段



