from flask import Blueprint, render_template, make_response, redirect, session, jsonify
from flask_dance.consumer import oauth_authorized
from Models.Google import Google


mod = Blueprint('google_routes', __name__)


@oauth_authorized.connect
def grab_tok(blueprint, token):
    print(token)


@mod.route('/load')
def load_data():
    tok = session['google_oauth_token']['access_token']
    google = Google(tok=tok)
    events_list = google.last_N_days_of_events(days=7)

    return jsonify(events_list)
