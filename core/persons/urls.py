from persons.views import *
from django.urls import path

urlpatterns = [
    path("/", all_persons),
    path("id/<str:person_id>", by_id),

    path("create/<str:name>/<str:surname>", by_id),
    path("delete/<int:person_id>", by_id),
]