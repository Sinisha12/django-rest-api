from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .model_serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
@csrf_exempt
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        # return JsonResponse(serializer.data, safe=False) #without decorator
        return Response(serializer.data)
    elif request.method == 'POST':
        # data = JSONParser().parse(request) #without decorator
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201) #without decorator
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            # return JsonResponse(serializer.errors, status=400) #without decorator


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return JsonResponse(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
        # return HttpResponse(status=204)
