"""
Django command to wait for the database to be available.
"""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database to be available."""

    def handle(self, *args, **kargs):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                # Attempt to connect to the database
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database not available, waiting 1 second...")
                self.stdout.flush()
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
