This application defines the API endpoint /countries to manage the list of countries. It handles two different kinds of
 requests:

    GET /countries returns the list of countries.
    POST /countries adds a new country to the list.

This Flask application includes functions to handle only two types of requests to the API endpoint, /countries.

In a full REST API, you’d want to expand this to include functions for all the required operations.

Source:
```
https://realpython.com/api-integration-in-python/#rest-and-python-tools-of-the-trade
```


### Project Structure:
```
│
├── README.md                             # This file
├── app.py                                # API Flask
├── request.py                            # python file to send request to the local API
```

To Run the API:
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
````