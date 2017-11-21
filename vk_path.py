import params
import requests
import tg_path

def getLongPoolSelrver():
    resp = requests.get(f'{params.domain}/messages.getLongPollServer?access_token={params.vk_token}')
    attrs = resp.json()['response']
    return attrs


def longPool():
    attrs = getLongPoolSelrver()
    while True:
        query = 'https://{server}?act=a_check&key={key}&ts={ts}&wait=25&mode=2&version=2'.format(**attrs)
        response = requests.get(query).json()
        # print(response)
        try:
            updates = response['updates']
        except KeyError:
            attrs = getLongPoolSelrver()
            continue
        if updates:
            for event in updates:
                action_code = event[0]
                if action_code == 61:
                    user = requests.get('https://api.vk.com/method/users.get', params={'user_ids': event[1]}).json()[
                        'response'][0]  # получение имени и фамилии пользователя
                    message = f"{id: {event[1]}\nuser['first_name']} {user['last_name']}, набирает сообщение..."
                    tg_path.send_message(message)
        attrs['ts'] = response['ts']



# getLongPoolSelrver()
longPool()