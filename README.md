# freelance-job-CLI-manager
A Powerfull CLI app for freelancers to manage freelancers, jobs, and payments . Ideal for tracking deadlines, updating job status and monitoring earnings.

##  Features

- View all freelancers, jobs, and payments
- Add new freelancers and assign jobs
- Mark jobs as completed
- Search jobs by title
- View total earnings for each freelancer
- Data persistence using SQLite and SQLAlchemy ORM

##  Project Structure

freelance-job-CLI-manager/
├── config.py # Database setup and session configuration
|__main.py     #acts as entry point when running cli
|__cli.py    #implements interactive command-line to interact with data
|
|__db/
│ ├── migrate.py # Creates database tables
│ └── seed.py # Provides the database with sample data
├── lib/
  |
  -models
│ ├── freelancer.py   # Freelancer model
│ ├──job.py  # Job model
│ |
│ └── payment.py # Payment model
└── README.md # Project documentation

##  Installation & Setup
-Youll need ubuntu/lynux

1. **Clone the repository by pasting the ssh key given for this repository in to your local machine -git clone "the ssh key"**

2. then cd in to the file created and do 'code .'

3. do pipenv install then pipenv shell to run in virtual environment


## License 
The project is licensed under the Apache License

## Author
- Built and owned by Rotich Jared

## Running the App
python3 then the specific file   -i.e python3 db/seed.py to run seed.py



