import requests


def get_create_game():
    """
        function is requesting a new game from the server
    :return: Returns new game id
    :rtype: str
    """
    resp = requests.post('http://127.0.0.1:5000/create_game')
    if resp.status_code == 200:
        return resp.json()['game_id']
    else:
        return "err"


def get_update_game(gid, uid):
    """
    calls the server for updates of the game
    :param gid: game ID
    :type gid: string
    :param uid: user ID
    :type uid: string
    :return: returns new FEN and two times left
    :rtype: str
    """
    resp = requests.get('http://127.0.0.1:5000/game?id=' + gid, json={'user_id': uid})
    resp_json = resp.json()
    return resp_json['fen'], resp_json['white_time_left'], resp_json['black_time_left'],resp_json["white_nick"], resp_json["black_nick"], resp_json["game_status"]


def login(nick, password):
    """
    Sends API call for login purpose
    :param nick: User nick
    :type nick: str
    :param password: User password
    :type password: str
    :return: returns UUID of the user, later used as an authentication tool
    :rtype: str
    """
    resp = requests.get('http://127.0.0.1:5000/login', json={'username': nick, 'password': password})
    if resp.status_code == 200:
        return resp.json()['uid']
    return "-1"


def register(nick, password, email):
    """
    Registering on server
    :param nick: unique user nickname
    :type nick: str
    :param password: user password
    :type password: str
    :param email: user email
    :type email: str
    :return: returns UUID of the user, later used as an authentication tool
    :rtype: str
    """
    resp = requests.post('http://127.0.0.1:5000/register',
                         json={'username': nick, 'email': email, 'password': password})
    if resp.status_code == 200:
        return resp.json()['uid']
    return None


def join(gid, uid):
    """
    this function allows user to join to a new game
    :param gid: game ID
    :type gid: str
    :param uid: user ID
    :type uid: str
    :return: Game ID
    :rtype: str
    """
    resp = requests.put('http://127.0.0.1:5000/join_game', json={'game_id': gid, 'user_id': uid})
    if resp.status_code == 200:
        return resp.json()['game_id'], resp.json()['color']
    else:
        return "-1", "none"


def push_game(gid, uid, move):
    """
    API call that makes the move if possible
    :param gid: game ID
    :type gid: str
    :param uid: user ID
    :type uid: str
    :param move: move "a1,a2" for ex
    :type move:str
    :return: Status, either good, or some error
    :rtype: str
    """
    resp = requests.put('http://127.0.0.1:5000/game?id=' + gid, json={'user_id': uid, 'move': move, 'time_left': 500})
    if resp.status_code == 200:
        if resp.json()['status'] == "good":
            return resp.json()
        else:
            return None
    else:
        return None
def get_scoreboard():
    """
    returns a scoreboard
    :return: array of users
    :rtype: list

    """
    resp = requests.get("http://127.0.0.1:5000/scoreboard")
    return resp.json()["list"]