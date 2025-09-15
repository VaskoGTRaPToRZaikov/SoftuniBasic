airline_name = input()
adult_tickets = int(input())
kids_tickets = int(input())
adult_ticket_price = float(input())
service_fee = float(input())

kids_tickets_price = adult_ticket_price * 0.30

adult_ticket_price += service_fee
kids_tickets_price += service_fee

overall_sum = adult_ticket_price * adult_tickets + kids_tickets * kids_tickets_price

profit = overall_sum * 0.20

print(f"The profit of your agency from {airline_name} tickets is {profit:.2f} lv.")