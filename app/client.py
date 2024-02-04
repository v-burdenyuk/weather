import logging
import requests
from requests import Response

logger = logging.getLogger(__name__)


class BaseAPIException(Exception):
    pass


class APIClient:
    default_header = {"Content-Type": "application/json"}
    fail_message = "Request failed"
    exception_class = BaseAPIException

    def request(self, method, url, json=None, parameters=None, headers=None) -> Response:
        if headers is None:
            headers = {}

        try:
            response = requests.request(
                method=method,
                url=url,
                json=json,
                params=parameters,
                headers=dict(headers, **self.default_header),
            )
            if not response.ok:
                logger.warning(self.fail_message)
                logger.warning(response.text)
                return

            return response

        except requests.exceptions.RequestException as error:
            logger.warning(error)
            return
