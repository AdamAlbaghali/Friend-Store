from app import app, db
from models import Friend

# Create sample data
friend1 = Friend(
    name="Alice",
    role="Developer",
    description="Loves coding",
    gender="Female",
    img_url="http://example.com/alice.jpg"
)

friend2 = Friend(
    name="Bob",
    role="Designer",
    description="Enjoys designing",
    gender="Male",
    img_url="http://example.com/bob.jpg"
)

# Use application context
with app.app_context():
    db.session.add(friend1)
    db.session.add(friend2)
    db.session.commit()

print("Sample data inserted successfully.")
