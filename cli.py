import sys
from datetime import datetime
from config import Session
from lib.models.freelancer import Freelancer
from lib.models.job import Job
from lib.models.payment import Payment

def main_menu():
    print("\n FREELANCE JOB MANAGER")
    print("-" * 30)
    print("1. View all freelancers")
    print("2. View all jobs")
    print("3. View all payments")
    print("4. Add a new freelancer")
    print("5. Add a new job")
    print("6. Mark job as completed")
    print("7. Search Jobs")
    print("8. Update Job Status")
    print("9. Total Earnings per Freelancer")
    print("10. Exit")

def get_session():
    return Session()

def view_freelancers():
    session = get_session()
    freelancers = session.query(Freelancer).all()
    for f in freelancers:
        print(f"\n ID: {f.id} | Name: {f.name} | Skills: {f.skills}")
    session.close()

def view_jobs():
    session = get_session()
    jobs = session.query(Job).all()
    for j in jobs:
        print(f"\n ID: {j.id} | Title: {j.title} | Deadline: {j.deadline} | Status: {j.status} | Freelancer: {j.freelancer.name}")
    session.close()

def view_payments():
    session = get_session()
    payments = session.query(Payment).all()
    for p in payments:
        print(f"\n ID: {p.id} | Amount: ${p.amount:.2f} | Job: {p.job.title} | Freelancer: {p.job.freelancer.name}")
    session.close()

def add_freelancer():
    session = get_session()
    try:
        name = input("Enter name: ").strip()
        if not name:
            print("❌ Name cannot be empty!")
            return

        if session.query(Freelancer).filter(Freelancer.name == name).first():
            print("❌ Freelancer already exists!")
            return

        skills = input("Enter skills: ").strip()
        freelancer = Freelancer(name=name, skills=skills)
        session.add(freelancer)
        session.commit()
        print("✅ Freelancer added.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
    finally:
        session.close()

def add_job():
    session = get_session()
    try:
        title = input("Enter job title: ").strip()
        if not title:
            print("❌ Title cannot be empty!")
            return
            
        deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid date format! Use YYYY-MM-DD")
            return
            
        freelancer_id = input("Enter freelancer ID: ").strip()
        if not freelancer_id.isdigit():
            print("❌ Invalid freelancer ID!")
            return
            
        freelancer = session.query(Freelancer).get(int(freelancer_id))
        if not freelancer:
            print("❌ Freelancer not found!")
            return
            
        job = Job(
            title=title,
            deadline=deadline,
            status="pending",
            freelancer=freelancer
        )
        session.add(job)
        session.commit()
        print("✅ Job added successfully!")
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
    finally:
        session.close()

def complete_job():
    session = get_session()
    try:
        job_id = input("Enter job ID to mark as completed: ").strip()
        if not job_id.isdigit():
            print("❌ Invalid job ID!")
            return

        job = session.query(Job).get(int(job_id))
        if job:
            job.status = "completed"
            session.commit()
            print("✅ Job marked as completed.")
        else:
            print("❌ Job not found.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
    finally:
        session.close()

def search_jobs():
    session = get_session()
    keyword = input("Search by title or status: ").strip().lower()
    jobs = session.query(Job).filter(
        (Job.title.ilike(f"%{keyword}%")) | 
        (Job.status.ilike(f"%{keyword}%"))
    ).all()

    if jobs:
        print(f"\nFound {len(jobs)} job(s):")
        for j in jobs:
            print(f" {j.title} | Status: {j.status} | Freelancer: {j.freelancer.name}")
    else:
        print("❌ No matching jobs found.")
    session.close()

def update_job_status():
    session = get_session()
    try:
        job_id = input("Enter job ID to update: ").strip()
        if not job_id.isdigit():
            print("❌ Invalid job ID!")
            return

        job = session.query(Job).get(int(job_id))
        if job:
            print(f"\nCurrent status: {job.status}")
            print("Available statuses: pending, in progress, completed")
            new_status = input("Enter new status: ").strip().lower()
            if new_status in ["pending", "in progress", "completed"]:
                job.status = new_status
                session.commit()
                print("✅ Job status updated.")
            else:
                print("❌ Invalid status!")
        else:
            print("❌ Job not found.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
    finally:
        session.close()

def total_earnings():
    session = get_session()
    freelancers = session.query(Freelancer).all()
    for f in freelancers:
        print(f"\n{f.name} | Total Earnings: ${f.total_earnings():.2f}")
    session.close()

def run():
    while True:
        main_menu()
        choice = input("\nChoose an option (1-10): ").strip()
        
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
            search_jobs()
        elif choice == "8":
            update_job_status()
        elif choice == "9":
            total_earnings()
        elif choice == "10":
            print("👋 Exiting...")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    run()