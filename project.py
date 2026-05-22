# import os # Yeh line top par honi chahiye

# # ... baki code ...

# class StudentPortal(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         # ...
        
#         # --- PATH LOGIC UPDATE ---
#         # Yeh line script ki location nikaalti hai
#         base_path = os.path.dirname(os.path.abspath(__file__))
#         # Ab yeh hamesha sahi folder mein 'database.csv' dhoondega
#         self.db_file = os.path.join(base_path, "database.csv")
        
#         self.build_login()



# import customtkinter as ctk
# from tkinter import messagebox
# import re
# import csv
# import os

# # basic UI setup
# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")

# class StudentPortal(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Student Portal - Secure Login")
#         self.geometry("520x700")
#         self.configure(fg_color="#eef2f7")

#         self.active_frame = None
#         self.db_file = "database.csv" # Aapki file ka naam
#         self.build_login()

#     def switch_frame(self, new_frame):
#         if self.active_frame is not None:
#             self.active_frame.destroy()
#         self.active_frame = new_frame
#         self.active_frame.pack(padx=40, pady=40, fill="both", expand=True)

#     # ------------------ Login Page ------------------
#     def build_login(self):
#         frame = ctk.CTkFrame(self, corner_radius=20, fg_color="white")

#         title = ctk.CTkLabel(frame, text="Login", font=("Segoe UI", 26, "bold"))
#         title.pack(pady=(40, 25))

#         self.email = ctk.CTkEntry(frame, placeholder_text="Email (@jecrcu.edu.in)", width=320, height=45)
#         self.email.pack(pady=10)

#         self.roll = ctk.CTkEntry(frame, placeholder_text="Roll No (24bconXXXX)", width=320, height=45)
#         self.roll.pack(pady=10)

#         # Added Password Field for stronger logic
#         self.pwd = ctk.CTkEntry(frame, placeholder_text="Password", show="*", width=320, height=45)
#         self.pwd.pack(pady=10)

#         login_btn = ctk.CTkButton(frame, text="Secure Login", width=320, height=45,
#                                  fg_color="#00a884", hover_color="#02c39a",
#                                  command=self.validate_user)
#         login_btn.pack(pady=25)

#         self.switch_frame(frame)

#     def validate_user(self):
#         email_input = self.email.get().strip().lower()
#         roll_input = self.roll.get().strip().lower()
#         pwd_input = self.pwd.get().strip()

#         # Step 1: Basic Regex Validation
#         if not re.match(r"^[a-z0-9._%+-]+@jecrcu\.edu\.in$", email_input):
#             messagebox.showerror("Error", "Use official college email only.")
#             return

#         # Step 2: Database (CSV) Check
#         if not os.path.exists(self.db_file):
#             messagebox.showerror("Error", f"Database file '{self.db_file}' not found!")
#             return

#         authenticated = False
#         user_name = ""

#         try:
#             with open(self.db_file, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     # Logic Check: Email + Roll + Password must match
#                     if (row['email'].strip().lower() == email_input and 
#                         row['roll_no'].strip().lower() == roll_input and 
#                         row['password'].strip() == pwd_input):
#                         authenticated = True
#                         user_name = row['name']
#                         break
            
#             if authenticated:
#                 self.build_dashboard(user_name, roll_input)
#             else:
#                 messagebox.showerror("Auth Failed", "Invalid Credentials. Please check Email/Roll/Password.")
        
#         except Exception as e:
#             messagebox.showerror("System Error", f"Error reading database: {e}")

#     # ------------------ Dashboard ------------------
#     def build_dashboard(self, name, roll):
#         frame = ctk.CTkFrame(self, corner_radius=20, fg_color="white")

#         welcome = ctk.CTkLabel(frame, text=f"Welcome: {name}", font=("Segoe UI", 20, "bold"), text_color="#1d4ed8")
#         welcome.pack(pady=(20, 5))
        
#         roll_lbl = ctk.CTkLabel(frame, text=f"Roll No: {roll.upper()}", font=("Segoe UI", 14))
#         roll_lbl.pack(pady=(0, 15))

#         # Semester Selection
#         self.semester = ctk.StringVar(value="Select Semester")
#         sem_menu = ctk.CTkOptionMenu(frame, values=["Sem 1", "Sem 2", "Sem 3", "Sem 4"],
#                                      variable=self.semester, width=250)
#         sem_menu.pack(pady=10)

#         # Marks Input
#         self.entries = []
#         for i in range(5):
#             e = ctk.CTkEntry(frame, placeholder_text=f"Subject {i+1} marks", width=250)
#             e.pack(pady=5)
#             self.entries.append(e)

#         calc_btn = ctk.CTkButton(frame, text="Calculate CGPA", width=250,
#                                 fg_color="#1d4ed8", hover_color="#2563eb",
#                                 command=self.calculate_cgpa)
#         calc_btn.pack(pady=20)

#         self.result = ctk.CTkLabel(frame, text="", font=("Segoe UI", 20, "bold"))
#         self.result.pack(pady=10)

