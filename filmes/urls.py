from rest_framework import routers

from filmes.views import ActorViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'actors', ActorViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls