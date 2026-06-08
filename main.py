import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("anas-memory-book-firebase-adminsdk-fbsvc-5f3ee30c29.json")
firebase_admin.initialize_app(cred)
