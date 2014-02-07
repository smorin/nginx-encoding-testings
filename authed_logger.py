import hmac
import md5
import base64
from hashlib import sha1
import json

import requests

token_store = {
    "user1": "token1",
    "user2": "token2",
    "user3": "bullshittoken3",
}

test_valid_log_body = {
    "game": "AE",
    "env": "prod",
    "events": [
        { "tag": "a" },
        { "x": "b" },
    ],
}

test_invalid_log_body = {
    "game": "broked",
    "env": "invalid",
}

test_valid_log3_body = {
  "header": {
    "api_version": 3,
    "game": "AE",
    "game_version": "1.2a",
    "env": "prod",
    "session_id": "1FC94472-3189-48DF-9860-0C3FC8750726",
    "user_info": {
      "game_player_id": "12345",
    },
    "versions": {
      "game_version": "1.222adajkfhel", 
    },
  },
  "events": [],
  "batch_info": {
    "batch_id": "abced",
    "cum_events": 190823,
    "batch_no": 1413,
  },
}

log_host = "http://localhost:9000"
#log_host = "http://ec2-54-201-38-165.us-west-2.compute.amazonaws.com:9000"
#log_path = "/naiveLog"
log_path = "/log/3/test/1.00"
log_url = log_host + log_path

def get_current_time_as_date_header():
    from wsgiref.handlers import format_date_time
    from datetime import datetime
    from time import mktime

    now = datetime.now()
    stamp = mktime(now.timetuple())
    return format_date_time(stamp)

date_value = get_current_time_as_date_header()
method = 'POST'

base64_body = base64.b64encode(md5.new(json.dumps(test_valid_log3_body)).digest())

print "body signature: {}".format(base64_body)

joined_message = '\n'.join([method, date_value, log_path, base64_body])
token = token_store['user1']
digest_maker = hmac.new(token)
digest_maker.update(joined_message)
print "signing: {}".format(joined_message)

signature = base64.b64encode(digest_maker.digest())

print "HMAC signature: {}".format(signature)

headers={
    "Date": get_current_time_as_date_header(),
    "Authorization": "kxae_secret_{} : {}".format('user1', signature),
    #"Content-type": "application/json",
}

# print "headers: {}".format(headers)
# print "body: {}".format(json.dumps(test_valid_log_body))

# r = requests.post("http://requestb.in/x75s2gx7", headers=headers, data=json.dumps(test_valid_log_body))
# print r.content

r = requests.post(log_url, headers=headers, data=json.dumps(test_valid_log3_body))
print r.text

# r = requests.post("http://localhost:9000/raw", headers=headers, data=json.dumps(test_valid_log_body))
