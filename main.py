import socket
import re
import operator

# import mariadb
import pymysql.cursors
import sys

import requests
import json
import os

HOST = '0.0.0.0'
PORT = 514
fname = "syslog.log"

time = ""
app = ""
src = ""
dst = ""
srcMac = ""
dstMac = ""
proto = ""
Category = ""
rule = ""
note = ""
fw_action = ""
dstname = ""
usr = ""
arg = ""
msg = ""

hafiza = ""

print("-------------------------------------------------")
print("CEYLAN LOG SYS.")
print("-------------------------------------------------")


def yaz(logi):
        f = open('KCM_Logi.txt', 'a')
        f.write(logi)
        f.write('\n')
        f.close()

def check_ping():
    hostname = "192.168.11.104"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "1"
    else:
        pingstatus = "0"

    return pingstatus


def ipgeo(ipadres):
    try:

        request_url = 'https://geolocation-db.com/jsonp/' + ipadres
        # Send request and decode the result
        response = requests.get(request_url)
        result = response.content.decode()
        # Clean the returned string so it just contains the dictionary data for the IP address
        result = result.split("(")[1].strip(")")
        # Convert this data into a dictionary
        result = json.loads(result)
        return result

    except:
        return ""


def baglan():
    global conn
    global cur
    try:
        conn = pymysql.connect(host='192.168.11.104',
                               user='root',
                               password='Sys.kcm.2022',
                               db='logsys',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        # conn = mariadb.connect(
        #     user="root",
        #     password="Sys.kcm.2022",
        #     host="192.168.11.104",
        #     port=3306,
        #     database="logsys"
        #
        # )

    except pymysql.Error as e:
        print(f"Error connecting to Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()


def Kayit_Ekle_Any(time, app, src, dst, srcMac, dstMac, Category, proto, rule, note, fw_action, dstname, usr, arg, msg):
    sql = """insert into `log_any` (time, app, src, dst, srcMac, dstMac, proto, Category, rule, note, action, country_code, country_name, city, state, dstname, usr, arg, msg)
             values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
        """
    DIS_IPADRES = dst.split(":")[0]
    geo = ipgeo(DIS_IPADRES)

    try:
        cur.execute(sql, (
        time, app, src, dst, srcMac, dstMac, Category, proto, rule, note, fw_action, geo["country_code"],
        geo["country_name"], geo["city"], geo["state"], dstname, usr, arg, msg))
        conn.commit()
    except:
        pass



baglan()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"{HOST} Listening on port {PORT}")

    while True:

        if check_ping == 0:
            baglan()



        try:

            data = s.recv(1024).decode()
            result = re.findall(r'''\S+=(?:"[^"]+?")|(?:'[^']+?')|\S+=\S+''', data)
            son_sonuc = list(map(lambda x: tuple(x.split('=')), result))


            index = 0
            while index < len(son_sonuc):

                element = son_sonuc[index][0]

                if element == "time":
                    time = son_sonuc[index][1].replace(chr(34), "")

                if element == "app":
                    app = son_sonuc[index][1].replace(chr(34), "")

                if element == "src":
                    src = son_sonuc[index][1].replace(chr(34), "")

                if element == "dst":
                    dst = son_sonuc[index][1].replace(chr(34), "")

                if element == "srcMac":
                    srcMac = son_sonuc[index][1].replace(chr(34), "")

                if element == "dstMac":
                    dstMac = son_sonuc[index][1].replace(chr(34), "")

                if element == "proto":
                    proto = son_sonuc[index][1].replace(chr(34), "")

                if element == "Category":
                    Category = son_sonuc[index][1].replace(chr(34), "")

                if element == "rule":
                    rule = son_sonuc[index][1].replace(chr(34), "")

                if element == "note":
                    note = son_sonuc[index][1].replace(chr(34), "")

                if element == "fw_action":
                    fw_action = son_sonuc[index][1].replace(chr(34), "")

                if element == "dstname":
                    dstname = son_sonuc[index][1].replace(chr(34), "")

                if element == "usr":
                    usr = son_sonuc[index][1].replace(chr(34), "")

                if element == "arg":
                    arg = son_sonuc[index][1].replace(chr(34), "")

                if element == "msg":
                    msg = son_sonuc[index][1].replace(chr(34), "")


                index += 1
        except:
            pass

        cevirmen = str(result)
        if (cevirmen.find("dstname") > 1 and (cevirmen.find("dropped") < 1 and cevirmen.find("denied") < 1)):
            print(time, app, src, dst, srcMac, dstMac, proto, Category, rule, note, fw_action, dstname, usr, arg, msg)
            # yaz(str(son_sonuc))
            Kayit_Ekle_Any(time, app, src, dst, srcMac, dstMac, proto, Category, rule, note, fw_action, dstname, usr, arg, msg)

        # print(proto, time, app, src, dst, srcMac, dstMac, Category, rule, note, fw_action)

        # if proto == "tcp/https" and fw_action == "NA":
        #     print(proto, time, app, src, dst, srcMac, dstMac, Category, rule, note, fw_action)
        #     Kayit_Ekle_Any(time, app, src, dst, srcMac, dstMac, proto, Category, rule, note, fw_action)
        # if yasakli == 'E':
        #     if (proto == "tcp/https" and fw_action == "drop"):
        #         print(proto, time, app, src, dst, srcMac, dstMac, Category, rule, note, fw_action)
        #         Kayit_Ekle_Drop(time, app, src, dst, srcMac, dstMac, proto, Category, rule, note, fw_action)

        # print(son_sonuc)
        # print(result(0))
        # print(data)

        if not data:
            break
