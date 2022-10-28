from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from article.serializers import ArticleSerializer
from article.models import Article

class ArticleView(APIView):
    def get(request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

