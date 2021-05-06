from deposits.models import Deposit
from django.views.generic import ListView, FormView, DetailView
from django.urls import reverse_lazy
from deposits.forms import AddDepositForm
import math


class DepositListView(ListView):

    model = Deposit
    template_name = 'index.html'


class AddDepositView(FormView):

    form_class = AddDepositForm
    template_name = 'add_deposit_form.html'
    success_url = reverse_lazy('deposit-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        A = math.pow((1 + self.object.rate), self.object.term)
        B = (self.object.deposit * A) - self.object.deposit
        self.object.interest = B

        self.object.save()

        response = super().form_valid(form)
        return response


class GetDepositDetailView(DetailView):

    model = Deposit
    template_name = 'got_deposit.html'