#         logout_btn = ctk.CTkButton(frame, text="Logout", width=100, fg_color="transparent", 
#                                   text_color="gray", hover_color="#f3f4f6", command=self.build_login)
#         logout_btn.pack(pady=10)

#         self.switch_frame(frame)

#     def calculate_cgpa(self):
#         try:
#             marks = []
#             for entry in self.entries:
#                 val = entry.get().strip()
#                 if not val.isdigit():
#                     raise ValueError("Numeric values only")
#                 num = int(val)
#                 if num < 0 or num > 100:
#                     raise ValueError("Out of range")
#                 marks.append(num)

#             avg = sum(marks) / len(marks)
#             cgpa = avg / 10
#             self.result.configure(text=f"CGPA: {cgpa:.2f}", text_color="#059669")
        
#         except ValueError as e:
#             messagebox.showerror("Input Error", str(e) if str(e) != "" else "Please enter marks between 0-100")

# if __name__ == "__main__":
#     app = StudentPortal()
#     app.mainloop()





# import customtkinter as ctk # Yeh line miss ho gayi thi
# from tkinter import messagebox
# import re
# import csv
# import os

# # basic UI setup
# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")

# class StudentPortal(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Student Portal - Secure Login")
#         self.geometry("520x700")
#         self.configure(fg_color="#eef2f7")

#         # --- REFINED PATH LOGIC ---
#         # Yeh line detect karegi ki project.py kis folder mein hai
#         base_path = os.path.dirname(os.path.abspath(__file__))
#         # Aur usi folder mein database.csv ko dhoondegi
#         self.db_file = os.path.join(base_path, "database.csv")
        
#         self.active_frame = None
#         self.build_login()

#     def switch_frame(self, new_frame):
#         if self.active_frame is not None:
#             self.active_frame.destroy()
#         self.active_frame = new_frame
#         self.active_frame.pack(padx=40, pady=40, fill="both", expand=True)

#     # ------------------ Login Page ------------------
#     def build_login(self):
#         frame = ctk.CTkFrame(self, corner_radius=20, fg_color="white")

#         title = ctk.CTkLabel(frame, text="Login", font=("Segoe UI", 26, "bold"))
#         title.pack(pady=(40, 25))

#         self.email = ctk.CTkEntry(frame, placeholder_text="Email (@jecrcu.edu.in)", width=320, height=45)
#         self.email.pack(pady=10)

#         self.roll = ctk.CTkEntry(frame, placeholder_text="Roll No (24bconXXXX)", width=320, height=45)
#         self.roll.pack(pady=10)

#         self.pwd = ctk.CTkEntry(frame, placeholder_text="Password", show="*", width=320, height=45)
#         self.pwd.pack(pady=10)

#         login_btn = ctk.CTkButton(frame, text="Secure Login", width=320, height=45,
#                                  fg_color="#00a884", hover_color="#02c39a",
#                                  command=self.validate_user)
#         login_btn.pack(pady=25)

#         self.switch_frame(frame)

#     def validate_user(self):
#         email_input = self.email.get().strip().lower()
#         roll_input = self.roll.get().strip().lower()
#         pwd_input = self.pwd.get().strip()

#         if not re.match(r"^[a-z0-9._%+-]+@jecrcu\.edu\.in$", email_input):
#             messagebox.showerror("Error", "Use official college email only.")
#             return

#         # Check if file exists using the dynamic path
#         if not os.path.exists(self.db_file):
#             messagebox.showerror("Error", f"File not found at:\n{self.db_file}")
#             return

#         authenticated = False
#         user_name = ""

#         try:
#             with open(self.db_file, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     if (row['email'].strip().lower() == email_input and 
#                         row['roll_no'].strip().lower() == roll_input and 
#                         row['password'].strip() == pwd_input):
#                         authenticated = True
#                         user_name = row['name']
#                         break
            
#             if authenticated:
#                 self.build_dashboard(user_name, roll_input)
#             else:
#                 messagebox.showerror("Auth Failed", "Invalid Credentials!")
        
#         except Exception as e:
#             messagebox.showerror("System Error", f"Error: {e}")

#     # ------------------ Dashboard ------------------
#     def build_dashboard(self, name, roll):
#         frame = ctk.CTkFrame(self, corner_radius=20, fg_color="white")
#         welcome = ctk.CTkLabel(frame, text=f"Welcome: {name}", font=("Segoe UI", 20, "bold"), text_color="#1d4ed8")
#         welcome.pack(pady=(20, 5))
        
#         self.result = ctk.CTkLabel(frame, text="Login Successful!", font=("Segoe UI", 16))
#         self.result.pack(pady=20)

#         logout_btn = ctk.CTkButton(frame, text="Logout", command=self.build_login)
#         logout_btn.pack(pady=10)

#         self.switch_frame(frame)

# if __name__ == "__main__":
# #     app = StudentPortal()
# #     app.mainloop()










# import customtkinter as ctk
# from tkinter import messagebox
# import re
# import csv
# import os
# from datetime import datetime

