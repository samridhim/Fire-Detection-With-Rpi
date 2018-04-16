import urllib2
import json
import time


READ_API_KEY='PC0K2M3N4WB75JEU '
CHANNEL_ID = '467067'

while True:
    TS = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                       % (CHANNEL_ID,READ_API_KEY))

    response = TS.read()
    data=json.loads(response)


    a = data['created_at']
    b = data['field1']
    c = data['field2']
    d = data['field3']
    print a + "    " + b + "    " + c + "    " + d
    time.sleep(5)   

    TS.close()
