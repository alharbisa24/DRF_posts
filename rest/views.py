from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import Post
from rest.serializers import PostSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, filters

class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page' 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    pagination_class = MyPageNumberPagination
    ordering_fields = ['id', 'title', 'created_at']
    ordering = ['id']

    @action(detail=False, methods=['get'])
    def recent_posts(self, request):
        recent_posts = Post.objects.order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_posts, many=True)
        return Response(serializer.data)
