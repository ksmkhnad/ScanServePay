class PaymentGateway:
    def __init__(self, gateway_name):
        self.gateway_name = gateway_name

    def process_payment(self, amount):
        # Placeholder for payment processing logic using the payment gateway
        print(f"Processing payment of ${amount} using {self.gateway_name}")
        return True  # Placeholder for successful payment confirmation
