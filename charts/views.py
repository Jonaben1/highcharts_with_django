from django.shortcuts import render
from .models import Passenger
from django.db.models import ( Count, Q, F, ExpressionWrapper, IntegerField, 
                              Avg, Sum, Min, Max  )
from .models import Passenger
import json
from django.shortcuts import render


def survivors_by_ticket_class(request):
    dataset = []
    for ticket_class in Passenger.objects.values_list('p_class', flat=True).distinct():
        survived_count = Passenger.objects.filter(p_class=ticket_class, survived=True).count()
        not_survived_count = Passenger.objects.filter(p_class=ticket_class, survived=False).count()
        dataset.append({
            'ticket_class': ticket_class,
            'survived_count': survived_count,
            'not_survived_count': not_survived_count
        })


    survivors = {
        'name': 'Survived',
        'data': [data['survived_count'] for data in dataset],
        'color': 'green'
    }

    death = {
        'name': 'Not Survived',
        'data': [data['not_survived_count'] for data in dataset],
        'color': 'red'
    }


    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'xAxis': {'categories': [data['ticket_class'] for data in dataset]},
        'series': [survivors, death]
    }

    dump = json.dumps(chart)

    return render(request, 'ticket_class.html', {'chart': dump})




def survivors_by_gender(request):
    dataset = Passenger.objects \
        .values('sex') \
        .annotate(survived_count=Count('sex', filter=Q(survived=True)),
                  not_survived_count=Count('sex', filter=Q(survived=False))) \
        .order_by('sex')

    survivors = {
        'name': 'Survived',
        'data': [data['survived_count'] for data in dataset],
        'color': 'green'
    }

    death = {
        'name': 'Not Survived',
        'data': [data['not_survived_count'] for data in dataset],
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Gender'},
        'xAxis': {'categories': [data['sex'] for data in dataset]},
        'series': [survivors, death]
    }

    dump = json.dumps(chart)

    return render(request, 'gender.html', {'chart': dump})



def survivors_by_age(request):
    dataset = Passenger.objects \
        .annotate(age_bin=ExpressionWrapper((F('age')/10)*10, output_field=IntegerField())) \
        .values('age_bin') \
        .annotate(survived_count=Count('age_bin', filter=Q(survived=True)),
                  not_survived_count=Count('age_bin', filter=Q(survived=False))) \
        .order_by('age_bin')

    survivors = {
        'name': 'Survived',
        'data': [data['survived_count'] for data in dataset],
        'color': 'green'
    }

    death = {
        'name': 'Not Survived',
        'data': [data['not_survived_count'] for data in dataset],
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Age Group'},
        'xAxis': {'categories': [f"{int(data['age_bin'])}s" for data in dataset]},
        'series': [survivors, death]
    }

    dump = json.dumps(chart)

    return render(request, 'age.html', {'chart': dump})



def survivors_by_embarked(request):
    dataset = Passenger.objects \
        .values('embarked') \
        .annotate(survived_count=Count('embarked', filter=Q(survived=True)),
                  not_survived_count=Count('embarked', filter=Q(survived=Falsesx))) \
        .order_by('embarked')

    survivors = {
        'name': 'Survived',
        'data': [data['survived_count'] for data in dataset],
        'color': 'green'
    }

    death = {
        'name': 'Not Survived',
        'data': [data['not_survived_count'] for data in dataset],
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Port of Embarkation'},
        'xAxis': {'categories': [data['embarked'] for data in dataset]},
        'series': [survivors, death]
    }

    dump = json.dumps(chart)

    return render(request, 'embarked.html', {'chart': dump})




def avg_age_by_ticket_class(request):
    dataset = Passenger.objects \
        .values('p_class') \
        .annotate(avg_age=Avg('age')) \
        .order_by('p_class')

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Average Age by Ticket Class'},
        'xAxis': {'categories': [data['p_class'] for data in dataset]},
        'yAxis': {'title': {'text': 'Average Age'}},
        'series': [{
            'name': 'Average Age',
            'data': [data['avg_age'] for data in dataset],
            'color': 'blue'
        }]
    }

    dump = json.dumps(chart)

    return render(request, 'avg_age.html', {'chart': dump})



def total_fare_by_ticket_class(request):
    dataset = Passenger.objects \
        .values('p_class') \
        .annotate(total_fare=Sum('fare')) \
        .order_by('p_class')

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Total Fare by Ticket Class'},
        'xAxis': {'categories': [data['p_class'] for data in dataset]},
        'yAxis': {'title': {'text': 'Total Fare'}},
        'series': [{
            'name': 'Total Fare',
            'data': [data['total_fare'] for data in dataset],
            'color': 'blue'
        }]
    }

    dump = json.dumps(chart)

    return render(request, 'total_fare.html', {'chart': dump})



def min_max_age_by_ticket_class(request):
    dataset = Passenger.objects \
        .values('p_class') \
        .annotate(min_age=Min('age'), max_age=Max('age')) \
        .order_by('p_class')

    min_age = {
        'name': 'Minimum Age',
        'data': [data['min_age'] for data in dataset],
        'color': 'green'
    }

    max_age = {
        'name': 'Maximum Age',
        'data': [data['max_age'] for data in dataset],
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Minimum and Maximum Age by Ticket Class'},
        'xAxis': {'categories': [data['p_class'] for data in dataset]},
        'series': [min_age, max_age]
    }

    dump = json.dumps(chart)

    return render(request, 'min_max_age.html', {'chart': dump})
