from pyrogram.errors import FloodWait
from functools import wraps
import asyncio
import time
from collections import defaultdict

# রেট লিমিট ট্র্যাক করার জন্য ডিকশনারি
user_requests = defaultdict(list)

def flood_protect(func):
    @wraps(func)
    async def wrapper(client, message):
        user_id = message.from_user.id if message.from_user else None
        
        if user_id:
            now = time.time()
            
            # গত ১ সেকেন্ডের রিকুয়েস্ট ফিল্টার
            user_requests[user_id] = [
                t for t in user_requests[user_id] 
                if now - t < 1
            ]
            
            # প্রতি সেকেন্ডে ৩ বার এর বেশি না
            if len(user_requests[user_id]) >= 3:
                await message.reply("⚠️ আপনি খুব দ্রুত রিকুয়েস্ট পাঠাচ্ছেন! একটু থামুন।")
                return
            
            # বর্তমান রিকুয়েস্ট টাইম সেভ
            user_requests[user_id].append(now)
        
        try:
            return await func(client, message)
        except FloodWait as e:
            wait_time = e.x
            await asyncio.sleep(wait_time + 1)
            return await func(client, message)
    
    return wrapper