class PaymentInterface:
    def __init__(self):
        pass

    def display_menu(self, menu):
        # Placeholder for displaying menu to the customer
        print("Menu:")
        for item in menu:
            print(f"- {item.name}: ${item.price}")

    def get_payment_amount(self):
        # Placeholder for getting payment amount from the customer
        amount = float(input("Enter the payment amount: "))
        return amount

    def display_payment_status(self, status):
        # Placeholder for displaying payment status to the customer
        print(status)