# # UI setup
# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")

# class StudentPortal(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("JECRC University - Detailed Grading System")
#         self.geometry("600x850")
#         self.configure(fg_color="#eef2f7")

#         # Path Logic
#         base_path = os.path.dirname(os.path.abspath(__file__))
#         self.db_file = os.path.join(base_path, "database.csv")
#         self.results_file = os.path.join(base_path, "results.csv")
        
#         self.active_frame = None
#         self.current_user_roll = ""
#         self.current_user_name = ""
#         self.final_cgpa = 0.0

#         self.build_login()

#     def switch_frame(self, new_frame):
#         if self.active_frame is not None:
#             self.active_frame.destroy()
#         self.active_frame = new_frame
#         self.active_frame.pack(padx=20, pady=20, fill="both", expand=True)

#     # ------------------ Login Logic ------------------
#     def build_login(self):
#         frame = ctk.CTkFrame(self, corner_radius=20, fg_color="white")
#         ctk.CTkLabel(frame, text="Student Login", font=("Segoe UI", 28, "bold")).pack(pady=(60, 30))

#         self.email = ctk.CTkEntry(frame, placeholder_text="College Email", width=350, height=45)
#         self.email.pack(pady=10)

#         self.roll = ctk.CTkEntry(frame, placeholder_text="Roll No (24bconXXXX)", width=350, height=45)
#         self.roll.pack(pady=10)

#         self.pwd = ctk.CTkEntry(frame, placeholder_text="Password", show="*", width=350, height=45)
#         self.pwd.pack(pady=10)

#         ctk.CTkButton(frame, text="Login to Portal", width=350, height=50, font=("Segoe UI", 16, "bold"),
#                       fg_color="#00a884", hover_color="#02c39a", command=self.validate_user).pack(pady=30)

#         self.switch_frame(frame)

#     def validate_user(self):
#         e_in, r_in, p_in = self.email.get().strip().lower(), self.roll.get().strip().lower(), self.pwd.get().strip()
        
#         if not os.path.exists(self.db_file):
#             messagebox.showerror("Error", "Database file missing!")
#             return

#         try:
#             with open(self.db_file, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     if row['email'].lower() == e_in and row['roll_no'].lower() == r_in and row['password'] == p_in:
#                         self.current_user_name = row['name']
#                         self.current_user_roll = r_in
#                         self.build_dashboard()
#                         return
#             messagebox.showerror("Auth Failed", "Invalid Email, Roll or Password!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Error: {e}")

#     # ------------------ Dashboard Logic ------------------
#     def build_dashboard(self):
#         main_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="white")
        
#         # Header
#         header = ctk.CTkLabel(main_frame, text=f"Welcome, {self.current_user_name}", font=("Segoe UI", 22, "bold"), text_color="#1d4ed8")
#         header.pack(pady=(20, 5))
        
#         # Semester Dropdown (1 to 8)
#         self.semester = ctk.StringVar(value="Select Semester")
#         sem_list = [f"Semester {i}" for i in range(1, 9)]
#         ctk.CTkOptionMenu(main_frame, values=sem_list, variable=self.semester, width=300).pack(pady=10)

#         # Scrollable area for 5 Subjects
#         scroll_frame = ctk.CTkScrollableFrame(main_frame, width=500, height=400, fg_color="transparent")
#         scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

#         self.subject_data = [] # List to store entry objects

#         for i in range(1, 6): # Assuming 5 Subjects
#             sub_label = ctk.CTkLabel(scroll_frame, text=f"Subject {i}", font=("Segoe UI", 16, "bold"), text_color="#374151")
#             sub_label.pack(pady=(15, 5))
            
#             row = ctk.CTkFrame(scroll_frame, fg_color="#f9fafb", corner_radius=10)
#             row.pack(pady=5, fill="x", padx=5)

#             # 4 Inputs for each subject
#             is1 = ctk.CTkEntry(row, placeholder_text="IS1 (40)", width=100)
#             is1.grid(row=0, column=0, padx=5, pady=10)
            
#             is2 = ctk.CTkEntry(row, placeholder_text="IS2 (40)", width=100)
#             is2.grid(row=0, column=1, padx=5, pady=10)
            
#             asgn = ctk.CTkEntry(row, placeholder_text="ASG (20)", width=100)
#             asgn.grid(row=0, column=2, padx=5, pady=10)
            
#             final = ctk.CTkEntry(row, placeholder_text="Final (100)", width=100)
#             final.grid(row=0, column=3, padx=5, pady=10)

#             self.subject_data.append({'is1': is1, 'is2': is2, 'asgn': asgn, 'final': final})

#         # Calculation & Save Buttons
#         btn_row = ctk.CTkFrame(main_frame, fg_color="transparent")
#         btn_row.pack(pady=20)

#         ctk.CTkButton(btn_row, text="Calculate CGPA", width=180, height=45, command=self.calculate_weighted_cgpa).grid(row=0, column=0, padx=10)
        
