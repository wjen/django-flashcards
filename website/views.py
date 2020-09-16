from django.shortcuts import render
from random import randint
import re


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def add(request):

    num_1 = randint(0,9)
    num_2 = randint(0,9)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
        # Error handling for no input
        # Error handling for no input
        if not answer or not answer.isnumeric(): 
            return render(request, 'add.html', {
                'num_1':num_1,
                'num_2':num_2,
                'my_answer': 'Invalid form entry',
                'color': 'warning'
            })

        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = 'CORRECT! ' + old_num_1 + ' + ' + old_num_2 + " = " + answer
            color = 'success'
        else:
            my_answer ='INCORRECT! ' + old_num_1 + ' + ' + old_num_2 + " is not " + answer + ' it is ' + str(correct_answer)
            color = 'danger'
        return render(request, 'add.html', {
            'my_answer': my_answer,
            'answer': answer,
            'num_1': num_1, 
            'num_2': num_2,
            'color': color
        })
    return render(request, 'add.html', {
        'num_1': num_1, 
        'num_2': num_2,
    })

def subtract(request):
    from random import randint

    num_1 = randint(0,9)
    num_2 = randint(0,9)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
        # Error handling for no input
        if not answer or not answer.lstrip('-').isnumeric(): 
            return render(request, 'subtract.html', {
                'num_1':num_1,
                'num_2':num_2,
                'my_answer': 'Invalid form entry',
                'color': 'warning'
            })

        correct_answer = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = 'CORRECT! ' + old_num_1 + ' - ' + old_num_2 + " = " + answer
            color = 'success'
        else:
            my_answer ='INCORRECT! ' + old_num_1 + ' - ' + old_num_2 + " is not " + answer + ' it is ' + str(correct_answer)
            color = 'danger'
        return render(request, 'subtract.html', {
            'my_answer': my_answer,
            'answer': answer,
            'num_1': num_1, 
            'num_2': num_2,
            'color': color
        })
    return render(request, 'subtract.html', {
        'num_1': num_1, 
        'num_2': num_2,
    })

def multiply(request):

    num_1 = randint(0,9)
    num_2 = randint(0,9)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        
        # Error handling for no input
        if not answer or not answer.isnumeric(): 
            return render(request, 'multiply.html', {
                'num_1':num_1,
                'num_2':num_2,
                'my_answer': 'Invalid form entry',
                'color': 'warning'
            })

        correct_answer = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = 'CORRECT! ' + old_num_1 + ' X ' + old_num_2 + " = " + answer
            color = 'success'
        else:
            my_answer ='INCORRECT! ' + old_num_1 + ' X' + old_num_2 + " is not " + answer + ' it is ' + str(correct_answer)
            color = 'danger'
        return render(request, 'multiply.html', {
            'my_answer': my_answer,
            'answer': answer,
            'num_1': num_1, 
            'num_2': num_2,
            'color': color
        })
    return render(request, 'multiply.html', {
        'num_1': num_1, 
        'num_2': num_2,
    })

def divide(request):

    num_1 = randint(0,9)
    num_2 = randint(1,9)

    if request.method == "POST":
        answer = request.POST['answer']
        result = re.match("[-+]?\.?\d+\.?[\d]?$", answer)
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error handling for no input
        if not answer or result is None: 
            return render(request, 'divide.html', {
                'num_1':num_1,
                'num_2':num_2,
                'my_answer': 'Invalid form entry',
                'color': 'warning'
            })

        correct_answer = int(old_num_1) / int(old_num_2)

        if float(answer) == correct_answer:
            my_answer = 'CORRECT! ' + old_num_1 + ' / ' + old_num_2 + ' = ' + answer
            color = 'success'
        else: 
            my_answer = 'INCORRECT! ' + old_num_1 + ' / ' + old_num_2 + ' is not ' + answer + 'it is ' + str(correct_answer)
            color = 'danger'

        return render(request, 'divide.html', {
            'num_1':num_1,
            'num_2':num_2,
            'my_answer': my_answer,
            'answer': answer,
            'color': color
        })
    return render(request, 'divide.html', {
        'num_1':num_1,
        'num_2':num_2,
    })