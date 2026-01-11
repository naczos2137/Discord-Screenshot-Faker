import json
import os
import random
import datetime


logs = {
    "messages": []
}


def create_json_from_raw_data():
    YOUR_NICK = input("your nick: ")
    with open(os.path.join('data', 'trx_data.txt'), 'r', encoding='utf-8') as trx_file:
        trx_file = trx_file.readlines()
        trx_data = []
        for line_nr in range(0, len(trx_file), 4):
            trx_data.append({
                'value': trx_file[line_nr].strip(),
                'user': trx_file[line_nr + 1].strip(),
                'date': trx_file[line_nr + 2].strip()
            })

    conversations = []
    for filename in os.listdir(os.path.join('data', 'conversations')):
        if filename.endswith('.txt'):
            conversation = []
            with open(os.path.join('data', 'conversations', filename), 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith('i:') or line.startswith('k:'):
                        conversation.append(line.strip())
            conversations.append(conversation)

    random.shuffle(conversations)


    for data in trx_data:
        messages = []
        conversation = conversations.pop()
        for line in conversation:
            messages.append({
                'user': YOUR_NICK if line.startswith('i:') else data['user'],
                'content': line[3:].replace('{cena}', data['value']),
                'timestamp': data['date']
            })
        logs['messages'].append(messages)

    random_nicks = []

    with open(os.path.join('data', 'nicki.txt'), 'r', encoding='utf') as nicks_file:
        lines = nicks_file.readlines()
        for line in lines:
            random_nicks.append(line.strip())

    random.shuffle(random_nicks)

    for conversation in conversations:
        messages = []
        price = random.randint(20, 100)
        day = random.randint(1, 30)
        emergency_nick = random_nicks.pop()
        for line in conversation:
            messages.append({
                'user': YOUR_NICK if line.startswith('i:') else emergency_nick,
                'content': line[3:].replace('{cena}', str(price)),
                'timestamp': f'{str(day).zfill(2)}.{str(datetime.datetime.now().month).zfill(2)}.{datetime.datetime.now().year}'
            })
        logs['messages'].append(messages)


    with open('logi.json', 'w', encoding='utf-8') as file:
        json.dump(logs, file, ensure_ascii=False, indent=4)