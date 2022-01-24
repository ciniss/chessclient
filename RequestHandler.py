import requests


def get_create_game():
    resp = requests.post('http://127.0.0.1:5000/create_game')
    if resp.status_code == 200:
        return resp.json()['game_id']
    else:
        return "err"


def get_update_game(gid, uid):
    resp = requests.get('http://127.0.0.1:5000/game?id=' + gid, data={'user_id': uid})
    return resp.json()['fen']
def login(nick, password):
    resp = requests.get('http://127.0.0.1:5000/login', json={'username': nick, 'password': password})
    return resp.json()['uid']
def register(nick, password, email):
    resp = requests.post('http://127.0.0.1:5000/register', json={'username': nick, 'email': email, 'password': password})
    if resp.status_code == 200:
        return resp.json()['uid']
    return None
def join(gid, uid):
    resp = requests.put('http://127.0.0.1:5000/join_game', json={'game_id': gid, 'user_id': uid})
    json_resp = resp.json()
    if json_resp["status"] == 'ok':
        return json_resp['game_id']
    else:
        return json_resp["status"]
def push_game(gid, uid, move):
    resp = requests.put('http://127.0.0.1:5000/game?id='+gid, json={'user_id': uid, 'move': move, 'time_left': 500})
    if resp.status_code == 200:
        return resp.json()
    else:
        return None



