import requests
from datetime import datetime, timezone, timedelta

class Google:
    def __init__(self, tok):
        self.base_url = 'https://www.googleapis.com/'
        self.headers = {"Authorization": f"Bearer {tok}"}
        # self.email = requests.get(f"{self.base_url}/oauth2/v3/userinfo", headers=self.headers).json()['email']


    def get_events(self, N_days_past):
        url = f'{self.base_url}/calendar/v3/calendars/primary/events'
        params = {
            'updatedMin': N_days_past.isoformat(),
            'orderBy': 'updated'
        }
        r = requests.get(url, headers=self.headers, params=params)
        return r.json()


    def last_N_days_of_events(self, days=7):
        # N days ago
        # assuming UTC timezone?
        date_now = datetime.now(timezone.utc).astimezone()

        N_days_past = date_now - timedelta(days=days)
        N_days_future = date_now + timedelta(days=days)

        master_arr = []
        # iterate thru each event
        for item in self.get_events(N_days_past=N_days_past)['items']:
            # if event was not confirmed, skip
            if item['status'] != 'confirmed':
                continue

            event_start_date = datetime.fromisoformat(item['start']['dateTime'])
            event_end_date = datetime.fromisoformat(item['end']['dateTime'])

            # if event falls outside of 7 days in the past, skip
            if not (N_days_past <= event_start_date <= date_now):
                continue
            # build dict
            event_obj = {
                'summary': item['summary'],
                'creator_email': item['creator']['email'],
                'start_datetime': event_start_date,
                'end_datetime': event_end_date,
            }

            master_arr.append(event_obj)

        return master_arr