#         self.save_btn = ctk.CTkButton(btn_row, text="Save Result", width=180, height=45, fg_color="#f59e0b", 
#                                      state="disabled", command=self.save_result)
#         self.save_btn.grid(row=0, column=1, padx=10)

#         self.result_lbl = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 24, "bold"))
#         self.result_lbl.pack(pady=5)

#         ctk.CTkButton(main_frame, text="Logout", fg_color="transparent", text_color="red", command=self.build_login).pack(pady=10)

#         self.switch_frame(main_frame)

#     # ------------------ Weighted Calculation Logic ------------------
#     def calculate_weighted_cgpa(self):
#         try:
#             total_weighted_marks = 0
            
#             for data in self.subject_data:
#                 # Get values and validate
#                 v1 = float(data['is1'].get() or 0)
#                 v2 = float(data['is2'].get() or 0)
#                 vas = float(data['asgn'].get() or 0)
#                 vfn = float(data['final'].get() or 0)

#                 if v1 > 40 or v2 > 40 or vas > 20 or vfn > 100:
#                     raise ValueError("Marks exceed maximum limits!")

#                 # Weightage Formula:
#                 # IS1 (15%) + IS2 (15%) + ASG (100% of 20) + Final (50% of 100)
#                 subject_total = (v1/40 * 15) + (v2/40 * 15) + vas + (vfn/100 * 50)
#                 total_weighted_marks += subject_total

#             avg_marks = total_weighted_marks / 5
#             self.final_cgpa = avg_marks / 10
            
#             self.result_lbl.configure(text=f"CGPA: {self.final_cgpa:.2f}", text_color="#059669")
#             self.save_btn.configure(state="normal")

#         except ValueError as e:
#             messagebox.showerror("Input Error", f"Invalid Input: {e}\n(IS1:40, IS2:40, ASG:20, Final:100)")

#     # ------------------ Save Logic ------------------
#     def save_result(self):
#         sem = self.semester.get()
#         if sem == "Select Semester":
#             messagebox.showwarning("Warning", "Please select your semester!")
#             return

#         file_exists = os.path.isfile(self.results_file)
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

#         try:
#             with open(self.results_file, mode='a', newline='') as f:
#                 writer = csv.writer(f)
#                 if not file_exists:
#                     writer.writerow(["Date", "Roll No", "Name", "Semester", "CGPA"])
#                 writer.writerow([timestamp, self.current_user_roll, self.current_user_name, sem, f"{self.final_cgpa:.2f}"])
            
#             messagebox.showinfo("Success", "Data saved to results.csv")
#             self.save_btn.configure(state="disabled")
#         except Exception as e:
#             messagebox.showerror("Error", f"Save Failed: {e}")

# if __name__ == "__main__":
#     app = StudentPortal()
#     app.mainloop()






# import customtkinter as ctk
# from tkinter import messagebox
# import csv
# import os

# # Appearance - Minimal Soft Theme
# ctk.set_appearance_mode("light") 

# class StudentPortal(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Aesthetic Portal")
#         self.geometry("550x750")
#         self.configure(fg_color="#FDFEFF") # Pure Clean White Background

#         # Path Logic
#         base_path = os.path.dirname(os.path.abspath(__file__))
#         self.db_file = os.path.join(base_path, "database.csv")
        
#         self.active_frame = None
#         self.build_login()

#     def switch_frame(self, new_frame):
#         if self.active_frame is not None:
#             self.active_frame.destroy()
#         self.active_frame = new_frame
#         self.active_frame.pack(fill="both", expand=True)

#     # ------------------ Minimal Login ------------------
#     def build_login(self):
#         frame = ctk.CTkFrame(self, fg_color="transparent")
        
#         ctk.CTkLabel(frame, text="welcome back", font=("Helvetica", 32, "bold"), text_color="#2D3436").pack(pady=(100, 40))

#         self.email = ctk.CTkEntry(frame, placeholder_text="email", width=320, height=45, border_width=0, fg_color="#F1F2F6", corner_radius=10)
#         self.email.pack(pady=10)

#         self.roll = ctk.CTkEntry(frame, placeholder_text="roll no", width=320, height=45, border_width=0, fg_color="#F1F2F6", corner_radius=10)
#         self.roll.pack(pady=10)

#         self.pwd = ctk.CTkEntry(frame, placeholder_text="password", show="*", width=320, height=45, border_width=0, fg_color="#F1F2F6", corner_radius=10)
#         self.pwd.pack(pady=10)

#         ctk.CTkButton(frame, text="Login", width=320, height=45, corner_radius=10, 
#                       fg_color="#6C5CE7", hover_color="#A29BFE", font=("Helvetica", 14, "bold"),
#                       command=self.validate_user).pack(pady=40)

#         self.switch_frame(frame)

