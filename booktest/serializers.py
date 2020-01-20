from rest_framework.serializers import *


def vali_btitle(data:str):#data  表示原始的btitle
    data=data.lower()#转换小写
    if not data.startswith('taoin:'):

        # Python中的raise关键字用于引发一个异常
        raise ValidationError({'erron':'没有以taoin：开头'})




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
    # btitle=CharField()
    bpub_date=DateField()
    bread=IntegerField(read_only=True)
    #max_value/min_value 只能用于限制数字类型长度字段

    '''自定义校验的三种方法：想要验证btitle以 Taoin：开头'''

    #1，自定义函数
    # btitle=CharField(validators=[vali_btitle])

    #2，自定义方法
    # btitle=CharField()
    # def validate_btitle(self, data):
    #     data=data.lower()
    #     if not data.startswith('taoin:'):
    #     # Python中的raise关键字用于引发一个异常
    #         raise ValidationError({'erron': '没有以taoin：开头'})
    #     return data[6:]#对原始参数进行加工，切片的形式之后的数据保存到数据库
    #3，重写方法
    btitle=CharField()
    def validate(self, attrs):#attrs是一个字典,是前端传来的所有数据
        print(attrs)
        btitle=attrs.get('btitle')
        btitle=btitle.lower()
        if not btitle.startswith('taoin:'):
            raise ValidationError({'erron':'没有以taoin：开头'})
        attrs['btitle']=btitle[6:]
        return attrs






