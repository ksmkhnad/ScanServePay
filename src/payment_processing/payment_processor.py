from payment_gateway import PaymentGateway

class PaymentProcessor:
    def __init__(self, gateway_name):
        self.payment_gateway = PaymentGateway(gateway_name)

    def process_payment(self, amount):
        # Placeholder for payment processing logic
        if self.payment_gateway.process_payment(amount):
            return "Payment successful"
        else:
            return "Payment failed"
