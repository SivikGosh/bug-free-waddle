from pyrogram import Client
import time
from unique_addresses import result
import re
from dotenv import load_dotenv
import os


load_dotenv()


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
app = Client("my_account", api_id, api_hash)


def main():
    with app:
        start_date = input(
            'введите начальную дату периода (в формате гггг-мм-дд): '
        )
        count = 0

        for i in app.search_messages(os.getenv('SRC_CHAT_ID'), query='#нужно'):
            current_date = i.date.strftime("%Y-%m-%d")
            if (current_date != start_date):
                mes = re.findall(r'[A-Яа-я0-9\/-]+', i.text)
                for j in result:
                    print(j.intersection(set(mes)))
                    # if len(set(i.text.lower().split()).intersection(j)) > 0:
                    #     app.send_message('me', i.text)
                    #     app.forward_messages(
                    #         'me',
                    #         from_chat_id=os.getenv('SRC_CHAT_ID'),
                    #         message_ids=i.id
                    #     )
                    count += 1
            else:
                break

            time.sleep(1)

        app.send_message('me', f'загружено {count} сообщений')
        app.read_chat_history(os.getenv('SRC_CHAT_ID'))

        print(f'загружено {count} сообщений')


app.run(main())

# регулярка:
# r'[а-я0-9\/-]+'
