
import asyncio
from contextlib import closing

import logging

from cisco_support_api.eox.async_eox import AsyncEox

logger = logging.getLogger(__name__)


class Eox:
    def __init__(self):
        self._api = AsyncEox()

    def by_date(self, start_date, end_date):
        with closing(asyncio.get_event_loop()) as loop:
            return loop.run_until_complete(
                self._api.by_date(start_date, end_date)
            )

    def by_product(self, product_id):
        with closing(asyncio.get_event_loop()) as loop:
            return loop.run_until_complete(
                self._api.by_product(product_id)
            )

    def by_serial(self, serial):
        with closing(asyncio.get_event_loop()) as loop:
            return loop.run_until_complete(
                self._api.by_serial(serial)
            )

    def list(self):
        with closing(asyncio.get_event_loop()) as loop:
            return loop.run_until_complete(
                self._api.list()
            )
