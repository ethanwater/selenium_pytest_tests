import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver 
    driver.quit()

def test_google_search(browser):
    try:
        browser.get("https://www.google.com")

        searchbar = browser.find_element(By.NAME, "q")

        actions = ActionChains(browser)
        actions\
            .move_to_element(searchbar)\
            .send_keys("neko")\
            .key_down(Keys.ENTER)\
            .perform()
    except Exception as e:
        pytest.fail(f"error: {e}")

def test_click_button(browser):
    try:
        browser.get("https://uitestingplayground.com/click")
        
        wait = WebDriverWait(browser, 10)
        clickable = wait.until(EC.element_to_be_clickable((By.ID, "badButton")))
        
        actions = ActionChains(browser)
        actions.move_to_element(clickable).click().perform()  # <-- Add perform()
        
        button_color = clickable.value_of_css_property("background-color")
        print(f"Button color after click: {button_color}")
    except Exception as e:
        pytest.fail(f"error: {e}")

def test_text_input(browser):
    try:
        browser.get("https://uitestingplayground.com/textinput")

        textinput = browser.find_element(By.ID, "newButtonName")
        button = browser.find_element(By.ID, "updatingButton")

        mockdata = "cat"
        actions = ActionChains(browser)
        actions\
            .move_to_element(textinput)\
            .click()\
            .send_keys(mockdata)\
            .move_to_element(button)\
            .click()\
            .perform()

        button_text = button.text
        if button.text != mockdata:
            print(0)
        else:
            print(1)
    except Exception as e:
        pytest.fail(f"error: {e}")

@pytest.mark.skip(reason="takes too fuckin long")
def test_client_side_delay(browser):
    try:    
        browser.get("https://uitestingplayground.com/clientdelay")

        trigger_button = browser.find_element(By.ID, "ajaxButton")
        
        actions = ActionChains(browser)
        actions\
            .move_to_element(trigger_button)\
            .click()\
            .perform()

        wait = WebDriverWait(browser, timeout=25).until(
           EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
        )
    
        if browser.find_element(By.CLASS_NAME, "bg-success"):
            print("pass")
        else:
            print("fail")
    except Exception as e:
        pytest.fail(f"error: {e}")

def test_dynamic_id(browser):
    try:
        browser.get("https://uitestingplayground.com/dynamicid")
        button = browser.find_element(By.CLASS_NAME, "btn-primary")
        # print(button.text) just to ensure that we got the right one
    except Exception as e:
        pytest.fail(f"error: {e}")

def test_sample_app_login(browser):
    try:
        browser.get("https://uitestingplayground.com/sampleapp")
        
        username_input = browser.find_element(By.NAME, "UserName")
        password_input = browser.find_element(By.NAME, "Password")
        login_status = browser.find_element(By.ID, "loginstatus")
        login_button = browser.find_element(By.ID, "login")

        mockdata = ["bobbyflay", "pwd"]

        actions = ActionChains(browser)\
            .move_to_element(username_input)\
            .click()\
            .send_keys(mockdata[0])\
            .move_to_element(password_input)\
            .click()\
            .send_keys(mockdata[1])\
            .move_to_element(login_button)\
            .click()\
            .perform()
        
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "loginstatus"))
        )

        assert login_status.get_attribute("class") == "text-success", "rip"
    except Exception as e:
        pytest.fail(f"error: {e}")

def test_visibility(browser):
    try:
        browser.get("https://uitestingplayground.com/visibility")

        hide_button = browser.find_element(By.ID, "hideButton")
        zero_width_button = browser.find_element(By.ID, "zeroWidthButton")
        hiding_layer = browser.find_element(By.ID, "hidingLayer")

        actions = ActionChains(browser)\
            .move_to_element(hide_button)\
            .click()\
            .perform()

        assert WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.ID, "removedButton"))
        ) == False, "removedButton was not removed"
        assert zero_width_button.value_of_css_property("width") == "0px"
        assert hiding_layer.value_of_css_property("background-color") == "rgb(255, 255, 255)"
    except Exception as e:
        print(f"error{e}")


def test_class_attribute(browser):
    try:
        browser.get("https://uitestingplayground.com/classattr")
        blue_button = browser\
            .find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")

        actions = ActionChains(browser)\
            .move_to_element(blue_button)\
            .click()\
            .perform()

        time.sleep(2)

        alert = Alert(browser)
        alert.accept()
    except Exception as e:
        pytest.fail(f"error: {e}")
