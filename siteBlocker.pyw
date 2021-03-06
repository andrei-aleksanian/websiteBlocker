import time
from datetime import datetime as dt


file_path = r"C:\Windows\System32\Drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com", "vk.com", "www.vk.com"]

start_time = 15
end_time = 19

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, start_time)
            < dt.now() < dt(dt.now().year,
                            dt.now().month, dt.now().day, end_time)):
        print("Work hours!")

        with open(file_path, 'r+',) as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(file_path, 'r+',) as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")

    time.sleep(5)
