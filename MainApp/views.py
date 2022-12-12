from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    """the home page for Pizzeria"""
    return render(request,'MainApp/index.html')
    
def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')

    context = {'all_pizzas':pizzas}
    return render(request,"MainApp/pizzas.html",context)

def pizza(request,pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    comments = Comment.objects.filter(pizza=p)

    pictures = Picture.objects.filter(pizza=p)

    context = {'pizza':p,'toppings':toppings,'comments':comments,'pictures':pictures}
    return render(request,"MainApp/pizza.html",context)

def comment(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = PizzaCommentForm()
    else:
        print(request.POST)
        form = PizzaCommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.save()
            return redirect('MainApp:pizza',pizza_id=pizza_id)

    context = {'form':form,'pizza':pizza}
    return render(request,"MainApp/comment.html",context)


