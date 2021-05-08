from typing import Union

import requests
from fake_useragent import UserAgent
from requests.exceptions import HTTPError
from datetime import datetime

from app.constants import Constants
# from constants import Constants

def today() -> str:
    return datetime.now().strftime(Constants.DD_MM_YYYY)

def _callApi(url: str) -> Union[HTTPError, dict]:
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise e

    return response.json()

def getavailabilitybypincode(pinCode: str, date: str = today(), minAgeLimit: int = None):
    url = f"{Constants.AVAILABILITY_BY_PIN_CODE_URL}?pincode={pinCode}&date={date}"
    return _callApi(url)
    # return filter_centers_by_age_limit(self._call_api(url), min_age_limt) if min_age_limt else self._call_api(url)

# print(getavailabilitybypincode('560077','09-05-2021'))