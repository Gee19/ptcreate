#!/usr/bin/env python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://club.pokemon.com/us/pokemon-trainer-club/sign-up/"

page_timeout = 5
date_pick_timeout = 1

def init():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url);

def select_fix():
    driver.set_window_size(500,500)
    driver.maximize_window()

def wait_for_verify_age():
    element_present = EC.presence_of_element_located((By.ID, 'id_country'))
    WebDriverWait(driver, page_timeout).until(element_present)

def wait_for_create_acc():
    element_present = EC.presence_of_element_located((By.ID, 'id_username'))
    WebDriverWait(driver, page_timeout).until(element_present)

def click_dob():
    driver.find_element_by_id("id_dob").click()

def wait_for_date_picker():
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.month + .custom-select-menu'))
    WebDriverWait(driver, date_pick_timeout).until(element_present)

def set_month():
    driver.find_element_by_css_selector(".month + .custom-select-menu").click()
    el = driver.find_element_by_xpath("//ul/li[contains(text(), 'January')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", el)
    el.click()

def set_day():
    driver.find_element_by_css_selector(".year + .custom-select-menu").click()
    el = driver.find_element_by_xpath("//ul/li[contains(text(), '1980')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", el)
    el.click()

def set_country():
    select_fix()
    driver.find_element_by_css_selector("#id_country + .custom-select-menu").click()
    el = driver.find_element_by_xpath("//ul/li[contains(text(), 'Canada')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", el)
    el.click()

def confirm_dob():
    driver.find_element_by_class_name("picker__button--clear").click()

def continue_to_create():
    driver.find_element_by_class_name("continue-button").click()

def opt_out():
    radio = driver.find_element_by_id("id_public_profile_opt_in_1")
    driver.execute_script("arguments[0].click();", radio)

def accept_terms():
    driver.find_element_by_id("id_terms").click()

def set_username(user):
    driver.find_element_by_id("id_username").send_keys(user)

def set_passwords(p):
    driver.find_element_by_id("id_password").send_keys(p)
    driver.find_element_by_id("id_confirm_password").send_keys(p)
    
