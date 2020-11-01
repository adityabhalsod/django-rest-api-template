# https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html

import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seeding a database is a process in which an initial set of data is provided to a database when it is being installed."

    def __init__(self):
        self.user_class = get_user_model()

        super(Command, self).__init__()

    def handle(self, *args, **options):
        self.create_super_user()

    def create_super_user(self):
        if not os.getenv("ADMIN_EMAIL") or not os.getenv("ADMIN_PASSWORD"):
            self.stdout.write(
                self.style.HTTP_BAD_REQUEST("Environment variable is not set.")
            )
            return False

        if self.user_class.objects.filter(email=os.getenv("ADMIN_EMAIL")).exists():
            self.stdout.write(self.style.HTTP_INFO("Admin : Already created."))
            return False

        self.user_class.objects.create_superuser(
            email=os.getenv("ADMIN_EMAIL"),
            password=os.getenv("ADMIN_PASSWORD"),
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Created {} admin account.".format(os.getenv("ADMIN_EMAIL"))
            )
        )