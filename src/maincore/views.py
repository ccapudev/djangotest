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

    def get_options(self):
        from django.db import models
        props = dir(models)
        options = list()
        for prop in props:
            try:
                if issubclass(getattr(models, prop), models.Field):
                    options.append(prop)
            except Exception as e:
                pass
        return options

    def get(self, request):
        return JsonResponse(self.get_options(), safe=False)