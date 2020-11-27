from selenium                                   import webdriver
from selenium.webdriver.common.keys             import Keys
from selenium.webdriver.common.action_chains    import ActionChains
from selenium.webdriver.support.ui              import WebDriverWait

from random             import randrange
from datetime           import datetime , timedelta
from FunctionsWork      import time_to_wait_until_work_is_done

import sys, time 
from Login import email, password
from Path import PATH

driver = webdriver.Chrome(PATH)

# Opens given URL in given browser
def open_browser_and_game(window_option):
    URL = "https://s16-lt.gladiatus.gameforge.com/game/index.php?mod=overview&login=1&sh=d302fbbb7f6e736948e182c3125e86e9"
    driver.get(URL)

    if window_option >= 10:
        driver.fullscreen_window()
        time.sleep(2)
    else:
        driver.maximize_window()
        time.sleep(2)

def stop_program():
    driver.quit()
    sys.exit("Program clossed")

# Function to find given element if needed click on it.
# Element_selectors is array. element_selectors = [ 'id' , 'name', 'one specific id class name', 'xpah', 'css selector']
# In array program tries to find element by 'id' , 'name', 'one specific id class name', 'xpah', 'css selector'
def find_element(element_selectors, click = False, input_text = ''):
    selection_function_list = [ driver.find_element_by_id , driver.find_element_by_name, driver.find_element_by_class_name, driver.find_element_by_xpath, driver.find_element_by_css_selector]
    try:
        for selector, selection_function in zip(element_selectors, selection_function_list):
            if selector != '':
                try:
                    if input_text != '':
                        selection_function(selector).send_keys(input_text)
                        break
                    elif click:
                        selection_function(selector).click()
                        return True
                    elif not click:
                        return selection_function(selector)
                except:
                    print("could not find element: " + selector)
            else:
                continue
        raise NameError('Failed the cycle of finding element')
    except:
        print("Failed to find element: ")
        print(*element_selectors)
        return False
   
# Function to insert login data and login to the game
def login_function():
    open_login_form_btn = [ '' , '', '', '//*[@id="loginRegisterTabs"]/ul/li[1]', '#loginRegisterTabs > ul > li:nth-child(1) > span']
    email_selection_list = [ '' , 'email', '', '//*[@id="loginForm"]/div[1]/div/input', '#registerForm > div:nth-child(1) > div > input[type=email]']
    password_selection_list = [ '' , 'password', '', '//*[@id="loginForm"]/div[2]/div/input', '#loginForm > div:nth-child(2) > div > input[type=password]']
    login_btn = [ '' , '', '', '//*[@id="loginForm"]/p/button[1]', '#loginForm > p > button.button.button-primary.button-lg']
    try:
        find_element(open_login_form_btn, True)

        email_input = find_element(email_selection_list, False , email)
        password_input = find_element(password_selection_list, False, password)

        find_element(login_btn, True)
        return True
    except:
        print("Failed to login")
        return False

# Function that goes to the last played game server
def last_game():
    previous_game_btn = [ '' , '', '', '//*[@id="joinGame"]/button', '#joinGame > a > button']
    try:
        find_element(previous_game_btn, True)
        return True
    except:
        print("there is no last played game")
        return False

# Function to change window that is opened
def change_window(position = 1):
    try:
        driver.switch_to_window(driver.window_handles[position])
        return True
    except:
        print("could not change window")
        return False

# Function to collect dayly bolus
def dayly_bonus():
    dayly_bonus_btn = [ 'linkLoginBonus' , '', '', '//*[@id="linkLoginBonus"]', '#linkLoginBonus']
    try:
        find_element(dayly_bonus_btn, True)
        return True
    except:
        print("There is no dayly bonus promt")
        return False

# Function to mouse over the city meniu icon to show city menu
def hover_over_city_icon():
    city_icon_selection_list = [ '' , '', '', '//*[@id="submenuhead2"]/div[1]/a', '#submenuhead1 > div.menutab_city > a']
    try:
        city_icon_element = find_element(city_icon_selection_list)
        ActionChains(driver).move_to_element(city_icon_element).perform()
    except:
        print("city tab menu is opened or there is no menu")

# Function to mouse over the world menu icon to show city menu
def hover_over_world_icon():
    menu_world_icon = [ '' , '', '', '//*[@id="submenuhead1"]/div[2]/a', '#submenuhead1 > div.menutab_country > a']
    try:
        menu_world_icon_element = find_element(menu_world_icon)
        ActionChains(driver).move_to_element(menu_world_icon_element).perform()
    except:
        print("city tab menu is opened or there is no menu")


