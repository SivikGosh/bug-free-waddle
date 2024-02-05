from pyrogram import Client
# import time
import re
from dotenv import load_dotenv
import os
import sqlite3
# import sys

load_dotenv()


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
app = Client('parser', api_id, api_hash)


# def main():
#     with app:
#         start_date = sys.argv[1]

#         count = 0

#         for i in app.search_messages(os.getenv('SRC_CHAT_ID'), query='#нужно'):
#             current_date = i.date.strftime("%Y-%m-%d")
#             if (current_date != start_date):
#                 try:
#                     lower_mes = i.text.lower()
#                 except AttributeError:
#                     lower_mes = '_'
#                 mes = re.findall(r'[A-Яа-я0-9\/]+', lower_mes)
#                 con = sqlite3.connect('db.sqlite3')
#                 cur = con.cursor()
#                 res = cur.execute('SELECT * FROM addresses')
#                 for j in res.fetchall():
#                     alias = [j[1]]
#                     build = j[2].split(',')
#                     sett = set(alias + build)
#                     if len(sett.intersection(mes)) > 1:
#                         app.forward_messages(
#                             'me',
#                             from_chat_id=os.getenv('SRC_CHAT_ID'),
#                             message_ids=i.id
#                         )
#                     count += 1
#             else:
#                 break

#             time.sleep(1)

#         app.send_message('me', f'проверено {count} сообщений')
#         app.read_chat_history(os.getenv('SRC_CHAT_ID'))


@app.on_message()
def test(client, message):
    if (message.chat.id == int(os.getenv('SRC_CHAT_ID'))) and ('#нужно' in message.text):
        try:
            lower_mes = message.text.lower()
        except AttributeError:
            lower_mes = '_'
        mes = re.findall(r'[A-Яа-я0-9\/]+', lower_mes)
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()
        res = cur.execute('SELECT * FROM addresses')
        for j in res.fetchall():
            alias = [j[1]]
            build = j[2].split(',')
            sett = set(alias + build)
            if len(sett.intersection(mes)) > 1:
                client.forward_messages(
                    int(os.getenv('TARGET_CHAT_ID')),
                    from_chat_id=os.getenv('SRC_CHAT_ID'),
                    message_ids=message.id
                )


app.run()
