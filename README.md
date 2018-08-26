# ImpaktWebsite
Repository for the Impakt Website and API

# Setup
1. Create a new project directory
    `mkdir -p ~/Projects/ImpaktWebsite`
    `cd ~/Projects/ImpaktWebsite`
2. Create and activate virtual environment for the project
    `python3 -m venv venv`
    `source venv/bin/activate`
3. Install project requirements
    `pip install -r requirements.txt`
4. Install postgresql locally (instructions varying depending on platform)
5. Configure your local postgres database. Replace "myname" with... your name.
    `sudo su - postgres`
    `psql`
    `CREATE USER myname;`
    `ALTER USER myname WITH SUPERUSER;`
    `ALTER GROUP postgres ADD USER myname;`
    `ALTER USER myname WITH PASSWORD 'mypassword';`
6. Create a config.py file to store project credentials. The file is in the project gitignore, but take care to never commit this file to Git.
    `cp impakt/settings/sample_config.py impakt/settings/config.py`
    `nano impakt/settings/config.py`
7. Install node and npm for frontend dependency and build process management.
8. Install frontend dependencies
    `npm install`
9. Run project migrations
    `python manage.py migrate`
10. Run your local runserver and visit localhost:8000 to confirm that you're all set up!
    `python manage.py runserver`

And you're done!
