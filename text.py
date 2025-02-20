target = int("กรอกแคลลอรี่ที่ต้องการลด")
weight =int("จำนวนนำ้หนักของคุณ")
time =int("เวลาที่จะเดิน")
speed =int("ความเร็วในการเดิน")
met =int("ช้า กลาง เร็ว")
if calorie >= target:
    print("สำเร็จตามเป้าหมาย")
else:
    print("ไม่สำเร็จตามเป้าหมาย")
    calorie_deficit = target - calorie
    