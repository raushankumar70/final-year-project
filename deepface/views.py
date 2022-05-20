from http.client import HTTPResponse
import mysql.connector
from django.shortcuts import render
import cv2
import matplotlib.pyplot as plt
#from deepface import DeepFace
from tkinter import filedialog
from random import randint
import os , cv2
# db=mysql.connector.connect(host="localhost",user="root",password="1234",database="deepface")
# cur=db.cursor()
# Create your views here.
def index(request):  
    return render(request,"index.html")

def home(request):
    user_=request.GET["user"]
    pwd_=request.GET['pwd']
    
    return render(request,"camera.html")

def cam():
    cap=cv2.VideoCapture(0)
    ret,img=cap.read()
    cv2.imshow('webcam',img)
    k=cv2.waitKey(10)
    cap.release()
    cv2.destroyAllWindows()
    return img[:,:,::-1]

def camera_setting(request):
    img=cam()
    y=randint(1000000,2000000)
    file="upload/"+str(y)+".png"
    cv2.imwrite(file, img) 
    return render(request,"analysis.html")







