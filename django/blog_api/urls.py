from .views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'blog_app'

router = DefaultRouter()
router.register('',PostList,basename='user')

urlpatterns = router.urls