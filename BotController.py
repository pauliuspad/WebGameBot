import FunctionsGeneral     as general_func
import FunctionsController  as controller_func
import FunctionsWork        as work_func
import FunctionsPvE         as pve_func

import time, math
from datetime import datetime, timedelta  
 
# Set option to 11 for auto fight or 12 for auto work at the start of the program 
option = 0
times = -1
time_option = 0

# Open new crome window and fully open the game
general_func.open_browser_and_game(option)

# Login to the game and proceed to the main game window
controller_func.start_the_game()

# Option 1 for combat
# Option 2 for work
while True:
    if option == 0:
        controller_func.programs_main_menu_options()
        try:
            option = int(input("choose option: "))
        except:
            print('You entered not a number')
            option = 0
            continue
        print ("You chose option: " + str(option) )
    

    elif option == 1:
        while option == 1:
            try:
                combat_option = pve_func.main_combat_funtion(5, 1, 4)
                            
                if combat_option == 0:
                    continue
                elif combat_option == 1:
                    print('controller 1')
                    work_hours = 8
                    function_value = controller_func.process_the_job(work_hours)   
                    if function_value == 1:
                        total_work_time = work_func.time_to_wait_until_work_is_done(1 ,work_hours)
                        print('Waiting for: ' + str(total_work_time) + ' seconds')
                        time.sleep(total_work_time)
                        continue
                elif combat_option == 2:
                    print('controller 2')

                    cooldown_time = general_func.shortest_time_to_wait(2)
                    print('Waiting for: ' + str(cooldown_time) + ' seconds')
                    time.sleep(cooldown_time)  
                    continue
                else:
                    print('Combat option ' + str(combat_option))
                    option = 0
            except:
                try:
                    print('controller comfim_popups')
                    time.sleep(5)
                    general_func.comfim_popups()
                except:
                    print('Failed option 1')
            

    elif option == 2:
        controller_func.global_set_work_times(times) 
        while option == 2:
            try:
                if time_option == 0:
                    print('Chose work interval from 1 to 8 (hours). To go back to the menu enter 88')
                    time_option = int(input("hours: "))
                    
                elif time_option != 0 and time_option != 88:
                    while True:
                        function_value = controller_func.process_the_job(time_option)   
                        if function_value == 1:
                            total_work_time = work_func.time_to_wait_until_work_is_done()
                            print('seconds: ' + str(total_work_time))
                            
                            time.sleep(total_work_time)

                        elif function_value == 88:
                            option = 0
                            break 

                elif time_option == 88:
                    controller_func.global_set_work_times() 
                    option = 0
            except:
                try:
                    print('controller comfim_popups1')
                    time.sleep(5)
                    general_func.comfim_popups()
                except:
                    print('Failed option 2')


    elif option == 9:
        print ("Stopping program")
        general_func.stop_program()
    
    elif option == 11:
        option = 1
    
    elif option == 12:
        option = 2
        time_option = 8

    else:
        print('There is no such option' + str(option))
        option = 0

