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
        project_name = ''
        for timesheet in api_response:
            # completed entries with final duration (seconds)
            if timesheet.duration:
                total_seconds += timesheet.duration
            # started active entry with 'begin' value only
            else:
                # calculate time from when this entry began until now
                total_seconds += (datetime.astimezone(datetime.now(tz=None)) - timesheet.begin).total_seconds()
                project_id = f'{timesheet.project}'
                try:
                    api_project = kimai_python.ProjectApi(kimai_python.ApiClient(configuration))
                    project = api_project.api_projects_id_get(project_id)
                    project_name = f'{project.name[:5]}-'
                except ApiException as e:
                    print(f"Exception when calling api_projects_id_get: {e}\n")
        hr_min_sec = str(timedelta(seconds=total_seconds)).split(':')
        # return hours and minutes only
        return f'{project_name}{hr_min_sec[0]}:{hr_min_sec[1]}'
    except ApiException as e:
        print(f"Exception when calling api_timesheets_get: {e}\n")


if __name__ == '__main__':
    print(total_hours_today())
