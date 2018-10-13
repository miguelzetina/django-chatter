from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType

from blog.models import Blog

class BlogNode(DjangoObjectType):
    class Meta:
        model = Blog
        interfaces = Node,


class Query(ObjectType):
    blog = Node.Field(BlogNode)
    all_blogs = DjangoConnectionField(BlogNode)


schema = Schema(query=Query)

