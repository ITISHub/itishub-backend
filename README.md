# ITIS HUB Backend🐱‍👤
## Configuration

Just create  _**.env**_   file in folder , where is located settings.py file and add following lines:
```
SECRET_KEY=             # some string secret key for django project
DB_NAME=                # your postgresDB name
DB_USER=                # your postgresDB username
DB_PASSWORD=            # your postgresDB user password
DB_HOST=                # your postgresDB host
DB_PORT=                # your postgresDB port
EMAIL_HOST_USER=        # your smtp hostmail login
EMAIL_HOST_PASSWORD=    # your smtp hostmail password
EMAIL_CONSUMER=         # email consumer (our itishub mail :) )

```
Also install all requirement modules from **requirements.txt** and make all migrations 

#### _Don't forget to run PostgresDB server !_

## :trollface: 16.08.2020: moved from PostgresDB to SQLITE3! :trollface:
