import random
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string
from  print_tracker.models import PrintTracker


class Command(BaseCommand): 
    help = 'Creates a lot of fake print jobs'


    def add_arguments(self, parser): 
        parser.add_argument('number_of_prints', type=int, help='Pass a number in to indicate the number of prints to be added to the database')


    def random_hour(self): 
        get_hour = random.randint(1, 101)
        return get_hour

    
    def random_minute(self):
        get_minute = random.randint(1, 60)
        return get_minute


    def handle(self, *args, **kwargs): 
        number_of_prints = kwargs['number_of_prints']
        random_name = get_random_string()
        total_hours_printed = self.random_hour()
        total_minutes_printed = self.random_minute()

        for print in range(number_of_prints):
            save = PrintTracker(print_name=random_name, total_hours_printed=total_hours_printed, total_minutes_printed=total_minutes_printed, material_used='PLA', color='Yellow')
            self.stdout.write(f'{save}')
            save.save()
            
