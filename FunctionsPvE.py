import FunctionsGeneral as general_func
import time

# Function opens specified location in world map
def open_location_in_world(location = 2):
    general_func.hover_over_world_icon()
    menu_btn = general_func.world_menu_items(location)
    menu_btn.click()
    
# Function returns enemy fight button element or clicks on button. enemy_number - button number from 1 to 4. Number 1 is weakest enemy and number 4 is boss monster.
def expedition_fight_element(enemy_number = 1, click = False):
    enemy_number = str(enemy_number)
    enemy_selection_list = [ '' , '', '', '/html/body/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/div['+ enemy_number +']/div[2]/button', 'div.expedition_box:nth-child('+ enemy_number +') > div:nth-child(2) > button:nth-child(1)']
    if click:
        general_func.find_element(enemy_selection_list).click()
    elif not click:
        return general_func.find_element(enemy_selection_list)

# Function opens specified locations dungeon and selects difficulity (1 - easy or 2 - hard).
def open_dungeon(location = 2, diff = 1):
    open_location_dungeon_btn = [ '' , '', '', '/html/body/div[2]/div/div[4]/ul/li/table/tbody/tr/td[2]/a', '#mainnav > li:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)']
    diff = str(diff)
    difficulity_btn = [ '' , '', '', '/html/body/div[2]/div/div[6]/div/div[2]/div[2]/div/form/table/tbody/tr/td['+ diff +']/input', 'div.contentItem:nth-child(3) > div:nth-child(2) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child('+ diff +') > input:nth-child(1)']
    
    open_location_in_world(location)
    time.sleep(1)
    general_func.find_element(open_location_dungeon_btn, True)
    try:
        general_func.find_element(difficulity_btn, True)
    except:
        print('difficulity already selected')

# Function tries to find enemy fight icon and click on it.
def dungeon_fight(img_number = 12):
    while img_number >= 0:
        try:
            monster_fighting_icon = [ '' , '', '', '/html/body/div[2]/div/div[5]/div/div[2]/div[2]/div/img[' + str(img_number) +']', '#content > div:nth-child(4) > div:nth-child(2) > img:nth-child(' + str(img_number) +')']
            result = general_func.find_element(monster_fighting_icon, True)
            if result:
                break
        except:
            print("could not find Monster: " + str(img_number))
        img_number -= 1

# Function returns array with remaining combat points for expedition and dungeon.
def get_combat_points():
    expedition_points_selection_list = [ 'expeditionpoints_value_point' , '', '', '//*[@id="expeditionpoints_value_point"]', '#expeditionpoints_value_point']
    dungeon_points_selection_list = [ 'dungeonpoints_value_point' , '', '', '//*[@id="dungeonpoints_value_point"]', '#dungeonpoints_value_point']
    try:
        expedition_points = general_func.find_element(expedition_points_selection_list).text
        dungeon_points = general_func.find_element(dungeon_points_selection_list).text
        return [expedition_points, dungeon_points]
    except:
        print('Could not get combat points')
    
# Function checks if default text is writen on buttons and fight is started in dungeon or/and expedition.
# Return: 0 to test one more time. 1 to refill points. 2 to wait for fight cooldown.
def main_combat_funtion(expedition_location, expedition_enemy, dungeon_location):
    default_expedition_button_text = "Eik į ekspediciją"
    default_dungeon_button_text = "Eik į požemius"
    expedition_text_selectors = [ 'cooldown_bar_text_expedition' , '', '', '//*[@id="cooldown_bar_text_expedition"]', '#cooldown_bar_text_expedition']
    dungeon_text_selectors = [ 'cooldown_bar_text_dungeon' , '', '', '//*[@id="cooldown_bar_text_dungeon"]', '#cooldown_bar_text_dungeon']

    # Refresh page to get current expedition and dungeon button text
    general_func.driver.refresh()

    expedition_text_element = general_func.find_element(expedition_text_selectors)
    dungeon_text_element = general_func.find_element(dungeon_text_selectors)
    
    current_dungeon_button_text = str(general_func.get_element_text(dungeon_text_element))
    current_expedition_button_text = str(general_func.get_element_text(expedition_text_element))
    
    if current_expedition_button_text == default_expedition_button_text or current_dungeon_button_text == default_dungeon_button_text:
        if current_expedition_button_text == default_expedition_button_text:
            open_location_in_world(expedition_location)
            time.sleep(1)
            try:
                expedition_fight_element(expedition_enemy, True)
            except:
                print('There were problem fighting in expedition')

        if current_dungeon_button_text == default_dungeon_button_text:
            open_dungeon(dungeon_location)
            time.sleep(1)
            try:
                dungeon_fight()
            except:
                print('There were problem fighting in dungeon')
        return 0
    else:
        action_points = get_combat_points()
        if action_points[0] == '0' and action_points[1] == '0':
            return 1
        else:
            return 2

