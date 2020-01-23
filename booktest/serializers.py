from rest_framework.serializers import ModelSerializer

from .models import BookInfo

'''ModelSerializer:表示如果序列化器类对应的Django的模型类，则可以继承Model
Serializer,可以基于模型类字段自动生成序列化字段，里面还包含create()和update()
方法的实现。
'''
class BookInfoGetSerializer(ModelSerializer):
    class Meta:
        model=BookInfo#model指定序列化器的模型类
        fields=['id','btitle']

class BookInfoSerializer(ModelSerializer):
    class Meta:
        model=BookInfo#model指定要序列化的模型类
        #fields指定序列化器生成的字段
        fields='__all__'#生成所有字段
        # fields=['id','btitle']#生成指定的
        # exclude=['id']#排除字段，除了id生成其他字段

