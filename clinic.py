from tkinter import *
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import ImageTk, Image

# Set up email server connection
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'clinicmanagementvit@gmail.com'
password = 'jrczihcgkzeoxqgx'
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aryan123",
  database="miniproject"
)
mycursor = mydb.cursor()

class Clinic:
    def __init__(self,root):
        self.root=root
        self.root.configure(bg="yellow")
        self.root.title("Clinic Management System")
        self.root.geometry("1500x800+0+0")
        
        lblTitle=Label(self.root,bd=20,relief=RIDGE,text="CLINIC MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lblTitle.pack(side=TOP,fill=X)
        image1 = Image.open('C:/Users/ARYAN/OneDrive/Desktop/4th sem miniproject/image1.png')
        image1 = image1.resize((300, 400), resample=Image.LANCZOS)
        tk_image1 = ImageTk.PhotoImage(image1)
        imglabel1 = Label(self.root, image=tk_image1)
        imglabel1.image=tk_image1
        imglabel1.place(x=50,y=150)
        tk_image2 = ImageTk.PhotoImage(image1)
        imglabel2 = Label(self.root, image=tk_image2)
        imglabel2.image=tk_image2
        imglabel2.place(x=950,y=150)

        image2 = Image.open('C:/Users/ARYAN/OneDrive/Desktop/4th sem miniproject/image2.png')
        image2 = image2.resize((75, 75), resample=Image.LANCZOS)
        tk_image3 = ImageTk.PhotoImage(image2)
        imglabel3 = Label(self.root, image=tk_image3)
        imglabel3.image=tk_image3
        imglabel3.place(x=20,y=20)

        tk_image4 = ImageTk.PhotoImage(image2)
        imglabel4 = Label(self.root, image=tk_image4)
        imglabel4.image=tk_image4
        imglabel4.place(x=1190,y=20)


        self.loginframe=Frame(self.root,bd=15,padx=20,relief=RIDGE,bg="white")
        self.loginframe.place(x=500,y=150,width=300,height=180)
        
        self.admin_button = Button(self.loginframe, text="Admin Login",bg="khaki", font=("Arial", 16),command=self.show_admin_login_frame).grid(row=1,column=0,padx=10,pady=4)
        self.patient_button = Button(self.loginframe, text="Patient Login",bg="khaki", font=("Arial", 16),command=self.show_patient_login_frame).grid(row=2,column=0,padx=10,pady=4)
        self.signup_button = Button(self.loginframe, text="New User? Sign Up",bg="khaki", font=("Arial", 16),command=self.show_sign_up_frame).grid(row=3,column=0,padx=10,pady=4)
    
    
    
    
    def show_admin_login_frame(self):
          # Hide the welcome frame
          
    
          # Create the admin login frame
          self.admin_login_frame = Frame(self.root,bd=20,padx=20,relief=RIDGE,bg="skyblue")
          self.admin_login_frame.place(x=500,y=150,width=300,height=180)
          self.admin_password=Label(self.admin_login_frame, text="Enter password:",bg="skyblue").grid(row=0,column=1,padx=20,pady=10)
          self.password_entry = Entry(self.admin_login_frame, show="*")
          self.password_entry.grid(row=1,column=1,padx=4,pady=10)
    
          def check_password():
           if self.password_entry.get() == "admin":
            # Show a message and open the admin frame
            messagebox.showinfo("Welcome admin!", "Password correct!")
            self.show_admin_frame()
           else:
            # Show an error message
            messagebox.showerror("Error", "Incorrect password!")
    
          # Create a login button
          self.login_button = Button(self.admin_login_frame, text="Login",bg="khaki", command=check_password)
          self.login_button.grid(row=2,column=0,padx=4,pady=5)
          def close():
             self.admin_login_frame.destroy()
          self.close_button = Button(self.admin_login_frame,text="Close",bg="khaki",command=close)
          self.close_button.grid(row=2,column=2,padx=4,pady=5)
    def show_patient_login_frame(self):
        # Hide the welcome frame
        
    
        # Create the patient login frame
        self.patient_login_frame = Frame(self.root,bd=20,padx=20,relief=RIDGE,bg="skyblue")
        self.patient_login_frame.place(x=500,y=150,width=300,height=180)
        self.mobile_number=Label(self.patient_login_frame, text="Mobile Number:").grid(row=0,column=0,padx=5,pady=12)
        self.mobile_number_entry = Entry(self.patient_login_frame)
        self.mobile_number_entry.grid(row=0,column=1,padx=5,pady=12)
        self.patient_password=Label(self.patient_login_frame, text="Password:").grid(row=1,column=0,padx=5,pady=12)
        self.password_entry = Entry(self.patient_login_frame, show="*")
        self.password_entry.grid(row=1,column=1,padx=5,pady=12)
    
        # Create a function to check the login credentials
        def check_login():
           # Fetch the patient record from the database
           mycursor.execute("SELECT * FROM patient_records WHERE mobile_number = %s AND password = %s", (self.mobile_number_entry.get(), self.password_entry.get()))
           patient = mycursor.fetchone()
           if patient:
            # Show a message and open the patient frame
            messagebox.showinfo("Login Successful", "Welcome " + patient[0] + "!")
            self.show_patient_frame()
           else:
             # Show an error message
             messagebox.showerror("Error", "Invalid mobile number or password!")
    
           # Create a login button
        self.login_button = Button(self.patient_login_frame, text="Login",bg="khaki", command=check_login)
        self.login_button.grid(row=2,column=0,padx=5,pady=12)
        def close():
          self.patient_login_frame.destroy()
        self.close_button = Button(self.patient_login_frame,text="Close",bg="khaki",command=close)
        self.close_button.grid(row=2,column=1,padx=5,pady=12)
    
    def show_sign_up_frame(self):
       # Hide the welcome frame
       
    
       # Create the sign up frame
       self.sign_up_frame = Frame(self.root,bd=20,padx=20,relief=RIDGE,bg="skyblue")
       self.sign_up_frame.place(x=500,y=150,width=300,height=180)
       self.signup_name=Label(self.sign_up_frame, text="Fullname:",bg="skyblue").grid(row=0, column=0)
       self.full_name_entry = Entry(self.sign_up_frame)
       self.full_name_entry.grid(row=0, column=1)
       self.signup_mobile=Label(self.sign_up_frame, text="Mobile Number:",bg="skyblue").grid(row=1, column=0)
       self.mobile_number_entry = Entry(self.sign_up_frame)
       self.mobile_number_entry.grid(row=1, column=1)
       self.signup_email=Label(self.sign_up_frame, text="Email ID:",bg="skyblue").grid(row=2, column=0)
       self.email_entry = Entry(self.sign_up_frame)
       self.email_entry.grid(row=2, column=1)
       self.signup_city=Label(self.sign_up_frame, text="City:",bg="skyblue").grid(row=3, column=0)
       self.city_entry = Entry(self.sign_up_frame)
       self.city_entry.grid(row=3, column=1)
       self.signup_pass=Label(self.sign_up_frame, text="Password:",bg="skyblue").grid(row=4, column=0)
       self.password_entry = Entry(self.sign_up_frame, show="*")
       self.password_entry.grid(row=4, column=1)
       # Create a function to sign up the user
       def sign_up():
           # Check if the mobile number already exists in the database
           mycursor.execute("SELECT * FROM patient_records WHERE mobile_number = %s", (self.mobile_number_entry.get(),))
           patient = mycursor.fetchone()
           if patient:
             # Show an error message
             messagebox.showerror("Error", "Mobile number already exists!")
           else:
             # Insert the patient record into the database
             sql = "INSERT INTO patient_records (full_name, mobile_number, email, city, password) VALUES (%s, %s, %s, %s, %s)"
             val = (self.full_name_entry.get(), self.mobile_number_entry.get(), self.email_entry.get(), self.city_entry.get(), self.password_entry.get())
             mycursor.execute(sql, val)
             mydb.commit()
             # Compose email
             from_email = 'clinicmanagementvit@gmail.com'
             to_email = self.email_entry.get()
             subject = 'Successful sign-up '
             body = f'You have successfully created an account in clinic management system.Your registered mobile number is {self.mobile_number_entry.get()} and password is {self.password_entry.get()}.Please note it for future reference.'
             msg = MIMEMultipart()
             msg['From'] = from_email
             msg['To'] = to_email
             msg['Subject'] = subject
             msg.attach(MIMEText(body, 'plain'))
             # Send email
             text = msg.as_string()
             server.sendmail(from_email, to_email, text)
             # Close server connection
             server.quit()
             # Show a message and open the patient frame
             messagebox.showinfo("Sign Up Successful", "Sign up successful!")
             self.sign_up_frame.destroy()
       
       
       # Create a sign up button
       self.sign_up_button = Button(self.sign_up_frame, text="Sign Up",bg="khaki", command=sign_up)
       self.sign_up_button.grid(row=5, column=0)
       def close():
          self.sign_up_frame.destroy()
       self.close_button = Button(self.sign_up_frame,text="Close",bg="khaki",command=close)
       self.close_button.grid(row=5,column=1)


    def show_admin_frame(self):
        for widget in root.winfo_children():
            widget.pack_forget()
        lblTitle=Label(self.root,bd=20,relief=RIDGE,text="CLINIC MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lblTitle.pack(side=TOP,fill=X)
        # Create the admin frame
        self.admin_frame = Frame(self.root,bd=20,padx=20,relief=RIDGE,bg="lime")
        self.admin_frame.place(x=500,y=150,width=300,height=180)
        # Create a function to see today's appointments
        def see_appointments():
          # Fetch the appointments for today
          mycursor.execute("SELECT mobile_number,patient_name,date,slot FROM appointments WHERE date = CURDATE()")
          appointments = mycursor.fetchall()
          if appointments:
            # Create a message with the appointments
            message = ""
            for appointment in appointments:
               message += appointment[1] + " - " + appointment[2] + "\n"
            # Show the message
            messagebox.showinfo("Today's Appointments", message)
          else:
            # Show a message if there are no appointments
            messagebox.showinfo("Today's Appointments", "No appointments today!")
        # Create a button to see today's appointments
        see_appointments_button = Button(self.admin_frame, text="See Today's Appointments",bg='khaki', command=see_appointments)
        see_appointments_button.pack(padx=10,pady=10)

        # Create a function to give a prescription
        def give_prescription():
            # Create the prescription frame
            prescription_frame = Frame(self.root,bd=20,padx=20,relief=RIDGE,bg="lime")
            prescription_frame.place(x=500,y=400,width=400,height=230)
            # Create a label and entry for the mobile number
            mobile=Label(prescription_frame, text="Mobile Number:",bg="lime").grid(row=0, column=0,pady=20)
            mobile_number_entry = Entry(prescription_frame)
            mobile_number_entry.grid(row=0, column=1,pady=20)
    
            # Create a label and entry for the prescription
            prescription=Label(prescription_frame, text="Prescription:",bg="lime").grid(row=1, column=0,pady=20)
            prescription_entry = Entry(prescription_frame)
            prescription_entry.grid(row=1, column=1,pady=20)
    
            # Create a function to give the prescription
            def submit_prescription():
                # Check if the mobile number exists in the database
                mycursor.execute("SELECT * FROM patient_records WHERE mobile_number = %s", (mobile_number_entry.get(),))
                patient = mycursor.fetchone()
        
                if patient:
                   # Insert the prescription into the database
                    sql = "INSERT INTO prescriptions (mobile_number, prescription) VALUES (%s, %s)"
                    val = (mobile_number_entry.get(), prescription_entry.get())
                    mycursor.execute(sql, val)
                    mydb.commit()
            
                    # Show a message and go back to the admin frame
                    messagebox.showinfo("Prescription Submitted", "Prescription submitted!")
                    prescription_frame.destroy()
                else:
                    # Show an error message if the mobile number is not in the database
                    messagebox.showerror("Error", "Mobile number not found!")
            def close():
                    prescription_frame.destroy() 
            # Create a button to submit the prescription
            submit_prescription_button = Button(prescription_frame, text="Submit Prescription",bg="khaki", command=submit_prescription)
            submit_prescription_button.grid(row=2,column=0,padx=20,pady=15)
            close_button = Button(prescription_frame,text="Close",bg="khaki",command=close)
            close_button.grid(row=2,column=1,padx=20,pady=15)
            
        def admin_logout():
            self.admin_frame.destroy()
            self.admin_login_frame.destroy()
           
        
        # Create a button to give a prescription
        give_prescription_button = Button(self.admin_frame, text="Give Prescription",bg='khaki', command=give_prescription)
        give_prescription_button.pack(padx=10,pady=10)  
        admin_logout_button = Button(self.admin_frame, text="Logout",bg='khaki', command=admin_logout)
        admin_logout_button.pack(side="bottom", pady=10)
         

    def show_patient_frame(self):
        # Hide the previous frame
        for widget in root.winfo_children():
            widget.pack_forget()
        lblTitle=Label(self.root,bd=20,relief=RIDGE,text="CLINIC MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lblTitle.pack(side=TOP,fill=X)
        self.patient_frame = Frame(self.root,bd=20,padx=20,relief=RIDGE,bg="lime")
        self.patient_frame.place(x=500,y=150,width=300,height=180)
        def generate_prescription():
           prescription_frame = Frame(self.root,bd=20,padx=20,relief=RIDGE,bg="lime")
           prescription_frame.place(x=400,y=350,width=400,height=300)
           mobile_label = Label(prescription_frame, text="Enter Mobile Number:",bg="lime")
           mobile_label.grid(row=0, column=0, padx=10, pady=10)

           # create an entry field for the mobile number
           mobile_entry = Entry(prescription_frame)
           mobile_entry.grid(row=0, column=1, padx=10, pady=10)
           prescription_listbox = Listbox(prescription_frame)
           prescription_listbox.grid(row=1,column=0,pady=10,padx=10)

           def fetch_prescriptions():
            # execute a SELECT query to fetch prescriptions for the given mobile number
             query = "SELECT prescription FROM prescriptions WHERE mobile_number=%s"
             values = (mobile_entry.get(),)
             mycursor.execute(query, values)
 
             # fetch all the rows from the query result
             rows = mycursor.fetchall()
             # display the list of prescriptions
           
             for row in rows:
               prescription_listbox.insert(END, row[0])
            
                      # create a button to fetch prescriptions
           fetch_button = Button(prescription_frame, text="Fetch Prescriptions",bg="khaki", command=fetch_prescriptions)
           fetch_button.grid(row=1, column=1,  padx=10, pady=10)
           # define function to close prescription frame and show patient frame
           def close_prescription_frame():
              prescription_frame.destroy()
              

           # create a button to close prescription frame
           close_button = Button(prescription_frame, text="Close",bg="khaki", command=close_prescription_frame)
           close_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        generate_prescription_button = Button(self.patient_frame, text="Generate Prescription",bg='khaki',command=generate_prescription)
        generate_prescription_button.pack(padx=10,pady=0)
        

        def book_appointment():
          book_appointment_frame=Frame(self.root,bd=20,padx=20,relief=RIDGE,bg="lime")
          book_appointment_frame.place(x=400,y=350,width=500,height=300) 
          today = datetime.date.today()
          date = today + datetime.timedelta(days=1)
          mobile_label = Label(book_appointment_frame, text="Enter Mobile Number:",bg="lime")
          mobile_label.grid(row=0, column=0, padx=10, pady=10)

            # create an entry field for the mobile number
          mobile_entry = Entry(book_appointment_frame)
          mobile_entry.grid(row=0, column=1, padx=10, pady=10)
          name_label=Label(book_appointment_frame,text="Enter Your name:",bg="lime")
          name_label.grid(row=1,column=0,padx=10,pady=10)
          name_entry =Entry(book_appointment_frame)
          name_entry.grid(row=1,column=1,padx=10,pady=10)
          available_slots = ["10:00 AM - 11:00 AM", "11:00 AM -  12:00 PM","12:00 PM -  1:00 PM", "1:00 PM -  2:00 PM","2:00 PM -  3:00 PM", "3:00 PM - 4:00 PM", "4:00 PM -  5:00 PM", "5:00 PM - 6:00 PM", "6:00 PM - 7:00 PM"]
          date_label=Label(book_appointment_frame,text="The date of appointment is:",bg="lime")
          date_label.grid(row=2,column=0,padx=10,pady=10)
          show_date=Label(book_appointment_frame,text=date,bg="lime")
          show_date.grid(row=2,column=1,padx=10,pady=10)
          selected_slot = StringVar(book_appointment_frame)
          selected_slot.set(available_slots[0])
          slot_label = Label(book_appointment_frame, text="Select Slot: ",bg="lime")
          slot_label.grid(row=3, column=0, padx=10, pady=10)
          slot_dropdown = OptionMenu(book_appointment_frame, selected_slot, *available_slots)
          slot_dropdown.grid(row=3, column=1, padx=10, pady=10)
          
          def book_slot():
            mobile = mobile_entry.get()
            name = name_entry.get()
            slot = selected_slot.get()
            mycursor.execute("SELECT email FROM patient_records where mobile_number=%s",(mobile,))
            email = mycursor.fetchone()
            recipient_email = email[0]
 
            # Check if slot is available
            mycursor.execute("SELECT * FROM appointments WHERE date=%s AND slot=%s", (date, slot))
            result = mycursor.fetchone()
            if result:
              messagebox.showerror("Error", "Slot not available!")
            else:
             
             # Compose email
             from_email = 'clinicmanagementvit@gmail.com'
             to_email = recipient_email
             subject = 'Appointment booking confirmation'
             body = f'Your appointment has been successfully booked for {date} at {slot}.'
             msg = MIMEMultipart()
             msg['From'] = from_email
             msg['To'] = to_email
             msg['Subject'] = subject
             msg.attach(MIMEText(body, 'plain'))
             # Send email
             text = msg.as_string()
             server.sendmail(from_email, to_email, text)
             # Close server connection
             server.quit()
             # Add appointment to database
             sql=("INSERT INTO appointments (mobile_number, patient_name, date, slot) VALUES (%s, %s, %s, %s)")
             val=(mobile, name, date, slot)
             mycursor.execute(sql,val)
             mydb.commit()
             messagebox.showinfo("Success", "Appointment booked successfully!")
            book_appointment_frame.destroy()
          def close():
             book_appointment_frame.destroy()
          close_button = Button(book_appointment_frame,text="Close",bg="khaki",command=close)
          close_button.grid(row=4,column=1,padx=10,pady=10)
          book_button = Button(book_appointment_frame, text="Book",bg="khaki", command=book_slot)
          book_button.grid(row=4, column=0, padx=10, pady=10)
        def patient_logout():
          self.patient_frame.destroy()
          self.patient_login_frame.destroy()
          

        book_appointment_button = Button(self.patient_frame, text="Book appointment",bg='khaki',command=book_appointment)
        book_appointment_button.pack(padx=10,pady=10)
        patient_logout_button = Button(self.patient_frame, text="Logout", command=patient_logout,bg='khaki')
        patient_logout_button.pack(side='bottom',pady=10)

       

        

root=Tk()
ob=Clinic(root)
root.mainloop()