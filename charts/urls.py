from django.urls import path
from .views import (survivors_by_ticket_class, survivors_by_gender, survivors_by_age,
                    survivors_by_embarked, avg_age_by_ticket_class, total_fare_by_ticket_class,
                    min_max_age_by_ticket_class )


urlpatterns = [
    path('ticket', survivors_by_ticket_class, name='survivors'),
    path('gender', survivors_by_gender, name='gender'),
    path('age', survivors_by_age, name='age'),
    path('embarked', survivors_by_embarked, name='embarked'),
    path('avg_age', avg_age_by_ticket_class, name='avg_age'),
    path('total_fare', total_fare_by_ticket_class, name='total_fare'),
    path('min_max', min_max_age_by_ticket_class, name='min_max'),
]
