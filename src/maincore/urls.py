from django.urls import path
from .views import (
    ModuleViewList, ModelViewList, FieldViewList,
    FieldOptionsViewList
)

urlpatterns = [
    path('apps/', ModuleViewList.as_view()),
    path('models/', ModelViewList.as_view()),
    path('fields/', FieldViewList.as_view()),
    path('fields/options/', FieldOptionsViewList.as_view()),
]