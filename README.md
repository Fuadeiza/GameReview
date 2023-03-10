# GameReview

The backend API of a video game review website with token authentication and permissions for diffrent users.


## Getting Started

To get started, go the directory on your computer where you want to install this
repository using the command line. Type the following in the command line:

- Create a virtual environment : `python3 venv venv` (if you do not have virtualenv installed here is a link to a github gist(https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
- Activate virtualenv: `source venv/bin/activate` (or equivalent for your OS Shell)

Clone the repo `git clone https://github.com/Fuadeiza/GameReview`

- Install the required package: `pip install -r requirements.txt`
- Install the `pre-commit` hooks: `pre-commit install`

To run the project, make sure youre in the same directoy as the `manage.py` file.

- Create the database by migrating using: `python3 manage.py migrate`

- Then run: `python3 manage.py runserver`


Goodluck ✌️✌️✌️
