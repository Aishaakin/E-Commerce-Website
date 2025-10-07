from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received  # Fixed spelling
from django.dispatch import receiver
from django.conf import settings

@receiver(valid_ipn_received)  
def paypal_payment_received(sender, **kwargs): 
    # Grab the information that paypal send for mc_gross
    paypal_obj = sender
    print(paypal_obj)
    print(f'Amount Paid: {paypal_obj.mc_gross}')