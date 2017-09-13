
import copy
import json
import logging
import datetime

import requests

from cisco_api.utilities.dot_dict import DotDict


logger = logging.getLogger(__name__)

class BaseApi(object):
    _token_url = 'https://cloudsso.cisco.com/as/token.oauth2'
    _username = None
    _password = None

    def __init__(self):
        self._session = requests.Session()

    def _get_headers(self):
        if not hasattr(self, '_headers'):
            logger.debug('Building request headers')
            token = self._get_token()
            self._headers = {
                'Accept': 'application/json',
                'Authorization': f'{token.type} {token.access}'
            }
        return self._headers

    def _get_token(self):
        if not hasattr(self, '_token'):
            logger.debug('Authenticating')
            params = {
                'client_id': self._username,
                'client_secret': self._password
            }
            data = {'grant_type': 'client_credentials'}

            logger.debug(f'POST {self._token_url}')
            logger.debug(f'data {data}')
            response = self._session.post(
                self._token_url,
                params=params,
                data=data,
            )
            response.raise_for_status()
            logger.debug(response.text.strip())
            data = response.json()
            self._token = DotDict({
                'access': data['access_token'],
                'type': data['token_type'],
                'expires': data['expires_in'],
            })
            logger.debug('Access Token Retrieved')
        return self._token

    def _get(self, url, params=None):
        headers = self._get_headers()
        logger.debug(f'GET {url}')
        logger.debug(f'headers: {headers}')
        request_params = copy.deepcopy(self._base_params)
        params = params or dict()
        request_params.update(params)
        response = self._session.get(
            url,
            headers=headers,
            params=request_params,
        )
        response.raise_for_status()
        data = response.json()
        pretty_data = json.dumps(data, indent=4, sort_keys=True)
        logger.debug(f'Response: {pretty_data}')
        return DotDict(data)
