import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\Ruler\\Downloads\\service.json")
firebase_admin.initialize_app(cred)

web_api_key = 'AIzaSyDVNdZJORJE9_g4fUWSVwiub1KBtwqhf-c'