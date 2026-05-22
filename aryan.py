import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        # Fetch values from entry boxes
        i1 = float(entry_insem1.get())
        i2 = float(entry_insem2.get())
        assign = float(entry_assignment.get())
        esem = float(entry_endsem.get())

        # Validation for max marks
        if i1 > 40 or i2 > 40 or assign > 20 or esem > 100:
            messagebox.showwarning("Input Error", "Please ensure marks are within limits:\nInsem: 40, Assignment: 20, Endsem: 100")
            return

        # Mathematical Logic:
        # Final = 15% of In1 + 15% of In2 + 100% of Assignment + 50% of Endsem
        final_score = (0.15 * i1) + (0.15 * i2) + assign + (0.50 * esem)
        
        # Criteria logic
        # Condition 1: Endsem > 35
        # Condition 2: Final score > 40
        if esem > 35 and final_score > 40:
            result_text = f"Final Score: {final_score:.2f}\nStatus: PASS"
            lbl_result.config(text=result_text, fg="green")
        else:
            result_text = f"Final Score: {final_score:.2f}\nStatus: FAIL"
            lbl_result.config(text=result_text, fg="red")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric marks.")

# --- UI Setup ---
root = tk.Tk()
root.title("Marks Calculator")
root.geometry("350x450")
root.config(padx=20, pady=20)

# Title
tk.Label(root, text="Student Marks Calculator", font=("Arial", 14, "bold")).pack(pady=10)

# Input Fields
tk.Label(root, text="1st Insem (Max 40):").pack(anchor="w")
entry_insem1 = tk.Entry(root)
entry_insem1.pack(fill="x", pady=5)

tk.Label(root, text="2nd Insem (Max 40):").pack(anchor="w")
entry_insem2 = tk.Entry(root)
entry_insem2.pack(fill="x", pady=5)

tk.Label(root, text="Assignment (Max 20):").pack(anchor="w")
entry_assignment = tk.Entry(root)
entry_assignment.pack(fill="x", pady=5)

tk.Label(root, text="Endsem (Max 100):").pack(anchor="w")
entry_endsem = tk.Entry(root)
entry_endsem.pack(fill="x", pady=5)

# Calculate Button
btn_calc = tk.Button(root, text="Calculate Result", command=calculate_result, 
                     bg="#007BFF", fg="white", font=("Arial", 10, "bold"))
btn_calc.pack(pady=20, fill="x")

# Result Display
lbl_result = tk.Label(root, text="", font=("Arial", 12, "bold"))
lbl_result.pack(pady=10)

root.mainloop()