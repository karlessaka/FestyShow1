from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from Festy.metier.model.models import Administrator, Artist, Concert, Booking  # adapte selon ton projet

fake = Faker()

class Command(BaseCommand):
    help = "Seed la base de données avec des données fictives"

    def handle(self, *args, **kwargs):
        self.stdout.write("🌱 Création de données fictives...")

        # Exemple : créer 5 administrateurs
        for _ in range(5):
            Administrator.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                password="password123"
            )

        # Exemple : créer 10 artistes
        STYLE_KEYS = [choice[0] for choice in Artist.style_choices]
        for _ in range(10):
            Artist.objects.create(
                bio=fake.text(),
                link=fake.url(),
                Full_name=fake.name(),
                style=fake.random_element(elements=STYLE_KEYS),
                email=fake.email()
            )

        # Exemple : créer 5 concerts
        for _ in range(5):
            Concert.objects.create(
                title=fake.sentence(nb_words=3),
                date_time=fake.date_time_between(start_date="now", end_date="+30d", tzinfo=timezone.get_current_timezone()),
                artist=Artist.objects.order_by('?').first(),
                location = fake.city(),
                seats_available=150
            )

        # Exemple : créer des reservations
        for _ in range(15):
            Booking.objects.create(
                concert=Concert.objects.order_by('?').first(),
                user_name=fake.name(),
                user_email=fake.email(),
                code_booking=fake.uuid4()
            )
            
        self.stdout.write(self.style.SUCCESS("✅ Données fictives créées avec succès !"))
