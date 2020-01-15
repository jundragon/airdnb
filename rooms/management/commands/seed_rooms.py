import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 5),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute()
        created_rooms_flat = flatten(list(created_rooms.values()))

        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        house_rules = room_models.HouseRule.objects.all()

        for pk in created_rooms_flat:
            room = room_models.Room.objects.get(pk=pk)

            # seed photos 생성
            # /uploads/room_seeds/1.webp
            for i in range(0, random.randint(5, 10)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_seeds/{random.randint(1, 31)}.webp",
                )

            for a in amenities:
                if random.randint(0, 15) % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:
                if random.randint(0, 15) % 2 == 0:
                    room.facilities.add(f)

            for hr in house_rules:
                if random.randint(0, 15) % 2 == 0:
                    room.house_rules.add(hr)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
