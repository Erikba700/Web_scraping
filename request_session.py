import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import time

load_dotenv()
username = os.getenv("REQUEST_LOGIN")
password = os.getenv('REQUEST_PASSWORD')


url = 'https://auasonis.jenzabarcloud.com/studsect.cfm'
protected_url = 'https://auasonis.jenzabarcloud.com/nmreg1.cfm?items=19BFED78169CDC7CE83FE6687089D30C'

login_data = {'SOC_SEC': username,
              'PIN': password}

cookies = {
    'LOGINPAGE': 'studsect%2Ecfm',
    'JSESSIONID': 'FB0D766BA8773005B965BA73A27F97AB.sonis_9',
    'CFCLIENT_SONISWEBTOOLS': 'idnum%3DBA0013902%23userid%3DBA0013902%23wik%5Fref%3Dnmreg%23photo%3D24b85922c636008b25414%2Ejpg%23loginpage%3Dstudsect%2Ecfm%23soc%5Fsec%3D%2952%5B%2D%26%5EXJ0MT%3B%0A%23weblistdef%3Dweblist%2Ecfm%3Flist%23%3D%26x%23tabcolor%3D707070%23pin%3D%295%40N92%2AU%403%2DT9%0A%23sepcolor%3Dwhite%23wik%5Fun%3DSONISStudent%23namesearch%3DBA0013902%23wik%5Fpw%3Dsonis%23text%3DStudent%23wik%5Fdom%3Dlocal%23accessstring%5Flp%3DStudent%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23usernavpage%3Dstudopt%25%23weburl%3Dhttps%3A%2F%2Fauasonis%2Ejenzabarcloud%2Ecom%2F%23newuniqcfidcftoken%3Den%5Fus%23wik%5Fmod%3Dstud%23schyear%3D202324%23semester%3D4%20%23accessstring%3DS%20T%20U%20D%20E%20N%20T%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23',
    'CFID': '2376179',
    'CFTOKEN': 'b6c775c790e8756e%2DCBD5DE0B%2D0275%2D276F%2D8CEC05AD6D1C9239',
    'CFGLOBALS': 'urltoken%3DCFID%23%3D2376179%26CFTOKEN%23%3Db6c775c790e8756e%2DCBD5DE0B%2D0275%2D276F%2D8CEC05AD6D1C9239%26jsessionid%23%3DFB0D766BA8773005B965BA73A27F97AB%2Esonis%5F9%23lastvisit%3D%7Bts%20%272024%2D07%2D18%2016%3A42%3A55%27%7D%23hitcount%3D172%23timecreated%3D%7Bts%20%272024%2D01%2D31%2012%3A53%3A00%27%7D%23cftoken%3Db6c775c790e8756e%2DCBD5DE0B%2D0275%2D276F%2D8CEC05AD6D1C9239%23cfid%3D2376179%23',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,hy;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'LOGINPAGE=studsect%2Ecfm; JSESSIONID=FB0D766BA8773005B965BA73A27F97AB.sonis_9; CFCLIENT_SONISWEBTOOLS=idnum%3DBA0013902%23userid%3DBA0013902%23wik%5Fref%3Dnmreg%23photo%3D24b85922c636008b25414%2Ejpg%23loginpage%3Dstudsect%2Ecfm%23soc%5Fsec%3D%2952%5B%2D%26%5EXJ0MT%3B%0A%23weblistdef%3Dweblist%2Ecfm%3Flist%23%3D%26x%23tabcolor%3D707070%23pin%3D%295%40N92%2AU%403%2DT9%0A%23sepcolor%3Dwhite%23wik%5Fun%3DSONISStudent%23namesearch%3DBA0013902%23wik%5Fpw%3Dsonis%23text%3DStudent%23wik%5Fdom%3Dlocal%23accessstring%5Flp%3DStudent%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23usernavpage%3Dstudopt%25%23weburl%3Dhttps%3A%2F%2Fauasonis%2Ejenzabarcloud%2Ecom%2F%23newuniqcfidcftoken%3Den%5Fus%23wik%5Fmod%3Dstud%23schyear%3D202324%23semester%3D4%20%23accessstring%3DS%20T%20U%20D%20E%20N%20T%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23; CFID=2376179; CFTOKEN=b6c775c790e8756e%2DCBD5DE0B%2D0275%2D276F%2D8CEC05AD6D1C9239; CFGLOBALS=urltoken%3DCFID%23%3D2376179%26CFTOKEN%23%3Db6c775c790e8756e%2DCBD5DE0B%2D0275%2D276F%2D8CEC05AD6D1C9239%26jsessionid%23%3DFB0D766BA8773005B965BA73A27F97AB%2Esonis%5F9%23lastvisit%3D%7Bts%20%272024%2D07%2D18%2016%3A42%3A55%27%7D%23hitcount%3D172%23timecreated%3D%7Bts%20%272024%2D01%2D31%2012%3A53%3A00%27%7D%23cftoken%3Db6c775c790e8756e%2DCBD5DE0B%2D0275%2D276F%2D8CEC05AD6D1C9239%23cfid%3D2376179%23',
    'origin': 'https://auasonis.jenzabarcloud.com',
    'priority': 'u=0, i',
    'referer': 'https://auasonis.jenzabarcloud.com/studsect.cfm',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'auth': '1',
    'express': '1',
}

data = {
    'SOC_SEC': 'erik_badalyan@edu.aua.am',
    'PIN': 'Addcry700',
}


def session_parse():
    with requests.Session() as session:
        login_response = session.post(url, data=login_data, headers=headers, cookies=cookies, params=params)

        if login_response.status_code == 200:
            print(login_response.text)
            # with open('response.html', 'w', encoding="utf-8") as file:
            #     file.write(login_response.text)
            # print("Login successful!")
            # protected_response = session.get(protected_url)
            # print(protected_response)
            # if protected_response.status_code == 200:
            #     print('protected passed')
            #     soup = BeautifulSoup(protected_response.text, 'html.parser')
            #     register_elem = soup.find_all('h1', class_='title maincontent')
            #     print(register_elem)
            # else:
            #     print('protected failed')
        else:
            print(f"Login failed with status code: {login_response.status_code}")


if __name__ == '__main__':
    start = time.time()
    session_parse()
    print(time.time() - start)