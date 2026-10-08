import requests
from datetime import datetime, timedelta, timezone

# กำหนดเวลาประเทศไทย (UTC+7)
tz_th = timezone(timedelta(hours=7))
now = datetime.now(tz_th)
current_time = now.strftime('%H:%M')

print(f"Current Thai time: {current_time}")

# ตารางเวลาและข้อความแจ้งเตือน
schedule_dict = {
    "15:30": "🚨 ทดสอบระบบแจ้งเตือนสำเร็จแล้วครับ!",
    "15:35": "🥗 ได้เวลาควบคุมอาหารช่วงบ่ายแล้ว สู้ๆ นะครับ!",
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
