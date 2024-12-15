from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, TransactionForm, GoalForm
from .models import Transaction, Goal, Category
from django.db.models import Sum

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create some default categories for the user
            Category.objects.create(name='Rent', user=user)
            Category.objects.create(name='Food', user=user)
            Category.objects.create(name='Entertainment', user=user)
            Category.objects.create(name='Salary', user=user)
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'finance/signup.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'finance/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    income = Transaction.objects.filter(user=request.user, transaction_type='income').aggregate(total=Sum('amount'))['total'] or 0
    expenses = Transaction.objects.filter(user=request.user, transaction_type='expense').aggregate(total=Sum('amount'))['total'] or 0
    goals = Goal.objects.filter(user=request.user)
    context = {
        'income': income,
        'expenses': expenses,
        'goals': goals,
    }
    return render(request, 'finance/dashboard.html', context)

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
        form.fields['category'].queryset = Category.objects.filter(user=request.user)
    return render(request, 'finance/add_transaction.html', {'form': form})

@login_required
def goals(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'finance/goals.html', {'goals': goals})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goals')
    else:
        form = GoalForm()
    return render(request, 'finance/add_transaction.html', {'form': form, 'goal': True})

@login_required
def reports(request):
    return render(request, 'finance/reports.html', {})
