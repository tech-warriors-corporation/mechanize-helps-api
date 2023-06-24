# mechanize-helps-api
Microservice of Helps for Mechanize (API).

## About
- Read the [architecture](https://github.com/tech-warriors-corporation/mechanize-api#architecture) project;
- Database name is _mechanize_helps_;
- Prefix in routes should be **/api/helps**.

## Setup
Create a `.env` file with `DB_ENV`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME_REMOTE`, `DB_USER_REMOTE`, `DB_PASSWORD_REMOTE`, `DB_HOST_REMOTE`, `DB_PORT_REMOTE`, `CLIENT_ID`, `ACCOUNTS_API_URL`, `NOMINATIM_API_URL` and `GOOGLE_MAPS_URL` variables to work.

## Installing
Use `pip install -r requirements.txt` to install dependencies.

## Start
Run `python -m app` to start project.
