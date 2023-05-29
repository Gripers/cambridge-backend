from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from .views import CourseView, CourseDetailView, TeacherView, RequestView

schema_view = get_swagger_view(title="Cambridge API")

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<int:pk>/", CourseDetailView.as_view()),
    path("teachers/", TeacherView.as_view()),
    path("requests/", RequestView.as_view()),
    path("swagger/", schema_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
