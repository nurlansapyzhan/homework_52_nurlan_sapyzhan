from django.urls import path

from to_do_list.views import base

from to_do_list.views.tasks import add_task, delete_task

urlpatterns = [
    path('', base.index_view),
    path('task/add/', add_task),
    path('task/delete/', delete_task)
]