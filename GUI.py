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

# Create labels and entry fields
label_target = tk.Label(window, text="กรอกแคลลอรี่ที่ต้องการลด:")
label_target.grid(row=0, column=0, sticky="w")
entry_target = tk.Entry(window)
entry_target.grid(row=0, column=1)

label_weight = tk.Label(window, text="จำนวนน้ำหนักของคุณ (kg):")
label_weight.grid(row=1, column=0, sticky="w")
entry_weight = tk.Entry(window)
entry_weight.grid(row=1, column=1)

label_time = tk.Label(window, text="เวลาที่จะเดิน (นาที):")
label_time.grid(row=2, column=0, sticky="w")
entry_time = tk.Entry(window)
entry_time.grid(row=2, column=1)

label_speed = tk.Label(window, text="ความเร็วในการเดิน (กม./ชม.):")
label_speed.grid(row=3, column=0, sticky="w")
entry_speed = tk.Entry(window)
entry_speed.grid(row=3, column=1)

label_met = tk.Label(window, text="MET (ช้า=3, กลาง=4, เร็ว=5):")
label_met.grid(row=4, column=0, sticky="w")
entry_met = tk.Entry(window)
entry_met.grid(row=4, column=1)

# Calculate button
calculate_button = tk.Button(window, text="คำนวณ", command=calculate_calories)
calculate_button.grid(row=5, column=0, columnspan=2)

# Start the GUI event loop
window.mainloop()
