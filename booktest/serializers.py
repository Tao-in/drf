from rest_framework.serializers import *
class HeroInfoSerializer(Serializer):
    id=IntegerField()
    hname=CharField()
    #想要自定义序列化处理，把字段定义成SerializerMethodField
    hgender=SerializerMethodField()
    def get_hgender(self, instance):
        #自定义字段的序列化处理
        #instances是模型对象
         return instance.get_hgender_diplay()#返回的是自定义的性别的显示

class BookInfoSerializer(Serializer):
    '''定义一个书籍序列化器类'''
    id=IntegerField()
    btitle=CharField()
    bpub_date=DateField()
    bread=IntegerField()

    '''通过序列化获取关联数据，三种定义方式；
    如果是对多关系设置many为True
    如果是关系字段设置rend_only 为True'''

    #1，定义关系主键字段
    # heroinfo_set=PrimaryKeyRelatedField(many=True,read_only=True
    #2.定义字符串关系字段,会返回关系字段的__str__方法的返回值
    # heroinfo_set=StringRelatedField(many=True,read_only=True)
    #3.自定义一个英雄序列化器的字段用于返回关系字段
    heroinfo_set=HeroInfoSerializer(many=True)
