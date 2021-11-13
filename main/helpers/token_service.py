from secrets import token_urlsafe


def generate_url_token() -> str:
    return token_urlsafe(60)