from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received  # Fixed spelling
from django.dispatch import receiver
from django.conf import settings
import time
from .models import Order

@receiver(valid_ipn_received)  
def paypal_payment_received(sender, **kwargs): 
    # add 10sec pause for paypal to send IPN data
    time.sleep(10)
    # Grab the information that paypal send for mc_gross
    paypal_obj = sender
    # Grab the invoice
    my_invoice = str(paypal_obj.invoice)
    # match invoice to the order invoice
    # look up order
    my_order = Order.objects.get(invoice=my_Invoice)
    # record the order was paid
    my_order.paid = True
    # save the order
    my_order.save()
    print(paypal_obj)
    print(f'Amount Paid: {paypal_obj.mc_gross}')