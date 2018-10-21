from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# getcode = '''
# from maincore import create_model
# response = HttpResponse("No Reponse in Code")
# model = create_model('web_log', app_label='dynamic')
# print(model.objects.all())
# contexto = 'Ricolino'
# response = render(request, 'index.html', locals())
# '''
#
# # Create your views here.
# class HomeView(View):
#
#     def get(self, request, **kwargs):
#         exec(getcode)
#         return eval('response')

exec('''
class HomeView(View):

    def get(self, request, **kwargs):
        from maincore import create_model
        response = HttpResponse("No Reponse in Code")
        # model = create_model('web_log_v2', app_label='dynamic')
        # model.create_table()
        # print(model.objects.all())
        contexto = 'Ricolinoz'
        return render(request, 'index.html', locals())
''')