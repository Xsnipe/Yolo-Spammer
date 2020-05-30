#Command Line Yolo spammer
#by Xsnipe
#amos Xsnipe
#insta @j_bowers10

from selenium import webdriver
import time
import os

print('''
                                                                                                                           
██╗   ██╗ ██████╗ ██╗      ██████╗     ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║     ██╔═══██╗    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
 ╚████╔╝ ██║   ██║██║     ██║   ██║    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
  ╚██╔╝  ██║   ██║██║     ██║   ██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝███████╗╚██████╔╝    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝     ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝             
                                            By Xsnipe
                                insta @j_bowers10 amos @Xsnipe1231

''')
#user input
url = input('Enter Target Url Yolo: ')
message = input('Enter message for yolo: ')
amount = input('Enter the amount of messages you would like to spam: ')
nums = int(amount)

for count in range(1,nums +1):
    driver=webdriver.Chrome()
    
    #find yolo
    driver.get(url)
    print("Target reached")

    #enter phrase and submit
    typebox = driver.find_element_by_xpath('//*[@id="text"]')
    typebox.send_keys(message)
    print("message entered")

    sendbutton = driver.find_element_by_xpath('//*[@id="send-button"]')
    sendbutton.click()
    print("message sent")
    

#finished
print("spam finished the message " + message + " was entered " + amount + " times")
time.sleep(3)
exit()
