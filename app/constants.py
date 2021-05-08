class Constants:
    BASE_URL = "https://cdn-api.co-vin.in/api/v2"

    STATES_LIST_URL = f"{BASE_URL}/admin/location/states"
    DISTRICTS_LIST_URL = f"{BASE_URL}/admin/location/districts"

    AVAILABILITY_BY_PIN_CODE_URL = f"{BASE_URL}/appointment/sessions/public/calendarByPin"
    AVAILABILITY_BY_DISTRICT_URL = f"{BASE_URL}/appointment/sessions/public/calendarByDistrict"

    DD_MM_YYYY = "%d-%m-%Y"
