
import copy
import json
import logging
import datetime

import aiohttp

from cisco_api.utilities.dot_dict import DotDict


logger = logging.getLogger(__name__)

class BaseApi(object):
    _token_url = 'https://cloudsso.cisco.com/as/token.oauth2'
    _username = None
    _password = None

    def __init__(self):
        self._session = None

    async def _get_session(self):
        if self._session is None:
            self._session = aiohttp.ClientSession()
        return self._session

    async def _get_headers(self):
        if not hasattr(self, '_headers'):
            logger.debug('Building request headers')
            token = await self._get_token()
            self._headers = {
                'Accept': 'application/json',
                'Authorization': f'{token.type} {token.access}'
            }
        return self._headers

    async def _get_token(self):
        if not hasattr(self, '_token'):
            logger.debug('Authenticating')
            params = {
                'client_id': self._username,
                'client_secret': self._password
            }
            data = {'grant_type': 'client_credentials'}

            logger.debug(f'POST {self._token_url}')
            logger.debug(f'data {data}')
            session = await self._get_session()
            async with await session.post(self._token_url, params=params, data=data) as response:
                response.raise_for_status()
                data = await response.json()

            pretty_data = json.dumps(data, indent=4, sort_keys=True)
            logger.debug(f'Response: {pretty_data}')

            self._token = DotDict({
                'access': data['access_token'],
                'type': data['token_type'],
                'expires': data['expires_in'],
            })
            logger.debug('Access Token Retrieved')
        return self._token

    async def _get(self, url, params=None):
        headers = await self._get_headers()
        logger.debug(f'GET {url}')
        logger.debug(f'headers: {headers}')
        request_params = copy.deepcopy(self._base_params)
        params = params or dict()
        request_params.update(params)
        session = await self._get_session()
        async with session.get(url, headers=headers, params=request_params) as response:
            response.raise_for_status()
            data = await response.json()
        pretty_data = json.dumps(data, indent=4, sort_keys=True)
        logger.debug(f'Response: {pretty_data}')
        return DotDict(data)

    def __del__(self):
        if self._session is not None:
            self._session.close()