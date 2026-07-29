import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from firebase_config import db

db.collection("contacts").document("001").set({
    "name": "Mohammed Faiz",
    "phone": "9876543210",
    "email": "faiz@example.com"
})

print("✅ Firebase Connected Successfully!")