# Function returns specified city menu button
# Possition 1 is button to open work page. 
def city_menu_items(menu_btn_number):
    menu_btn_number = str(menu_btn_number)
    work_btn_selection_list = [ '' , '', '', '//*[@id="submenu1"]/a['+ menu_btn_number +']', '#submenu1 > a:nth-child('+ menu_btn_number +')']
    try:
        return find_element(work_btn_selection_list)
    except:
        print('could not find element 1')
        return

# Function returns specified world menu button
# Possition 1 is button to open hermit page. 
def world_menu_items(menu_btn_number):
    menu_btn_number = str(menu_btn_number)
    forest_btn_selection_list = [ '' , '', '', '//*[@id="submenu2"]/a['+ menu_btn_number +']', '#submenu2 > a:nth-child('+ menu_btn_number +')']
    try:
        return find_element(forest_btn_selection_list)
    except:
        print('could not find element 1')
        return

# Function to get text that is in given element
def get_element_text(element):
    try:
        return element.text
    except:
        print('could not get text')
        return

# Function to get text from main fighting menu. Needed text is located in four buttons.
# btn_number = 1 (expedition), 2 (dungeon), 3 (arena), 4 (circus turma)
def main_fighting_menu_text(btn_number = 1):
    if btn_number == 1:
        expedition_text_selection_list = [ 'cooldown_bar_text_expedition' , '', '', '//*[@id="cooldown_bar_text_expedition"]', '#cooldown_bar_text_expedition']
        return find_element(expedition_text_selection_list).text

    elif btn_number == 2:
        dungeon_text_selection_list = [ 'cooldown_bar_text_dungeon' , '', '', '//*[@id="cooldown_bar_text_dungeon"]', '#cooldown_bar_text_dungeon']
        return find_element(dungeon_text_selection_list).text

    elif btn_number == 3:
        arena_text_selection_list = [ 'cooldown_bar_text_dungeon' , '', '', '//*[@id="cooldown_bar_text_dungeon"]', '#cooldown_bar_text_dungeon']
        return find_element(arena_text_selection_list).text

    elif btn_number == 4:
        circus_text_selection_list = [ 'cooldown_bar_text_dungeon' , '', '', '//*[@id="cooldown_bar_text_dungeon"]', '#cooldown_bar_text_dungeon']
        return find_element(circus_text_selection_list).text

# Function returns shortest time left to fight again
# max_fight_menu_btn - till which button check shortest time ( max 4)
# min_fight_menu_btn - from which button check shortest time ( max 4)
def shortest_time_to_wait(max_fight_menu_btn, min_fight_menu_btn = 0):
    seconds = 0

    if min_fight_menu_btn == 0:
        index = 1
        max_index = max_fight_menu_btn
    else:
        index = min_fight_menu_btn
        max_index = max_fight_menu_btn

    while index <= max_index:
        time_left = main_fighting_menu_text(index).split(':') 
        print(*time_left)
        tmp_seconds = time_to_wait_until_work_is_done(2, time_left)
        print(tmp_seconds)
        
        if seconds == 0 or tmp_seconds < seconds:
            seconds = tmp_seconds
        index += 1
    
    return seconds

def level_up_notification():
    lvl_up_menu_btn = [ 'linknotification' , '', '', '//*[@id="linknotification"]', '#linknotification']
    find_element(lvl_up_menu_btn, True)

def armor_peace_notification():
    armor_peace_popup_btn = [ 'linkcancelnotification' , '', '', '//*[@id="linkcancelnotification"]', '#linkcancelnotification']
    find_element(armor_peace_popup_btn, True)

def mission_completion_notification():
    mission_conpelted_btn = [ 'linkcancelnotification' , '', '', '//*[@id="linkcancelnotification"]', '#linkcancelnotification']
    find_element(mission_conpelted_btn, True)

def comfim_popups():
    try:
        level_up_notification()
    except:
        try:
            armor_peace_notification()
        except:
            try:
                mission_completion_notification()
            except:
                try:
                    dayly_bonus()
                except:
                    try:
                        maintenence_btn = [ '' , '', '', '/html/body/div[2]/div/div[4]/div/section/input', '']
                        if find_element(maintenence_btn):
                            time.sleep(65)
                    except:
                        print('Failed to comfirm notifications')