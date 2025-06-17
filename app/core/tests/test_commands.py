"""Test custom django management commands."""

from unittest.mock import patch

from psycopg.errors import Psycopg2error  # type: ignore

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("app.core.management.commands.wait_for_db.Command.check")
class CommandTest(SimpleTestCase):
    """Test custom django management commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for dabatabase when it is available."""

        patched_check.return_value = True
        call_command("wait_for_db")
        patched_check.assert_called_once(database=["default"])

    # @patch("time.sleep")
    # def test_wait_for_db_delay(self, patched_sleep, patched_check):
    #     """Test waiting for database when it is not available."""

    #     patched_check.side_effect = (
    #         [Psycopg2error] * 2 + [OperationalError] * 3 + [True]
    #     )

    #     call_command("wait_for_db")

    #     self.assertEqual(patched_check.call_count, 6)

    #     patched_check.assert_called_with(database=["default"])
