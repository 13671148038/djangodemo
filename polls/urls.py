from django.urls import path
from polls import views

app_name = 'polls'
urlpatterns = [
    path('addData', views.add_data, name='addData'),
    path('', views.index, name='index'),
    path('<question_id>', views.detail, name='detail'),
    path('<question_id>/results', views.result, name='result'),
    path('<question_id>/vote', views.vote, name='vote')
]
