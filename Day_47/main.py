import requests
from bs4 import BeautifulSoup
import smtplib
my_email = ""
password = ""
header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
 			"accept-encoding": "gzip, deflate, br",
 			"accept-language": "en",
 			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
}
url = "https://www.amazon.in/GoPro-Waterproof-Digital-Action-Warranty/dp/B08G2HBBB6/ref=sr_1_14?keywords=go%2Bpro%2B11&qid=1681463472&sprefix=go%2Bpro%2Caps%2C356&sr=8-14&th=1"

response = requests.get(url=url,headers=header)
print(response)
data = response.text
soup = BeautifulSoup(data,'html.parser')
price = soup.find(name='span', class_='a-price-whole')
print("\n ",price)
price = price.text.replace(',', '')
price = float(price)
if price < 30000:
    print("\n price",price)
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        msg = f"The price  of the product has been dropped to {price}, now you can buy the product,url - {url}"
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="demo2@gmail.com",
                            msg=f"Subject:Product ALert\n\n{msg}")
