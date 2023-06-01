import requests
from bs4 import BeautifulSoup
import time
import smtplib

"""
Time notifier:

By using these script it is possible to set any notifier of any type 
of changes of a certain cite that will inform you by sending mail with
any content and subject that you want.

In these example, program sends mails if the World time is 16:22.

Author: Erik Badalyan
Date: June 2023

"""


while True:
    url = 'https://www.google.com/search?q=clock&sxsrf=ALiCzsaQ9gsBJZ7Xq83pse4bsrF72ICZTg%3A1672315684223&ei=JIOtY6mdDduCxc8P7u2Q8Ag&ved=0ahUKEwipv72y5Z78AhVbQfEDHe42BI4Q4dUDCA8&uact=5&oq=clock&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQQzIFCAAQkQIyCAguEIAEENQCMg4ILhCABBDHARCvARDLATIFCAAQgAQyCAgAEIAEEMsBMggILhDUAhCABDIICAAQgAQQywEyBQgAEIAEMggIABCABBDLAToECAAQRzoECCMQJzoLCC4QgAQQxwEQ0QM6BQguEIAEOgsILhCABBDHARCvAToOCC4QgAQQxwEQrwEQ1AI6DgguEIAEEMcBENEDENQCSgQIQRgASgQIRhgAUJIbWI4fYIIjaABwAngAgAGrAYgB7QWSAQMwLjWYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp'
    url_req = requests.get(url)

    soup = BeautifulSoup(url_req.text, 'html.parser')
    world_time = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text
    print(world_time)
    if world_time == '16:22':
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        smt.ehlo()
        smt.starttls()
        smt.login("erik.badalyan700@gmail.com", 'avipyqvwrzjlbjok')
        smt.sendmail('erik.badalyan700@gmail.com',
                     'erik.badalyan700@gmail.com',
                     f"Subject: World_time\n\nTime changed")
        print('finish changed')
    time.sleep(10)



# OR
# import requests
# from bs4 import BeautifulSoup
# import time
# import smtplib
# from selenium import webdriver
#
# while True:
#     url = 'https://www.google.com/search?q=clock&sxsrf=ALiCzsaQ9gsBJZ7Xq83pse4bsrF72ICZTg%3A1672315684223&ei=JIOtY6mdDduCxc8P7u2Q8Ag&ved=0ahUKEwipv72y5Z78AhVbQfEDHe42BI4Q4dUDCA8&uact=5&oq=clock&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQQzIFCAAQkQIyCAguEIAEENQCMg4ILhCABBDHARCvARDLATIFCAAQgAQyCAgAEIAEEMsBMggILhDUAhCABDIICAAQgAQQywEyBQgAEIAEMggIABCABBDLAToECAAQRzoECCMQJzoLCC4QgAQQxwEQ0QM6BQguEIAEOgsILhCABBDHARCvAToOCC4QgAQQxwEQrwEQ1AI6DgguEIAEEMcBENEDENQCSgQIQRgASgQIRhgAUJIbWI4fYIIjaABwAngAgAGrAYgB7QWSAQMwLjWYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp'
#     driver = webdriver.Chrome()
#     driver.get(url)
#     url_req = driver.execute_script("return document.documentElement.innerHTML")
#     soup = BeautifulSoup(url_req, 'html.parser')
#     world_time = soup.find('div', class_='gsrt vk_bk FzvWSb YwPhnf').text
#     print(world_time)
#     if world_time == '16:22':
#         smt = smtplib.SMTP('smtp.gmail.com', 587)
#         smt.ehlo()
#         smt.starttls()
#         smt.login("erik.badalyan700@gmail.com", 'avipyqvwrzjlbjok')
#         smt.sendmail('erik.badalyan700@gmail.com',
#                      'erik.badalyan700@gmail.com',
#                      f"Subject: World_time\n\nTime changed")
#         print('finish changed')
#     time.sleep(10)


# OR 2
# import requests
# from bs4 import BeautifulSoup
# import time
# import smtplib
# from requests_html import HTMLSession
# while True:
#     url = 'https://www.google.com/search?q=clock&sxsrf=ALiCzsaQ9gsBJZ7Xq83pse4bsrF72ICZTg%3A1672315684223&ei=JIOtY6mdDduCxc8P7u2Q8Ag&ved=0ahUKEwipv72y5Z78AhVbQfEDHe42BI4Q4dUDCA8&uact=5&oq=clock&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQQzIFCAAQkQIyCAguEIAEENQCMg4ILhCABBDHARCvARDLATIFCAAQgAQyCAgAEIAEEMsBMggILhDUAhCABDIICAAQgAQQywEyBQgAEIAEMggIABCABBDLAToECAAQRzoECCMQJzoLCC4QgAQQxwEQ0QM6BQguEIAEOgsILhCABBDHARCvAToOCC4QgAQQxwEQrwEQ1AI6DgguEIAEEMcBENEDENQCSgQIQRgASgQIRhgAUJIbWI4fYIIjaABwAngAgAGrAYgB7QWSAQMwLjWYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp'
#     s = HTMLSession()
#     r = s.get(url)
#     r.html.render(sleep=2)
#
#     soup = BeautifulSoup(r.html.html, 'html.parser')
#     world_time = soup.find('div', class_='gsrt vk_bk FzvWSb YwPhnf').text
#     print(world_time)
#     if world_time == '16:22':
#         smt = smtplib.SMTP('smtp.gmail.com', 587)
#         smt.ehlo()
#         smt.starttls()
#         smt.login("erik.badalyan700@gmail.com", 'avipyqvwrzjlbjok')
#         smt.sendmail('erik.badalyan700@gmail.com',
#                      'erik.badalyan700@gmail.com',
#                      f"Subject: World_time\n\nTime changed")
#         print('finish changed')
#     time.sleep(10)