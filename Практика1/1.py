import redis
import random
import string
import time
import json

# Подключение к Redis
r = redis.Redis(decode_responses=True)

while True:
    # Генерация случайного сообщения
    message = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    # Преобразование словаря в строку JSON
    message_dict = {'message': message}
    message_json = json.dumps(message_dict)
    
    # Отправка сообщения в Redis
    r.lpush('messages', message_json)
    print(f"Sent: {message_json}")
    time.sleep(60)
