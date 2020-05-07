from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time

token = "6ae4f05ab2f1e52b159d3cafac4c57f6d548dea57e3eb53d56490a14a1d6d56c2c8cc9ff6f20abca418fa"
vk_session=vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(str(datetime.strftime(datetime.now(), "%H:%M:%S")) + ' От:' + str(event.user_id) + '.' + str(event.text))
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Здарова епты', 'random_id': 0})
