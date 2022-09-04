import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_exist_button(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    button.click()
    text1 = browser.find_element(By.CLASS_NAME, "alertinner").text
    assert len(text1) != 0, "Somethong gone wrong. Try to add item again"
    browser.quit()
