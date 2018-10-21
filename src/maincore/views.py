from django.views.generic import View, ListView
from django.http.response import JsonResponse
from .models import App, Model, Field


class ModuleViewList(View):

    def get(self, request):
        objects = list(App.objects.all().values(
            'uid', 'name', 'module'
        ))
        return JsonResponse(objects, safe=False)


class ModelViewList(View):

    def get(self, request):
        objects = list(Model.objects.all().values(
            'uid',
            'app__uid',
            'app__module',
            'app__name',
            'name'
        ))
        return JsonResponse(objects, safe=False)


class FieldViewList(View):

    def get(self, request):
        objects = list(Field.objects.all().values(
            'uid',
            'model__uid',
            'model__name',
            'name',
            'type'
        ))
        return JsonResponse(objects, safe=False)


class FieldOptionsViewList(View):

    def get(self, request):
        from maincore.utils import get_valid_fields
        return JsonResponse(get_valid_fields(), safe=False)