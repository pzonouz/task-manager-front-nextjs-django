from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from categories.views import CategoryViewset
from django.contrib import admin
from django.urls import include, path
from priorities.views import PriorityViewset
from projects.views import ProjectsViewset
from tags.views import TagsViewset
from tasks.views import TasksViewset

router = DefaultRouter()
router.register("api/v1/tasks", TasksViewset)
router.register("api/v1/categories",CategoryViewset)
router.register("api/v1/priorities",PriorityViewset)
router.register("api/v1/tags",TagsViewset)
router.register("api/v1/projects",ProjectsViewset)
urlpatterns = [
    path("api/v1/admin/", admin.site.urls),
    path("api/v1/auth/", include("users.urls")),
]
urlpatterns += router.urls
