import sys
from config import Session
from lib.models.freelancer import Freelancer
from lib.models.job import Job
from lib.models.payment import Payment

session = Session()

def main_menu():
    print("\n FREELANCE JOB MANAGER")
    print("-" * 30)
    print("1. View all freelancers")
    print("2. View all jobs")
    print("3. View all payments")
    print("4. Add a new freelancer")
    print("5. Add a new job")
    print("6. Mark job as completed")
    print("7. Exit")

def view_freelancers():
    freelancers = session.query(Freelancer).all()
    for f in freelancers:
        print(f"\n ID: {f.id} | Name: {f.name} | Skills: {f.skills}")

def view_jobs():
    jobs = session.query(Job).all()
    for j in jobs:
        print(f"\n ID: {j.id} | Title: {j.title} | Deadline: {j.deadline} | Completed: {j.is_completed} | Freelancer ID: {j.freelancer_id}")

def view_payments():
    payments = session.query(Payment).all()
    for p in payments:
        print(f"\n ID: {p.id} | Amount: ${p.amount} | Status: {p.status} | Job ID: {p.job_id}")

def add_freelancer():
    name = input("Enter name: ")
    skills = input("Enter skills: ")
    freelancer = Freelancer(name=name, skills=skills)
    session.add(freelancer)
    session.commit()
    print("✅ Freelancer added.")

def add_job():
    title = input("Enter job title: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    freelancer_id = input("Assign to freelancer ID: ")
    job = Job(title=title, deadline=deadline, freelancer_id=int(freelancer_id), is_completed=False)
    session.add(job)
    session.commit()
    print("✅ Job added.")

def complete_job():
    job_id = input("Enter job ID to mark as completed: ")
    job = session.query(Job).get(int(job_id))
    if job:
        job.is_completed = True
        session.commit()
        print("✅ Job marked as completed.")
    else:
        print("❌ Job not found.")

def run():
    while True:
        main_menu()
        choice = input("\nChoose an option: ")
        if choice == "1":
            view_freelancers()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            view_payments()
        elif choice == "4":
            add_freelancer()
        elif choice == "5":
            add_job()
        elif choice == "6":
            complete_job()
        elif choice == "7":
            print("👋 Exiting...")
            break
        else:
            print("❗ Invalid choice.")

if __name__ == "__main__":
    run()
