# Migrating a Web Application from Flask to FastAPI: Avoiding Pitfalls

Have you ever had to migrate code from one stack to another? Migrating stacks on an application can be a daunting task. The secret is to keep changes to a small size and watch out for blind copy-and-paste.

Join me in this tutorial to learn the key differences between FastAPI and Flask plus how these differences will affect your stack migration.

Learn by doing it: migrate a simple Flask application to FastAPI. Learn how templates work in each framework, how you can use routers to create more complex applications in both Flask and FastAPI, and finally some tips if you are considering migrating from one to the other and vice-versa.

After this tutorial, you will feel confident to start your stack migrations between these two frameworks.

[This tutorial was made for EuroPython 2024](http://ep2024.europython.eu/session/migrating-a-web-application-from-flask-to-fastapi-avoiding-pitfalls).

## This Repo

This is a repo containing two web applications:
1. `flask-webapp`: Flask web application complete that will be used to migrate over to fastAPI;
1. `fastapi-webapp`: FastAPI starter application, this will be updated to work similarly to the Flask one.

Both applications count with an integration with [Auth0 by Okta, use this link to sign up](https://a0.to/plg_signup) and create your **free** account.

Note: They will run without the Auth0 setup but you'll be unable to login and follow the second half of the tutorial without it.

## Setup for the tutorial

You can either run this locally or on the cloud with GitHub Codespaces.

I recommend either connecting to the Codespace on VS Code on your machine using the [Codespaces VS Code extension](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) or run it locally to avoid problems with the auth integration.

### Pre-Reqs for the tutorial

1. [A free Auth0 account, click here to sign up](https://a0.to/plg_signup)
1. A clone of this repo locally or a Github Codespace;

<details>
<summary>If you want to be extra prepared</summary>
1. Go into the `flask-webapp/` create a python environment and install the requirements;
1. Go into the `fastapi-webapp/` create a python environment and install the requirements.
Both folders count with the detailed instructions on their perspective `README.md` files.
</details>

----

[Find Jess on the web anywhere](https://jtemporal.com/socials).

[Sign up for Auth0's developer newsletter here](https://a0.to/nl-signup/python).