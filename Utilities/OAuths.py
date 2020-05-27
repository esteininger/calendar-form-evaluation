from flask_dance import OAuth2ConsumerBlueprint
from config import google_secret

google = OAuth2ConsumerBlueprint(
    "google", __name__,
    client_id=google_secret['client_id'],
    client_secret=google_secret['client_secret'],
    authorization_url="https://accounts.google.com/o/oauth2/auth",
    token_url="https://accounts.google.com/o/oauth2/token",
    scope=[
        "https://www.googleapis.com/auth/calendar.readonly",
        "https://www.googleapis.com/auth/userinfo.email"
    ],
    redirect_url="/build"
)
