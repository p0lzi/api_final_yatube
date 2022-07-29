from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                'comment')
router.register(r'follow', FollowViewSet)

v1_urlpatterns = (
    [
        path('', include(router.urls)),
        path('', include('djoser.urls')),
        path('', include('djoser.urls.jwt')),
    ],
    'v1'
)

urlpatterns = [
    path('v1/', include(v1_urlpatterns))
]
