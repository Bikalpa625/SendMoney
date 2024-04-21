from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm

@login_required
def homepage(request):
    return render(request,'sendmoney/homepage.html')


@login_required
def send_money(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            # Handle money transfer logic
            return render(request, 'sendmoney/success.html')
    else:
        form = TransactionForm()
    return render(request, 'sendmoney/send_money.html', {'form': form})

# Create your views here.
