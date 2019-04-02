from selenium import webdriver
import random
import time

driver = webdriver.Safari()


def join_game():
    wait_time = 0
    nic = "Drink_some_vodka"
    time.sleep(0.1)
    element_pin = driver.find_element_by_id('inputSession')
    element_pin.send_keys(nic)
    element_join = driver.find_element_by_css_selector("button[class='btn btn-greyscale join ng-binding']")
    element_join.click()
    time.sleep(3.5)
    try:
        if input("Continue") == "no":
            try_join()
        else:
            driver.find_element_by_css_selector("span[class='alert__body__msg']")
        #  try to find option
    except:
        print("Waiting for start/ next question ", wait_time * 5, "seconds")
        wait_time += 1


def try_join():
    join = 0
    pin = random.randint(111111, 999999)
    driver.get('https://kahoot.it')
    time.sleep(0.1)
    element_pin = driver.find_element_by_id('inputSession')
    element_pin.send_keys(pin)
    element_join = driver.find_element_by_css_selector("button[class='btn btn-greyscale join ng-binding']")
    element_join.click()
    time.sleep(3.5)
    try:
        driver.find_element_by_css_selector("span[class='alert__body__msg']")

    except:
        print("Joined room1")
        join += 1

    for i in range(1, 1000):
        if join == 0:
            try_join()
        else:
            print("Joined room2")
            join_game()
            break

try_join()