#     def validate_user(self):
#         e_in, r_in, p_in = self.email.get().strip().lower(), self.roll.get().strip().lower(), self.pwd.get().strip()
#         try:
#             with open(self.db_file, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     if row['email'].lower() == e_in and row['roll_no'].lower() == r_in and row['password'] == p_in:
#                         self.user_name = row['name']
#                         self.user_roll = r_in
#                         self.build_dashboard()
#                         return
#             messagebox.showerror("Error", "Check your credentials")
#         except Exception: messagebox.showerror("Error", "Database error")

#     # ------------------ Minimal Dashboard ------------------
#     def build_dashboard(self):
#         frame = ctk.CTkFrame(self, fg_color="transparent")
        
#         # Centered Header
#         ctk.CTkLabel(frame, text=f"hello, {self.user_name.split()[0].lower()}", font=("Helvetica", 28, "bold"), text_color="#2D3436").pack(pady=(40, 10))
        
#         self.semester = ctk.StringVar(value="semester 1")
#         sem_menu = ctk.CTkOptionMenu(frame, values=[f"semester {i}" for i in range(1, 9)], 
#                                      variable=self.semester, fg_color="#F1F2F6", text_color="#2D3436", 
#                                      button_color="#F1F2F6", width=140)
#         sem_menu.pack(pady=10)

#         # Subject Inputs - No Borders, Clean Layout
#         scroll = ctk.CTkScrollableFrame(frame, width=500, height=380, fg_color="transparent")
#         scroll.pack(pady=20, padx=30, fill="both")

#         self.subject_entries = []
#         for i in range(1, 6):
#             sub_title = ctk.CTkLabel(scroll, text=f"subject {i}", font=("Helvetica", 13, "bold"), text_color="#636E72")
#             sub_title.pack(anchor="w", padx=10, pady=(15, 2))
            
#             row = ctk.CTkFrame(scroll, fg_color="transparent")
#             row.pack(fill="x")

#             # Mini Inputs with soft background
#             params = {"width": 85, "height": 35, "border_width": 0, "fg_color": "#F1F2F6", "corner_radius": 8, "font": ("Helvetica", 12)}
            
#             is1 = ctk.CTkEntry(row, placeholder_text="is1", **params)
#             is1.pack(side="left", padx=5)
#             is2 = ctk.CTkEntry(row, placeholder_text="is2", **params)
#             is2.pack(side="left", padx=5)
#             asg = ctk.CTkEntry(row, placeholder_text="asg", **params)
#             asg.pack(side="left", padx=5)
#             fnl = ctk.CTkEntry(row, placeholder_text="final", **params)
#             fnl.pack(side="left", padx=5)

#             self.subject_entries.append({'is1': is1, 'is2': is2, 'asgn': asg, 'final': fnl})

#         # Calculate Button - Aesthetic Purple
#         ctk.CTkButton(frame, text="calculate", width=250, height=45, corner_radius=20,
#                       fg_color="#6C5CE7", hover_color="#A29BFE", font=("Helvetica", 14, "bold"),
#                       command=self.calculate_cgpa).pack(pady=20)

#         # Large Clean Result
#         self.result_lbl = ctk.CTkLabel(frame, text="", font=("Helvetica", 36, "bold"), text_color="#6C5CE7")
#         self.result_lbl.pack(pady=5)

#         ctk.CTkButton(frame, text="logout", fg_color="transparent", text_color="#B2BEC3", 
#                       hover_color="#F1F2F6", command=self.build_login).pack(pady=10)

#         self.switch_frame(frame)

#     def calculate_cgpa(self):
#         try:
#             total_score = 0
#             for s in self.subject_entries:
#                 # Formula implementation
#                 i1, i2, a, f = float(s['is1'].get() or 0), float(s['is2'].get() or 0), float(s['asgn'].get() or 0), float(s['final'].get() or 0)
#                 if i1>40 or i2>40 or a>20 or f>100: raise ValueError
                
#                 weighted = (i1/40*15) + (i2/40*15) + a + (f/100*50)
#                 total_score += weighted
            
#             cgpa = (total_score / 5) / 10
#             self.result_lbl.configure(text=f"{cgpa:.2f}")
#         except: messagebox.showerror("Input Error", "Enter valid marks (is:40, asg:20, final:100)")

# if __name__ == "__main__":
#     app = StudentPortal()
#     app.mainloop()







# import customtkinter as ctk
# from tkinter import messagebox
# import csv
# import os

# ctk.set_appearance_mode("light")


# class StudentPortal(ctk.CTk):

#     def __init__(self):
#         super().__init__()

#         self.title("StudentHub")
#         self.geometry("560x740")
#         self.configure(fg_color="#F8FAFC")

#         base_path = os.path.dirname(os.path.abspath(__file__))
#         self.db_file = os.path.join(base_path, "database.csv")

#         self.current_frame = None

#         self.build_login()

#     def change_frame(self, frame):
#         if self.current_frame:
#             self.current_frame.destroy()

#         self.current_frame = frame
#         self.current_frame.pack(fill="both", expand=True)

#     def build_login(self):

#         frame = ctk.CTkFrame(self, fg_color="transparent")

