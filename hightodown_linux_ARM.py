import sys
import datetime
import os
import time
import random
import tkinter.messagebox
import platform
import runpy
import math
import socket
#import win32com.client
import subprocess
import hashlib
import psutil
#import plyer.platforms.win.notification
#import pyautogui
#from plyer import notification
alias = [""]
often = 0
allowed = True
i=0
variables = {}
counter = 0
#if len(sys.argv[0]) < 1:
try:
  data=open(sys.argv[1] ,"r")
except:
  

  data=open("Test.htd","r")
  
#else:

s  = data.readlines()
import webbrowser
while allowed == True:
  
 if s[i]=="show_time\n" or s[i]=="show_time;\n":
   print(datetime.datetime.now())
   i=i+1 
 if s[i] == "declare\n" or  s[i]=="declare;\n":
    variables = {s[i+1]:s[i+2]}
    print (variables)
    i = i + 3
 if s[i] == "print\n" or s[i]=="print;\n":
     print (s[i+1].strip("\n"))
     i=i+2
 if s[i]=="input\n" or s[i]=="input;\n":
   input(">>>")
   i=i+1 
 if s[i] == "end\n" or s[i]=="end;\n" or s[i]=="end" or s[i]=="end;":
    break
 if s[i] =="show_input\n" or s[i]=="show_input;\n":
   the_input=input(">>>")
   print (the_input)
   i = i+1
 if s[i] == "system_call\n" or s[i] == "system_call;\n":
   os.system(s[i+1])
   i=i+2
 if s[i] == "sleep\n" or s[i]=="sleep;\n":
   timey = s[i+1]
   time.sleep(int(timey))
   i = i +2
 if s[i] =="msg_box\n" or s[i] == "msg_box;\n":
   tkinter.messagebox.showinfo(title="htd" ,message=s[i+1])
   i=i+2
 if s[i].startswith("//"):
   i=i+1
 if s[i]=="random\n" or s[i]=="random;\n":
   print(random.randint(int(s[i+1]),int(s[i+2])))
   i=i+3
 if s[i]=="show_os\n" or s[i]=="show_os;\n":
   print(platform.system())
   i=i+1
 if s[i]=="openwebsite\n" or s[i]=="openwebsite;\n":
   webbrowser.open(s[i+1])
   i=i+2
 if s[i]=="show_line\n" or s[i]=="show_line;\n":
   print("current line:"+str(i))
   i=i+1
 if s[i]=="restart\n" or s[i]=="restart;\n" or s[i]=="restart" or s[i]=="restart;":
   i=0
 if s[i]=="only_input\n" or s[i]=="only_input;\n":
   f=input(">>>")
   if s[i+1]==f+"\n":
     print("valid")
     i=i+2
   else:
     print("invalid cant continue")
     break
 if s[i]=="make_file\n" or s[i]=="make_file;\n":
   a=open(s[i+1].strip("\n"),"w")
   a.close()
   i=i+2
 if s[i]=="only_file\n"or s[i]=="only_file;\n":
   if os.path.isfile(s[i+1].strip("\n")):
     print("valid:")
     i=i+2
   else:
     print("invalid cant continue")
     break
 if s[i]=="list_files\n" or s[i]=="list_files;\n":#
   print(os.listdir())
   i=i+1
 if s[i]=="write_tofile\n" or s[i]=="write_tofile;\n":
   to_open=open(s[i+1].strip("\n"),"a")
   to_open.write(s[i+2].strip("\n"))
   to_open.close()
   i=i+3
 if s[i] =="py_launch\n" or s[i]=="py_launch;\n":
   runpy.run_path(s[i+1].strip("\n"))
   i=i+2
 if s[i]=="only_if_line_file\n" or s[i]=="only_if_line_file;\n":
   only_open=open(s[i+1].strip("\n"),"r")
   if only_open.readline().strip("\n") == s[i+2].strip("\n"):
     i=i+3
   else:
     print("invalid cant continue")
     break
 if s[i]=="goto\n" or s[i]=="goto;\n":
   i=int(s[i+1].strip("\n"))
 if s[i] =="del_file\n" or s[i]=="del_file;\n":
   os.remove(s[i+1].strip("\n"))
   i=i+2
 if s[i] =="get_cwd\n" or s[i]=="get_cwd;\n":
   print(os.getcwd())
   i=i+1
 if s[i]=="make_dir\n" or s[i]=="make_dir;\n":
   os.mkdir(s[i+1].strip("\n"))
   i=i+2
 if s[i]=="math_pi\n" or s[i]=="math_pi;\n":
   print(math.pi)
   i=i+1
 if s[i]=="math_pow\n" or s[i]=="math_pow;\n":
   print(pow(int(s[i+1]) ,int(s[i+2])))
   i=i+3
 if s[i]=="math_sqrt\n" or s[i]=="math_sqrt;\n":
   print(math.sqrt(int(s[i+1])))
   i=i+2
 if s[i]=="calc_multi\n" or s[i]=="calc_multi;\n":
   print(float(s[i+1])*float(s[i+2]))
   i=i+3
 if s[i]=="calc_minus\n" or s[i]=="calc_minus;\n":
   print(float(s[i+1])-float(s[i+2]))
   i=i+3
 if s[i]=="calc_plus\n" or s[i]=="calc_plus;\n":
   print(float(s[i+1]) + float(s[i+2]))
   i=i+3
 if s[i]=="calc_divide\n" or s[i]=="calc_divide;\n":
   print(float(s[i+1]) / float(s[i+2]))
   i=i+3
 if s[i]=="get_host_name\n" or s[i]=="get_host_name;\n":
   print(socket.gethostname())
   i=i+1
 if s[i]=="computer_voice\n" or s[i]=="computer_voice;\n":
   talker = win32com.client.Dispatch("SAPI.SpVoice")
   talker.Speak(s[i+1].strip("\n"))
   i=i+2
 if s[i]=="call_exe\n" or s[i]=="call_exe;\n":
   subprocess.call(s[i+1].strip("\n"))
   i=i+2
 if s[i].startswith("#") or s[i].startswith("//"):
   i=i+1
 if s[i] =="to_bin\n" or s[i]=="to_bin;\n":
   print(bin(int(s[i+1])))
   i=i+2
 if s[i]=="to_hex\n" or s[i]=="to_hex;\n":
   print(hex(int(s[i+1])))
   i=i+2
 if s[i]=="to_oct\n" or s[i]=="to_oct;\n":
   print(oct(int(s[i+1])))
   i=i+2
 if s[i]=="hash_md5\n" or s[i]=="hash_md5;\n":
   string = s[i+1].strip("\n")
   string_hash = hashlib.md5(string.encode())
   print(string_hash.hexdigest())
   i=i+2
 if s[i]=="hash_sha256\n" or s[i]=="hash_256;\n":
   To_hash = s[i+1].strip("\n")
   String_to_hash = hashlib.sha256(To_hash.encode())
   print(String_to_hash.hexdigest())
   i=i+2
 if s[i]=="show_battery_percent\n" or s[i]=="show_battery_percent;\n":
   voltage = psutil.sensors_battery()
   print(voltage.percent)
   i=i+1
 if s[i]=="win_notify\n" or s[i]=="win_notify;\n":
   notification.notify(s[i+1],s[i+2])
   i=i+3
 if s[i]=="make_screenshot\n" or s[i]=="make_screenshot;\n":
   pyautogui.screenshot(s[i+1].strip("\n"))
   i=i+2
 if s[i] =="set_alias\n" or s[i]=="set_alias;\n":
   alias[0] = s[i+1].strip("\n")
   i = i + 2
 if s[i] =="print_alias\n" or s[i]=="print_alias;\n":
   print(alias[0])
   i=i+1
 if s[i] =="input_in_alias\n" or s[i]=="input_in_alias;\n":
   alias_input = input(">>>")
   alias[0] = alias_input
   i=i+1
 if s[i] =="openwebsite_alias\n" or s[i]=="openwebsite_alias;\n":
   webbrowser.open(alias[0])
   i=i+1
 if s[i] =="notify_alias\n" or s[i]=="notify_alias;\n":
    notification.notify("Alias" ,alias[0])
    i=i+1
 if s[i] =="only_input_alias\n" or s[i] == "only_input_alias;\n":
   only_alipu = input(">>>")
   if only_alipu == alias[0]:
     i=i+1
   else:
      print("invalid cant continue")
      break
 if s[i] =="computer_voice_alias\n" or s[i] == "computer_voice_alias;\n":
   sayer = win32com.client.Dispatch("SAPI.SpVoice")
   sayer.speak(alias[0])
   i=i+1
 if s[i] =="clear_alias\n" or s[i]=="clear_alias;\n":
   alias[0] = ""
   i = i +1
 if s[i] == "only_alias_num\n" or s[i] =="only_alias_num;\n":
   if alias[0].strip("\n").isnumeric():
     i=i+1
   else:
     break
 if s[i] == "sleep_alias\n" or s[i] == "sleep_alias;\n":
   time.sleep(int(alias[0]))
   i=i+1
 if s[i] =="only_alias\n" or s[i] == "only_alias;\n":
   if alias[0] == s[i+1].strip("\n"):
     i=i+2
   else:
     print("invalid  cant continue")
     break
 if s[i] =="random_in_alias\n" or s[i] == "random_in_alias;\n":
   alias[0] = random.randint(int(s[i+1]),int(s[i+2]))
   i=i+3


   
 if s[i] =="only_alias_else_jump\n" or s[i] =="only_alias_else_jump;\n":
  if s[i+1].strip("\n") == alias[0]:
     i=i+3
  else:
     i=int(s[i+2].strip("\n"))
     else_state=True
 if s[i] =="only_alias_endswith\n" or s[i] == "only_alias_endswith;\n":
   if alias[0].endswith(s[i+1].strip("\n")):
     print("valid")
     i=i+2
   else:
     print("invalid cant continue")
     break
 if s[i]=="hash_md5_alias\n" or s[i]=="hash_md5_alias;\n":
   string2 = alias[0].strip("\n")
   string_hash2 = hashlib.md5(string2.encode())
   print(string_hash2.hexdigest())
   i=i+1
 if s[i] =="hash_sha256_alias\n" or s[i]=="hash_sha256_alias;\n":
   hashingstring = alias[0].strip("\n")
   string_hash3 = hashlib.sha256(hashingstring.encode())
   print(string_hash3.hexdigest())
   i=i+1
 if s[i]=="set_counter\n" or s[i]=="set_counter;\n":
   counter = int(s[i+1])
   i=i+2
 if s[i] =="increase_counter\n" or s[i]=="increase_counter;\n":
   counter = counter + int(s[i+1])
   i=i+2
 if s[i] =="decrease_counter\n" or s[i]=="decrease_counter;\n":
   counter = counter - int(s[i+1])
   i=i+2
 if s[i]=="only_counter_is\n" or s[i]=="only_counter_is;\n":
   if counter == int(s[i+1]):
     i=i+2
   else:
     print("Invalid cant continue")
     break
 if s[i]=="only_counter_lower\n" or s[i]=="only_counter_lower;\n":
   if counter < int(s[i+1]):
     i=i+2
   else:
     print("Invalid cant continue")
     break
 if s[i]=="only_counter_higher\n" or s[i]=="only_counter_higher;\n":
   if counter > int(s[i+1]):
     i=i+2
   else:
     print("Invalid cant continue")
     break
   
data.close()
 
     

  
 
 
   
   
   
   
   
   
   
   

   
   

   
   
   

  
 

   
  
 
  
   
   
   
   
 

  
   
 
 
   

 
   
 
   

 
  
   
  
 

 
    

