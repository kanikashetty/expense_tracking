from django.conf.urls import url, include
from .views import listClientExpenses,listClientNames,addClient,addExpense

urlpatterns = [
    url(r'^listClientNames$', listClientNames, name="ClientNames"),
    url(r'^listClientExpenses/(?P<client_name>.*)/$', listClientExpenses, name="ClientExpenses"),
    url(r'^addClient$', addClient, name="addClient"),
    url(r'^addExpense/(?P<client_name>.*)/$', addExpense, name="addExpense"),
]