#         ctk.CTkLabel(
#             frame,
#             text="Student Login",
#             font=("Segoe UI", 30, "bold"),
#             text_color="#0F172A"
#         ).pack(pady=(90, 10))

#         ctk.CTkLabel(
#             frame,
#             text="Enter your details to continue",
#             font=("Segoe UI", 13),
#             text_color="#64748B"
#         ).pack(pady=(0, 30))

#         self.email_entry = ctk.CTkEntry(
#             frame,
#             placeholder_text="Email",
#             width=320,
#             height=44,
#             border_width=0,
#             corner_radius=10,
#             fg_color="#E2E8F0",
#             font=("Segoe UI", 13)
#         )
#         self.email_entry.pack(pady=10)

#         self.roll_entry = ctk.CTkEntry(
#             frame,
#             placeholder_text="Roll Number",
#             width=320,
#             height=44,
#             border_width=0,
#             corner_radius=10,
#             fg_color="#E2E8F0",
#             font=("Segoe UI", 13)
#         )
#         self.roll_entry.pack(pady=10)

#         self.password_entry = ctk.CTkEntry(
#             frame,
#             placeholder_text="Password",
#             show="*",
#             width=320,
#             height=44,
#             border_width=0,
#             corner_radius=10,
#             fg_color="#E2E8F0",
#             font=("Segoe UI", 13)
#         )
#         self.password_entry.pack(pady=10)

#         ctk.CTkButton(
#             frame,
#             text="Login",
#             width=320,
#             height=44,
#             corner_radius=10,
#             fg_color="#2563EB",
#             hover_color="#1D4ED8",
#             font=("Segoe UI", 14, "bold"),
#             command=self.validate_user
#         ).pack(pady=35)

#         self.change_frame(frame)

#     def validate_user(self):

#         email = self.email_entry.get().strip().lower()
#         roll = self.roll_entry.get().strip().lower()
#         password = self.password_entry.get().strip()

#         try:
#             with open(self.db_file, mode="r") as file:

#                 reader = csv.DictReader(file)

#                 for row in reader:

#                     if (
#                         row["email"].lower() == email
#                         and row["roll_no"].lower() == roll
#                         and row["password"] == password
#                     ):

#                         self.student_name = row["name"]
#                         self.build_dashboard()
#                         return

#             messagebox.showerror("Login Failed", "Invalid credentials")

#         except FileNotFoundError:
#             messagebox.showerror("Error", "Database file not found")

#     def build_dashboard(self):

#         frame = ctk.CTkFrame(self, fg_color="transparent")

#         first_name = self.student_name.split()[0]

#         ctk.CTkLabel(
#             frame,
#             text=f"Welcome, {first_name}",
#             font=("Segoe UI", 28, "bold"),
#             text_color="#0F172A"
#         ).pack(pady=(35, 10))

#         self.semester = ctk.StringVar(value="Semester 1")

#         semester_menu = ctk.CTkOptionMenu(
#             frame,
#             values=[f"Semester {i}" for i in range(1, 9)],
#             variable=self.semester,
#             width=160,
#             fg_color="#E2E8F0",
#             button_color="#CBD5E1",
#             button_hover_color="#94A3B8",
#             text_color="#0F172A",
#             dropdown_fg_color="#F8FAFC",
#             font=("Segoe UI", 13)
#         )

#         semester_menu.pack(pady=10)

#         scroll_frame = ctk.CTkScrollableFrame(
#             frame,
#             width=500,
#             height=380,
#             fg_color="transparent"
#         )

#         scroll_frame.pack(padx=25, pady=20, fill="both")

#         self.subject_data = []

#         for i in range(1, 6):

#             ctk.CTkLabel(
#                 scroll_frame,
#                 text=f"Course {i}",
#                 font=("Segoe UI", 13, "bold"),
#                 text_color="#475569"
#             ).pack(anchor="w", padx=8, pady=(14, 4))

#             row = ctk.CTkFrame(
#                 scroll_frame,
#                 fg_color="transparent"
#             )

#             row.pack(fill="x")

#             is1_entry = ctk.CTkEntry(
#                 row,
#                 placeholder_text="ISA 1",
#                 width=90,
#                 height=36,
#                 border_width=0,
#                 corner_radius=8,
#                 fg_color="#E2E8F0",
#                 font=("Segoe UI", 12)
#             )
#             is1_entry.pack(side="left", padx=5)

#             is2_entry = ctk.CTkEntry(
#                 row,
#                 placeholder_text="ISA 2",
#                 width=90,
#                 height=36,
#                 border_width=0,
#                 corner_radius=8,
#                 fg_color="#E2E8F0",
#                 font=("Segoe UI", 12)
#             )
#             is2_entry.pack(side="left", padx=5)

#             assignment_entry = ctk.CTkEntry(
#                 row,
#                 placeholder_text="Assignment",
#                 width=100,
#                 height=36,
#                 border_width=0,
#                 corner_radius=8,
#                 fg_color="#E2E8F0",
#                 font=("Segoe UI", 12)
#             )
#             assignment_entry.pack(side="left", padx=5)

