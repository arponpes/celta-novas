from rest_framework import routers
from .views import ArticleViewSet

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet, basename='articles')
urlpatterns = router.urls
