# Flask Demo Web App with Auth0

This application is a sample on how to integrate Auth0 for authentication in a Flask web application using APIRouter and module separation.

## How to run the server

1. Clone this repository:

```sh
git clone https://github.com/jtemporal/flask-to-fastapi.git && cd flask-webapp
```

2. Create [your free Auth0 account here](https://a0.to/plg_signup).

3. Create a [Regular Web Application](https://auth0.com/docs/get-started/auth0-overview/create-applications/regular-web-apps) in the [Auth0 Dashboard](https://manage.auth0.com/#/applications).

4. Create a `.config` file from `.config.example` and populate the values from your Auth0 Application:

```sh
cp .config.example .config
```

5. Create a secret key and populate the corresponding value on the `.config` file:

```sh
python3 -c "import secrets; print(secrets.token_hex(32))"
```

6. Create a virtual environment and install dependencies
   
```sh
# Create a venv
python3 -m venv .env 

# Activate
source .env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

7. Start the server

```sh
flask --app app run --port 4040 --reload
```
   
8. Visit [`http://localhost:4040/`](http://localhost:4040/) to access the starter web application.

----


[Find Jess on the web anywhere](https://jtemporal.com/socials).

[Sign up for Auth0's developer newsletter here](https://a0.to/nl-signup/python).