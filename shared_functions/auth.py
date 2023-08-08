import jwt


def create_token():
    payload_data = {
        "sub": "4242",
        "name": "Admin",
        "username": "admin",
        "email": "admin@gmail.com"
    }

    my_secret = 'admin'

    token = jwt.encode(
        payload=payload_data,
        key=my_secret
    )

    return token


def verify_token(token, key):
    try:
        if jwt.decode(token, key=key, algorithms=['HS256', ]):
            return True
    except jwt.PyJWTError:
        return False

