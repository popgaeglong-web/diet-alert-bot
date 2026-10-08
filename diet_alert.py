import requests
from datetime import datetime
import pytz

# กำหนด Timezone เป็นประเทศไทย
tz = pytz.timezone('Asia/Bangkok')
now = datetime.now(tz)
current_time = now.strftime('%H:%M')

print(f"Current time: {current_time}")

# ตารางเวลาและข้อความแจ้งเตือน (สามารถเพิ่มเวลาอื่นๆ ได้ตามต้องการ)
schedule_dict = {
    "15:21": "🚨 ถึงเวลาดื่มน้ำและเช็กเป้าหมายลดน้ำหนักแล้วครับ!",
    "15:25": "🥗 ได้เวลาควบคุมอาหารช่วงบ่ายแล้ว สู้ๆ นะครับ!",
}

# ตรวจสอบว่าเวลาปัจจุบันตรงกับตารางเวลาหรือไม่
if current_time in schedule_dict:
    message = schedule_dict[current_time]
    topic = "sister_diet_2026"
    
    # ส่งแจ้งเตือนผ่าน ntfy.sh
    response = requests.post(
        f"https://ntfy.sh/{topic}",
        data=message.encode(encoding='utf-8')
    )
    
    if response.status_code == 200:
        print(f"Alert sent successfully at {current_time}!")
    else:
        print("Failed to send alert.")
else:
    print(f"No alert scheduled for {current_time}.")
