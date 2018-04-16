from mq import *
import sys, time
import smtplib
import http.client, urllib
import time

def smoketest(a,b,c):
    params = urllib.parse.urlencode({'field1': a,'field2':b,'field3':c,'key':'MLEPEFFVRVX4NNS7'}) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except:
        print("Connection failed!")
            
try:
    print("Press CTRL+C to abort.")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    server.login("nth.credenz16@gmail.com", "******")
    msg = "Hello!"
    count = 0

    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
        smoketest(perc["GAS_LPG"], perc["CO"], perc["SMOKE"])
        sys.stdout.flush()
        if(perc["SMOKE"] > 0.03):
            if(count < 2):
                server.sendmail("nth.credenz16@gmail.com", "samridhimaheshwari@gmail.com",msg)
                count = count + 1
            else:
                time.sleep(1500000)
        time.sleep(120000)

    server.close()

except Exception as e:
    print(e)

