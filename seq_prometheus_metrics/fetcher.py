import json

from satella.coding.concurrent import TerminableThread
import time
import logging
import datetime
import requests

from .app import MetricData
from .settings import SEQ_ADDRESS, SEQ_API_KEY


logger = logging.getLogger(__name__)


class FetcherThread(TerminableThread):
    def get_exported_data(self) -> dict:
        if SEQ_API_KEY is None:
            headers = {}
        else:
            headers = {'X-Seq-ApiKey': SEQ_API_KEY}
        try:
            req = requests.get(SEQ_ADDRESS+'api/diagnostics/metrics', headers=headers)
        except requests.exceptions.RequestException:
            logger.warning('Failure obtaining metrics')
            return {'up': 0}

        if req.status_code != 200:
            logger.warning(f'Bad status code from seq, {req.status_code} seen')
            return {'up': 0}

        try:
            data = req.json()
        except json.decoder.JSONDecodeError:
            logger.warning('Got invalid JSON', extra={'content': req.text})
            return {'up': 0}

        exported_data = {'up': 1}
        for key, value in data.items():
            if isinstance(value, (int, float)):
                exported_data[key] = value
            elif isinstance(value, str):
                try:
                    date = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
                except ValueError:
                    continue
                else:
                    exported_data[key] = date.timestamp()

        return exported_data

    def loop(self) -> None:
        exported_data = self.get_exported_data()
        MetricData().update_data(exported_data)

        for i in range(5):
            time.sleep(5)
            if self._terminating:
                return
