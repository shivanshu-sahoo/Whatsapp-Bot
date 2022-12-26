from twilio.rest import Client
from datetime import datetime
from datetime import date
from datetime import time
import apscheduler
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dateutil.parser import parse
import time
import os
from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']

client_twilio = Client(account_sid, auth_token)
def send_rem(rem):
  message = client_twilio.messages.create(
  from_='+13253265312',
  body=rem,
  to='+917735611200' 
)


s=['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']


scheduler = BackgroundScheduler()
creds= ServiceAccountCredentials.from_json_keyfile_name("credentials.json",s)
client=gspread.authorize(creds)


worksheet = client.open("Messages").sheet1
list_of_lists = worksheet.get_all_values()
scheduler.start()
while(1):
    time.sleep(2)
    row = worksheet.row_values(2)
    if row:
        try:
            if row[2]=="Done":
                scheduler.add_job(send_rem, 'date', run_date=parse(row[0]), args=[row[1]])
                worksheet.delete_rows(2)
        except:
            pass
    else:
        pass




