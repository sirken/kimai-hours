# kimai-hours
Returns the total number of timesheet hours today. 

Uses `kimai-python` library https://github.com/kbancerz/kimai-python

## config.json
Add your details to config.json. Create an API token in the web GUI under `User > Profile > API`

    {
      "user": "Username",
      "token": "API_token",
      "server": "https://server"
    }

## setup
    # set script as executable
    chmod u+x kimai-hours.sh

## run
    ./kimai-hours.sh