#             final_entry = ctk.CTkEntry(
#                 row,
#                 placeholder_text="Final",
#                 width=90,
#                 height=36,
#                 border_width=0,
#                 corner_radius=8,
#                 fg_color="#E2E8F0",
#                 font=("Segoe UI", 12)
#             )
#             final_entry.pack(side="left", padx=5)

#             self.subject_data.append({
#                 "isa1": is1_entry,
#                 "isa2": is2_entry,
#                 "assignment": assignment_entry,
#                 "final": final_entry
#             })

#         ctk.CTkButton(
#             frame,
#             text="Generate CGPA",
#             width=260,
#             height=45,
#             corner_radius=12,
#             fg_color="#2563EB",
#             hover_color="#1D4ED8",
#             font=("Segoe UI", 14, "bold"),
#             command=self.calculate_cgpa
#         ).pack(pady=20)

#         self.cgpa_label = ctk.CTkLabel(
#             frame,
#             text="",
#             font=("Segoe UI", 34, "bold"),
#             text_color="#2563EB"
#         )

#         self.cgpa_label.pack(pady=5)

#         ctk.CTkButton(
#             frame,
#             text="Sign Out",
#             fg_color="transparent",
#             hover_color="#E2E8F0",
#             text_color="#64748B",
#             command=self.build_login
#         ).pack(pady=12)

#         self.change_frame(frame)

#     def calculate_cgpa(self):

#         try:

#             total_marks = 0

#             for subject in self.subject_data:

#                 isa1 = float(subject["isa1"].get() or 0)
#                 isa2 = float(subject["isa2"].get() or 0)
#                 assignment = float(subject["assignment"].get() or 0)
#                 final_exam = float(subject["final"].get() or 0)

#                 if min(isa1, isa2, assignment, final_exam) < 0:
#                     raise ValueError

#                 if isa1 > 40 or isa2 > 40:
#                     raise ValueError

#                 if assignment > 20 or final_exam > 100:
#                     raise ValueError

#                 score = (
#                     (isa1 / 40) * 15
#                     + (isa2 / 40) * 15
#                     + assignment
#                     + (final_exam / 100) * 50
#                 )

#                 total_marks += score

#             cgpa = (total_marks / 5) / 10

#             self.cgpa_label.configure(
#                 text=f"{cgpa:.2f}"
#             )

#         except ValueError:

#             messagebox.showerror(
#                 "Invalid Input",
#                 "Please enter valid marks"
#             )


# if __name__ == "__main__":

#     app = StudentPortal()
#     app.mainloop()


import customtkinter as ctk
from tkinter import messagebox
import csv
import os

ctk.set_appearance_mode("light")


