import FunctionsGeneral as general_func
import FunctionsWork    as work_func
import time

run_work_times = -1
number_of_times_work_funtion_was_runned = 0

# Function goes thrue all nececary functions to start the game and get to the character screen
def start_the_game():
    finished = False
    while finished == False:
        finished = general_func.login_function()
    time.sleep(1)

    finished = False
    while finished == False:
        finished = general_func.last_game()

    time.sleep(1)
    general_func.change_window()
    time.sleep(1)
    general_func.dayly_bonus()

def programs_main_menu_options():
    print("1: Constant fighting")
    print("2: Only working")
    print("9: stops program")

# Function to reset and set how many times work hase to be runned.
def global_set_work_times(times = -1):
    run_work_times = times
    number_of_times_work_funtion_was_runned = 0


# Function open work page and start work.
def process_the_job(entered_hours):
    close = False

    if not work_func.work_time_text_element(1):
        general_func.hover_over_city_icon()
        general_func.city_menu_items(1)

        work_func.start_work(entered_hours)
        number_of_times_work_funtion_was_runned += 1
        return 1
    else:
        return 1

    if close:
        return 88
