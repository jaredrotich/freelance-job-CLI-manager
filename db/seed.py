import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import Session
from lib.models.freelancer import Freelancer
from lib.models.job import Job
from lib.models.payment import Payment
from datetime import date

# Start a database session
session = Session()


session.query(Payment).delete()
session.query(Job).delete()
session.query(Freelancer).delete()

# --------- FREELANCERS ----------
freelancer1 = Freelancer(name="Alice Mwangi", skills="Web Development, React, Django")
freelancer2 = Freelancer(name="Brian Otieno", skills="Graphic Design, Photoshop")
freelancer3 = Freelancer(name="Carol Wanjiku", skills="Mobile Development, Flutter")

# Add to session
session.add_all([freelancer1, freelancer2, freelancer3])
session.commit()

# --------- JOBS ----------
job1 = Job(title="Build E-commerce Website", deadline=date(2025, 6, 10), status="pending", freelancer=freelancer1)
job2 = Job(title="Design Logo and Brand Kit", deadline=date(2025, 6, 2), status="completed", freelancer=freelancer2)
job3 = Job(title="Create Mobile App", deadline=date(2025, 6, 20), status="in progress", freelancer=freelancer3)

# Add to session
session.add_all([job1, job2, job3])
session.commit()

# --------- PAYMENTS ----------
payment1 = Payment(amount=500.0, job=job1)
payment2 = Payment(amount=250.0, job=job2)
payment3 = Payment(amount=800.0, job=job3)

session.add_all([payment1, payment2, payment3])
session.commit()

print("✅ Dummy data seeded successfully!")
