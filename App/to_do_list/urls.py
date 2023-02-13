from django.urls import path

from to_do_list.views import base

from to_do_list.views.tasks import detail_view

urlpatterns = [
    path('', base.index_view),
    path('task/add/', add_task),
    path('article/', detail_view),
]