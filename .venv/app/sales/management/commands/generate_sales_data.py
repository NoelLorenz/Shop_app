from django.core.management.base import BaseCommand
from faker import Faker
from sales.models import Odr, Orderitems
from libraries.models import Customers, Products

fake = Faker()

class Command(BaseCommand):
    help = 'Generate Random Order and Orderitems data. Command should be python manage.py run generate_sales_data --orders2 --order_items10'

    # Adding arguments to dynamically control number of flights and passengers
    def add_arguments(self, parser):
        parser.add_argument(
            '--orders',
            type=int,
            default=2,
            help='Number of orders to generate (default is 2)',
        )

        parser.add_argument(
            '--order_items',
            type=int,
            default=10,
            help='Number of items per order (default is 10)',
        )

    def handle(self, *args, **kwargs):
        # Fetch the values for flights and passengers from the command line arguments
        num_orders = kwargs['orders']
        num_order_items = kwargs['order_items']

        self.stdout.write(
            self.style.SUCCESS(f'Starting to create {num_orders} ordrs with {num_order_items} order_items each.'))

        for i in range(num_orders):

            order_id_choice = Customers.objects.order_by('?').first()
            order_pay_method = fake.random_element(elements=[1, 2, 3])

            order = Odr.objects.create(
                order_buyer_id = order_id_choice,
                orderpay_method = order_pay_method
            )
        for order in Odr.objects.all():
            for i in range(num_orders):
                items = Products.objects.order_by('?').first()
                item_size = fake.random_element(elements=[1, 2, 3])
                item_qty = fake.random_int(min=3, max=9)
                item_status = fake.random_element(elements=[1, 2])
                item_size = fake.random_element(elements=[1, 2,3])


                Orderitems.objects.create(
                    oi_order    =order,
                    oi_type     = items,
                    oi_size     = item_size,
                    oi_qty      = item_qty,
                    oi_status   = item_status,
                )
                self.stdout.write(
                    self.style.SUCCESS(f'Created {num_orders} orders with {num_order_items} order_items each.'))

            # order_id_choice = fake.random_element(elements=[1, 2, 3])
            # flight_name = dict(Flights.FLIGHT_NAMES).get(flight_name_choice, 'Unknown Airline')
            #
            # # Generate the flight_no based on the flight_name choice
            # if flight_name_choice == 1:
            #     flight_no = f"PAL-{fake.bothify(text='####')}"  # PAL- followed by random digits
            # elif flight_name_choice == 2:
            #     flight_no = f"CEB-{fake.bothify(text='####')}"  # CEB- followed by random digits
            # elif flight_name_choice == 3:
            #     flight_no = f"AIR-{fake.bothify(text='####')}"  # AIR- followed by random digits
            # else:
            #     flight_no = fake.bothify(text='??######')  # Fallback in case something unexpected happens

            # Random Flight City (assuming you have existing cities in the Cities table)
            # random_city = Cities.objects.order_by('?').first()  # Getting a random city