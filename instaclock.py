import autoit
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import playsound

wakeUpTime = datetime.now().replace(hour = 16, minute = 25, second = 0)
ctr = -1

def post(ctr):

    username = "******" #Enter your username
    password = "*******" #Enter your password
    image_path = [r"C:\Users\Malhaar\Desktop\Python Projects\instaclock\snooze1.png", r"C:\Users\Malhaar\Desktop\Python Projects\instaclock\snooze2.png", r"C:\Users\Malhaar\Desktop\Python Projects\instaclock\snooze3.png", r"C:\Users\Malhaar\Desktop\Python Projects\instaclock\snooze4.png"] #The written path is just an example, Delete the path and Enter the Path of your image. #1. path should not start with a back slash
    caption = "Smh." #Enter the caption

    mobile_emulation = { "deviceName": "Pixel 2" }
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(executable_path=r"C:\Users\Malhaar\Downloads\chromedriver_win32 (1)\chromedriver.exe",options=opts) #you must enter the path to your driver
    driver.maximize_window()

    main_url = "https://www.instagram.com"
    driver.get(main_url)

    sleep(4)

    def login():
        login_button = driver.find_element_by_xpath("//button[contains(text(),'Log In')]")
        login_button.click()
        sleep(3)
        username_input = driver.find_element_by_xpath("//input[@name='username']")
        username_input.send_keys(username)
        password_input = driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(password)
        password_input.submit()

    login()

    sleep(4)

    def close_reactivated():
        try:
            sleep(2)
            not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Not Now')]")
            not_now_btn.click()
        except:
            pass

    close_reactivated()

    def close_notification():
        try:
            sleep(2)
            close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
            close_noti_btn.click()
            sleep(2)
        except:
            pass

    close_notification()

    def close_add_to_home():
        sleep(3)
        close_addHome_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
        close_addHome_btn.click()
        sleep(1)

    close_add_to_home()

    sleep(3)

    close_notification()

    new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
    sleep(1.5)
    autoit.win_active("Open")
    sleep(2)
    autoit.control_send("Open","Edit1", image_path[ctr])
    sleep(1.5)
    autoit.control_send("Open","Edit1","{ENTER}")

    sleep(2)

    next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

    sleep(1.5)

    caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
    caption_field.send_keys(caption)

    share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()

    sleep(25)


    driver.close()


while datetime.now() < wakeUpTime:
    pass

else:

    ans = 's'
    while ans == "s":
        playsound.playsound(r"C:\Users\Malhaar\Desktop\Python Projects\instaclock\alarm.mp3")
        ans = input("d/s: ")
        ans = ans.lower()
        if ans == "s":
            ctr += 1
            post(ctr)
            sleep(300)
        elif ans == "d":
            exit()
        else:
            print("That is not a valid answer")
            print("I'll take that as a snooze then.")
            ans = "s"
            sleep(300)
