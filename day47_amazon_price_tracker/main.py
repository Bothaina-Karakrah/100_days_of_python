from bs4 import BeautifulSoup
import requests
import smtplib
# Add the os and dotenv modules
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7",
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()
# Remove the dollar sign using split
price = price.split("$")[1]
clean_price = price.replace('\u200e', ' ')
price = float(clean_price)
# print(price)

# ====================== Send an Email ===========================

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
# print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 70
if price <= BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    # Use environment variables
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )