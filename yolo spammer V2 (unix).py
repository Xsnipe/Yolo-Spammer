#Command Line Yolo spammer
#by Xsnipe
#amos Xsnipe
#insta @j_bowers10

from selenium import webdriver
import time
import os

print('''\u001b[34m
                                                                                                                                
     ██╗   ██╗ ██████╗ ██╗      ██████╗     ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
     ╚██╗ ██╔╝██╔═══██╗██║     ██╔═══██╗    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
      ╚████╔╝ ██║   ██║██║     ██║   ██║    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
       ╚██╔╝  ██║   ██║██║     ██║   ██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
        ██║   ╚██████╔╝███████╗╚██████╔╝    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
        ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝     ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝             
                                                 \u001b[37m
                                                 By Xsnipe
                                     insta @j_bowers10 amos @Xsnipe1231

''')
#user input
url = input('     Enter Target Url Yolo: ')
message = input('     Enter message for yolo: ')
amount = input('     Enter the amount of messages you would like to spam: ')
nums = int(amount)
os.system("clear")

for count in range(1,nums +1):
    driver=webdriver.Chrome()
    
    #find yolo
    driver.get(url)

    #enter phrase and submit
    typebox = driver.find_element_by_xpath('//*[@id="text"]')
    typebox.send_keys(message)

    sendbutton = driver.find_element_by_xpath('//*[@id="send-button"]')
    sendbutton.click()
    
    #close chrome window after 2 seconds
    time.sleep(2)
    os.system("killall -9 chromium")

#finished
print("     spam finished the message " + message + " was entered " + amount + " times")
time.sleep(3)
os.system("clear")
print('''\u001b[34m
     ██████╗  ██████╗ ███╗   ██╗███████╗   
     ██╔══██╗██╔═══██╗████╗  ██║██╔════╝   
     ██║  ██║██║   ██║██╔██╗ ██║█████╗     
     ██║  ██║██║   ██║██║╚██╗██║██╔══╝     
     ██████╔╝╚██████╔╝██║ ╚████║███████╗██╗
     ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝
\u001b[37m
''')
time.sleep(3)
os.system("clear")
time.sleep(1)
os.system("exit")