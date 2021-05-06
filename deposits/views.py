from deposits.models import Deposit
from django.views.generic import ListView, FormView, DetailView
from django.urls import reverse_lazy
from deposits.forms import AddDepositForm


class Depositt:
    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate

    def interest(self):
        invested = self.deposit
        for year in range(self.term):
            invested = invested * (1 + self.rate)
        return invested


class DepositListView(ListView):

    model = Deposit
    template_name = 'index.html'


class AddDepositView(FormView):

    form_class = AddDepositForm
    template_name = 'add_deposit_form.html'
    success_url = reverse_lazy('deposit-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        my_deposit = Depositt(deposit=self.object.deposit, term=self.object.term, rate=self.object.rate)
        self.object.interest = my_deposit.interest() - self.object.deposit

        self.object.save()

        response = super().form_valid(form)
        return response


class GetDepositDetailView(DetailView):

    model = Deposit
    template_name = 'got_deposit.html'
