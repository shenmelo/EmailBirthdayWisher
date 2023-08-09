import datetime as dt
import pandas as pd
import smtplib
import random


MY_EMAIL = "sherwinatendido.dev@gmail.com"
PASSWORD = "vxlroinpstqjcokw"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    celebrant = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as data_file:
        content = data_file.read()
        letter = content.replace("[NAME]", celebrant["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=celebrant["email"],
                            msg=f"Subject:Happy Birthday!\n\n{letter}")


