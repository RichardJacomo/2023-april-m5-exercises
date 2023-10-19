from django.core.management.base import BaseCommand, CommandParser
from accounts.models import Account
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create random users"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "amount", type=int, help="Amount of users will be created"
        )

        parser.add_argument(
            "-p", "--prefix", type=str, help="Define username prefix"
        )
        # creates --super_user field in the command
        parser.add_argument(
            "-su", "--super_user", type=bool, help="Define users as admin"
        )

    # creates 4 users with random name

    def handle(self, *args: tuple, **options: dict) -> str | None:
        amount = options.get("amount")
        prefix = options.get("prefix")
        # get the --super_user in the command
        super_user = options.get("super_user")

        for i in range(amount):
            if prefix:
                username = f"{prefix}_{get_random_string(5)}"
            else: 
                username = get_random_string(5)
            if super_user:  # verify if --super_user is True
                # creates a super user
                Account.objects.create_superuser(username=username, password="1234")
            else:
                Account.objects.create_user(username=username, password="1234")    