class StudentPortal(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("StudentHub")
        self.geometry("560x740")
        self.configure(fg_color="#F8FAFC")

        base_path = os.path.dirname(os.path.abspath(__file__))
        self.db_file = os.path.join(base_path, "database.csv")

        self.current_frame = None

        self.subject_count = {
            "Semester 1": 6,
            "Semester 2": 6,
            "Semester 3": 5,
            "Semester 4": 5,
            "Semester 5": 2,
            "Semester 6": 2,
            "Semester 7": 2,
            "Semester 8": 1
        }

        self.build_login()

    def change_frame(self, frame):

        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = frame
        self.current_frame.pack(fill="both", expand=True)

    def build_login(self):

        frame = ctk.CTkFrame(self, fg_color="transparent")

        ctk.CTkLabel(
            frame,
            text="Student Login",
            font=("Segoe UI", 30, "bold"),
            text_color="#0F172A"
        ).pack(pady=(90, 10))

        ctk.CTkLabel(
            frame,
            text="Enter your details to continue",
            font=("Segoe UI", 13),
            text_color="#64748B"
        ).pack(pady=(0, 30))

        self.email_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Email",
            width=320,
            height=44,
            border_width=0,
            corner_radius=10,
            fg_color="#E2E8F0",
            font=("Segoe UI", 13)
        )
        self.email_entry.pack(pady=10)

        self.roll_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Roll Number",
            width=320,
            height=44,
            border_width=0,
            corner_radius=10,
            fg_color="#E2E8F0",
            font=("Segoe UI", 13)
        )
        self.roll_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Password",
            show="*",
            width=320,
            height=44,
            border_width=0,
            corner_radius=10,
            fg_color="#E2E8F0",
            font=("Segoe UI", 13)
        )
        self.password_entry.pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Login",
            width=320,
            height=44,
            corner_radius=10,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            font=("Segoe UI", 14, "bold"),
            command=self.validate_user
        ).pack(pady=35)

        self.change_frame(frame)

    def validate_user(self):

        email = self.email_entry.get().strip().lower()
        roll = self.roll_entry.get().strip().lower()
        password = self.password_entry.get().strip()

        try:

            with open(self.db_file, mode="r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    if (
                        row["email"].lower() == email
                        and row["roll_no"].lower() == roll
                        and row["password"] == password
                    ):

                        self.student_name = row["name"]
                        self.build_dashboard()
                        return

            messagebox.showerror("Login Failed", "Invalid credentials")

        except FileNotFoundError:

            messagebox.showerror(
                "Error",
                "Database file not found"
            )

    def build_dashboard(self):

        frame = ctk.CTkFrame(self, fg_color="transparent")

        first_name = self.student_name.split()[0]

        ctk.CTkLabel(
            frame,
            text=f"Welcome, {first_name}",
            font=("Segoe UI", 28, "bold"),
            text_color="#0F172A"
        ).pack(pady=(35, 10))

        self.semester = ctk.StringVar(value="Semester 1")

        semester_menu = ctk.CTkOptionMenu(
            frame,
            values=list(self.subject_count.keys()),
            variable=self.semester,
            width=160,
            fg_color="#E2E8F0",
            button_color="#CBD5E1",
            button_hover_color="#94A3B8",
            text_color="#0F172A",
            dropdown_fg_color="#F8FAFC",
            font=("Segoe UI", 13),
            command=self.load_subjects
        )

        semester_menu.pack(pady=10)

        self.scroll_frame = ctk.CTkScrollableFrame(
            frame,
            width=500,
            height=380,
            fg_color="transparent"
        )

        self.scroll_frame.pack(
            padx=25,
            pady=20,
            fill="both"
        )

        self.subject_data = []

        self.load_subjects("Semester 1")

        ctk.CTkButton(
            frame,
            text="Generate CGPA",
            width=260,
            height=45,
            corner_radius=12,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            font=("Segoe UI", 14, "bold"),
            command=self.calculate_cgpa
        ).pack(pady=20)

        self.cgpa_label = ctk.CTkLabel(
            frame,
            text="",
            font=("Segoe UI", 34, "bold"),
            text_color="#2563EB"
        )

        self.cgpa_label.pack(pady=5)

        ctk.CTkButton(
            frame,
            text="Sign Out",
            fg_color="transparent",
            hover_color="#E2E8F0",
            text_color="#64748B",
            command=self.build_login
        ).pack(pady=12)

        self.change_frame(frame)

    def load_subjects(self, semester):

        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        self.subject_data.clear()

        total_subjects = self.subject_count[semester]

        for i in range(1, total_subjects + 1):

            ctk.CTkLabel(
                self.scroll_frame,
                text=f"Course {i}",
                font=("Segoe UI", 13, "bold"),
                text_color="#475569"
            ).pack(anchor="w", padx=8, pady=(14, 4))

            row = ctk.CTkFrame(
                self.scroll_frame,
                fg_color="transparent"
            )

            row.pack(fill="x")

            isa1_entry = ctk.CTkEntry(
                row,
                placeholder_text="ISA 1",
                width=90,
                height=36,
                border_width=0,
                corner_radius=8,
                fg_color="#E2E8F0",
                font=("Segoe UI", 12)
            )
            isa1_entry.pack(side="left", padx=5)

            isa2_entry = ctk.CTkEntry(
                row,
                placeholder_text="ISA 2",
                width=90,
                height=36,
                border_width=0,
                corner_radius=8,
                fg_color="#E2E8F0",
                font=("Segoe UI", 12)
            )
            isa2_entry.pack(side="left", padx=5)

            assignment_entry = ctk.CTkEntry(
                row,
                placeholder_text="Assignment",
                width=100,
                height=36,
                border_width=0,
                corner_radius=8,
                fg_color="#E2E8F0",
                font=("Segoe UI", 12)
            )
            assignment_entry.pack(side="left", padx=5)

            final_entry = ctk.CTkEntry(
                row,
                placeholder_text="Final",
                width=90,
                height=36,
                border_width=0,
                corner_radius=8,
                fg_color="#E2E8F0",
                font=("Segoe UI", 12)
            )
            final_entry.pack(side="left", padx=5)

            self.subject_data.append({
                "isa1": isa1_entry,
                "isa2": isa2_entry,
                "assignment": assignment_entry,
                "final": final_entry
            })

    def calculate_cgpa(self):

        try:

            total_marks = 0
            total_subjects = len(self.subject_data)

            for subject in self.subject_data:

                isa1 = float(subject["isa1"].get() or 0)
                isa2 = float(subject["isa2"].get() or 0)
                assignment = float(subject["assignment"].get() or 0)
                final_exam = float(subject["final"].get() or 0)

                if min(isa1, isa2, assignment, final_exam) < 0:
                    raise ValueError

                if isa1 > 40 or isa2 > 40:
                    raise ValueError

                if assignment > 20 or final_exam > 100:
                    raise ValueError

                score = (
                    (isa1 / 40) * 15
                    + (isa2 / 40) * 15
                    + assignment
                    + (final_exam / 100) * 50
                )

                total_marks += score

            cgpa = (total_marks / total_subjects) / 10

            self.cgpa_label.configure(
                text=f"{cgpa:.2f}"
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid marks"
            )


if __name__ == "__main__":

    app = StudentPortal()
    app.mainloop()