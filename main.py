import json
import kimai_python
from kimai_python.rest import ApiException
from datetime import datetime, timedelta

with open('config.json', 'r') as f:
    config = json.load(f)

configuration = kimai_python.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = config['token']
configuration.api_key['X-AUTH-USER'] = config['user']
configuration.host = config['server']

api_instance = kimai_python.TimesheetApi(kimai_python.ApiClient(configuration))
today = datetime.today().strftime('%Y-%m-%dT00:00:00')


def total_hours_today():
    try:
        api_response = api_instance.api_timesheets_get(modified_after=today)
        # print(api_response)
        total_seconds = 0
        for timesheet in api_response:
            # completed entries with final duration (seconds)
            if timesheet.duration:
                total_seconds += timesheet.duration
            # started active entry with 'begin' value only
            else:
                # calculate time from when this entry began until now
                total_seconds += (datetime.astimezone(datetime.now(tz=None)) - timesheet.begin).total_seconds()
        return str(timedelta(seconds=total_seconds))[:-3]
    except ApiException as e:
        print(f"Exception when calling api_timesheets_get: {e}\n")


if __name__ == '__main__':
    print(total_hours_today())
