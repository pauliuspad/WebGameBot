import FunctionsGeneral as general_functions
import time, random

server_time_multiplyer = 2

# Function to start the job for specified amount of time
def start_work(work_time = 8):
    start_job_btn = [ 'doWork' , '', '', '//*[@id="doWork"]', '#doWork']
    try:
        general_functions.hover_over_city_icon()
        work_btn = general_functions.city_menu_items(1)
        work_btn.click()
    except:
        print("Could not open job page.")

    try:
        select_work_hours = work_hour_selector(work_time)
        select_work_hours.click()
    except:
        print("Could not select hours to work.")

    try:
        general_functions.find_element(start_job_btn, True)
    except:
        print("Could not click on btn to start the job.")

# Function from drop down munu selects specified number of hours 
def work_hour_selector(hour_number):
    hour_number = str(hour_number)
    option_selection_list = [ '' , '', '', '//*[@id="workTime"]/option['+ hour_number +']', '#workTime > option:nth-child('+ hour_number +')']
    try:
        return general_functions.find_element(option_selection_list)
    except:
        print('Could not select option: ' + hour_number)
        return

# Function stops current work that is in progress
def cancel_work():
    cancel_work_btn = [ '' , '', '', '//*[@id="content"]/article/section/table/tbody/tr[3]/td[3]/a', '#content > article > section > table > tbody > tr:nth-child(3) > td:nth-child(3) > a']
    confirm_cancellation_btn = [ 'link' , '', '', '//*[@id="link"]', '#link']
    try:
        general_functions.find_element(cancel_work_btn, True)
        general_functions.find_element(confirm_cancellation_btn, True)
    except:
        print("could not cancel work")

# Function to time element in work page
def work_time_text_element(check_times = 5):
    index = 1
    time_field_selection_list = [ '' , '', '', '//*[@id="content"]/article/section/table/tbody/tr[3]/td[2]/span', '#content > article > section > table > tbody > tr:nth-child(3) > td:nth-child(2) > span']
    try:
        while index <= check_times:
            time.sleep(3)
            work_time_element = general_functions.find_element(time_field_selection_list)
            if not work_time_element:
                print("cound not find work time element " + index + " times")
            else:
                return work_time_element
            index += 1
    except:
        print("Error: cound not find work time element")
        return

# Function calculates time in second and if needed adds delay.
def time_to_wait_until_work_is_done(option = 0, passed_time = 0):
    if option == 0:
        # Work delay in minutes
        work_max_delay = 5
        work_min_delay = 2
        delay = random.randint(work_min_delay, work_max_delay) * 60

        try:
            work_time = work_time_text_element()
        except:
            print('Failed to find time element')
            if not work_time:
                return

        try:
            split_work_time = general_functions.get_element_text(work_time).split(":")
        except:
            print("Time split was not successful.")

    elif option == 1:
        hours = passed_time / server_time_multiplyer
        time_in_seconds = hours * 3600
        return time_in_seconds

    elif option == 2:
        split_work_time = passed_time
        delay = 5
        
    try:
        work_time_hours   = int(split_work_time[0])
        work_time_minutes = int(split_work_time[1])
        work_time_seconds = int(split_work_time[2])
        
        time_in_seconds = work_time_hours * 3600 + work_time_minutes * 60 + work_time_seconds + delay
        
        # returns total wait time in seconds
        return time_in_seconds
    except:
        print("failed to calculate time")
