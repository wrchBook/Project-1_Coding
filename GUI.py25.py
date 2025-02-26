import tkinter as tk
from tkinter import messagebox

def calculate_calories():
    try:
        target = int(entry_target.get())
        weight = int(entry_weight.get())
        time = int(entry_time.get())
        speed = int(entry_speed.get())
        met = int(entry_met.get())

        # Sample calculation for calories burned (you can adjust the formula)
        # Formula: Calories burned = MET x weight (kg) x time (hours)
        calories_burned = met * weight * (time / 60)

        if calories_burned >= target:
            messagebox.showinfo("ผลลัพธ์", "สำเร็จตามเป้าหมาย")
        else:
            messagebox.showinfo("ผลลัพธ์", f"ไม่สำเร็จตามเป้าหมาย\nคุณขาดแคลอรี่ {target - calories_burned:.2f} แคลลอรี่")

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง")

# Set up the main window
window = tk.Tk()
window.title("คำนวณการเผาผลาญแคลลอรี่")
window.geometry("400x350")  # Set window size
window.configure(bg="#f2f2f2")  # Set background color

# Create a title label
title_label = tk.Label(window, text="คำนวณการเผาผลาญแคลลอรี่", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#4CAF50")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create labels and entry fields
label_target = tk.Label(window, text="กรอกแคลลอรี่ที่ต้องการลด:", font=("Arial", 12), bg="#f2f2f2", anchor="w")
label_target.grid(row=1, column=0, sticky="w", padx=20, pady=5)
entry_target = tk.Entry(window, font=("Arial", 12), bd=2, relief="solid")
entry_target.grid(row=1, column=1, padx=20, pady=5)

label_weight = tk.Label(window, text="จำนวนน้ำหนักของคุณ (kg):", font=("Arial", 12), bg="#f2f2f2", anchor="w")
label_weight.grid(row=2, column=0, sticky="w", padx=20, pady=5)
entry_weight = tk.Entry(window, font=("Arial", 12), bd=2, relief="solid")
entry_weight.grid(row=2, column=1, padx=20, pady=5)

label_time = tk.Label(window, text="เวลาที่จะเดิน (นาที):", font=("Arial", 12), bg="#f2f2f2", anchor="w")
label_time.grid(row=3, column=0, sticky="w", padx=20, pady=5)
entry_time = tk.Entry(window, font=("Arial", 12), bd=2, relief="solid")
entry_time.grid(row=3, column=1, padx=20, pady=5)

label_speed = tk.Label(window, text="ความเร็วในการเดิน (กม./ชม.):", font=("Arial", 12), bg="#f2f2f2", anchor="w")
label_speed.grid(row=4, column=0, sticky="w", padx=20, pady=5)
entry_speed = tk.Entry(window, font=("Arial", 12), bd=2, relief="solid")
entry_speed.grid(row=4, column=1, padx=20, pady=5)

label_met = tk.Label(window, text="MET (ช้า=3, กลาง=4, เร็ว=5):", font=("Arial", 12), bg="#f2f2f2", anchor="w")
label_met.grid(row=5, column=0, sticky="w", padx=20, pady=5)
entry_met = tk.Entry(window, font=("Arial", 12), bd=2, relief="solid")
entry_met.grid(row=5, column=1, padx=20, pady=5)

# Calculate button
calculate_button = tk.Button(window, text="คำนวณ", font=("Arial", 14, "bold"), fg="white", bg="#4CAF50", bd=0, relief="solid", command=calculate_calories)
calculate_button.grid(row=6, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

# Start the GUI event loop
window.mainloop()