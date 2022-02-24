# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import pytest
from selenium.webdriver.common.by import By


def testar_my_demo_app():
    ambiente = 'saucelasssbs'

    if ambiente == 'saucelabs':
        caps = {
            "platformName": "Android",
            "appium:platformVersion": "9.0",
            'browserName': '',
            "appium:deviceName": "Samsung Galaxy S9 FHD GoogleAPI Emulator",
            "appium:deviceOrientation": "portrait",
            "appium:app": "storage:filename=mda-1.0.10-12.apk",
            "appium:appPackage": "com.saucelabs.mydemoapp.android",
            "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
        }

        driver = webdriver.Remote(
            "https://oauth-horleylamorim-0788b:9aba8f05-e98e-436c-bf64-2f4675c8d668@ondemand.us-west-1.saucelabs.com:443/wd/hub",
            caps)
    else:  # Local
        caps = {
            "platformName": "Android",
            "appium:platformVersion": "10",
            "appium:automationName": "UiAutomator2",
            "browserName": "",
            "appium:deviceName": "emulator-5554",
            "appium:deviceOrientation": "portrait",
            "appium:appPackage": "com.saucelabs.mydemoapp.android",
            "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
        }
        driver = webdriver.Remote("127.0.0.1:4723", caps)

    el1 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"Displays selected product\"])[1]")
    el1.click()

    el3 = driver.find_element_by_accessibility_id("com.saucelabs.mydemoapp.android:id/priceTV")
    el3.click()
    TouchAction(driver).press(x=927, y=2073).move_to(x=967, y=1313).release().perform()

    el4 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"Displays color of product\"])[4]")
    el4.click()
    el5 = driver.find_element_by_accessibility_id("Increases number of products")
    el5.click()
    el6 = driver.find_element_by_accessibility_id("Tap to add product to cart")
    el6.click()
    el7 = driver.find_element_by_accessibility_id("com.saucelabs.mydemoapp.android:id/cartTV")
    el7.click()
    el8 = driver.find_element_by_accessibility_id("com.saucelabs.mydemoapp.android:id/productTV")
    el8.click()
    el9 = driver.find_element_by_accessibility_id("com.saucelabs.mydemoapp.android:id/titleTV")
    el9.click()
    el10 = driver.find_element_by_accessibility_id("com.saucelabs.mydemoapp.android:id/priceTV")
    el10.click()

    el11 = driver.find_element_by_accessibility_id("Displays color of selected product")
    el11.click()
    el12 = driver.find_element_by_accessibility_id("com.saucelabs.mydemoapp.android:id/noTV")
    el12.click()
    el13 = driver.find_element_by_accessibility_id("com.saucelabs.mydemoapp.android:id/totalPriceTV")
    el13.click()

    driver.quit()
