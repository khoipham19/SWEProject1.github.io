from flask import Flask, render_template, request, redirect, url_for
import pyrebase



firebaseConfig = {
  "apiKey": "AIzaSyCzEocPUOnDcarC0oQu_6_VK-rukqDyEiU",
  "authDomain": "fridge-42574.firebaseapp.com",
  "projectId": "fridge-42574",
  "storageBucket": "fridge-42574.appspot.com",
  "messagingSenderId": "461258862353",
  "appId": "1:461258862353:web:a76aa7d322077ef08ee6b0",
  "measurementId": "G-NHZ6J76QM0",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()




def signup(email, password):
        try:
            user = auth.create_user_with_email_and_password(email, password)
        except:
            return "Registration failed"


def login(email, password):
      try:
         login = auth.sign_in_with_email_and_password(email, password)
         print("Successfully logged in!")
      except:
         print("Invalid email or password")
