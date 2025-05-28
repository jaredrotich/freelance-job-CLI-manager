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
|__main.py
|__cli.py
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

3. do pipenv install then pipenv shell to run in remote directory



