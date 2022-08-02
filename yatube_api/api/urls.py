from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(r'groups', GroupViewSet, basename='group')
router_v1.register(r'^posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comment')
router_v1.register(r'follow', FollowViewSet, basename='follow')

v1_urlpatterns = (
    [
        path('', include(router_v1.urls)),
        path('', include('djoser.urls.jwt')),
    ],
    'v1'
)

urlpatterns = [
    path('v1/', include(v1_urlpatterns))
]
