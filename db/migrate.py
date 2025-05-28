import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import Base, engine
from lib.models.freelancer import Freelancer
from lib.models.job import Job
from lib.models.payment import Payment

Base.metadata.create_all(engine)
print("✅ Tables created successfully!")
