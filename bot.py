import os, time, requests

TOKEN = os.getenv("TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

offset = 0
while True:
    try:
        r = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 30}).json()
        for u in r.get("result", []):
            offset = u["update_id"] + 1
            msg = u.get("message")
            if msg and "text" in msg:
                chat_id = msg["chat"]["id"]
                text = msg["text"]
                requests.post(f"{URL}/sendMessage", json={"chat_id": chat_id, "text": f"وصلتني: {text}"})
    except Exception as e:
        print(e)
        time.sleep(5)
