from django.db import models
from django.contrib.auth.models import User
from plans.models import Plan
from payment_terms.models import PaymentTerm

class Product(models.Model):
    plan = models.ForeignKey(Plan, related_name='plan', on_delete=models.CASCADE)
    payment_term = models.ForeignKey(PaymentTerm, related_name='payment_term', on_delete=models.CASCADE)
    cost = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('plan', 'payment_term')

    def __str__(self):
        return self.plan.hmo.name + ' - ' + self.plan.name + ' (' + self.payment_term.name + ')'
