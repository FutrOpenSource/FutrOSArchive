#(c) FutrOS 2020. All rights reserved.
#Last updated: 05/27/2023
#It is illegal to redistribute or rebrand this software without author permission.

import os

print ("""
    ███████╗██╗░░░██╗████████╗██████╗░  ░█████╗░░██████╗
    ██╔════╝██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
    █████╗░░██║░░░██║░░░██║░░░██████╔╝  ██║░░██║╚█████╗░
    ██╔══╝░░██║░░░██║░░░██║░░░██╔══██╗  ██║░░██║░╚═══██╗
    ██║░░░░░╚██████╔╝░░░██║░░░██║░░██║  ╚█████╔╝██████╔╝
    ╚═╝░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░╚═════╝░   BETA 1.1.0
          (c) 2020 Futr. All rights reserved.
""")

print (""" 
[1] Continue with setup
[2] I've already done setup
""")

setup = input ("[?]:")
if setup == '1':
        name = input(str("Enter your name: "))
        pas  = input(str("Create a password: "))
        email = input(str("Enter your email: "))
        phone = input(str("Enter your phone: "))

        with open('username.txt' , 'w') as f:
            f.write(name)

print (f"[1] About [2] Apps [3] Release Notes\n©2020 Futr. All rights reserved. ")
setup = input ("[?]: ")

if setup ==  '1':
        print ("""   
    ╔═══╦╗───────╔╗     
    ║╔═╗║║──────╔╝╚╗
    ║║─║║╚═╦══╦╗╠╗╔╝
    ║╚═╝║╔╗║╔╗║║║║║
    ║╔═╗║╚╝║╚╝║╚╝║╚╗
    ╚╝─╚╩══╩══╩══╩═╝  

    ███████╗██╗░░░██╗████████╗██████╗░  ░█████╗░░██████╗
    ██╔════╝██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
    █████╗░░██║░░░██║░░░██║░░░██████╔╝  ██║░░██║╚█████╗░
    ██╔══╝░░██║░░░██║░░░██║░░░██╔══██╗  ██║░░██║░╚═══██╗
    ██║░░░░░╚██████╔╝░░░██║░░░██║░░██║  ╚█████╔╝██████╔╝
    ╚═╝░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░╚═════╝░
    BETA Version 1.1.0U 
    ©2020 Futr. All rights reserved. This is a licensed and authentic version of FutrOS.   
    """)
if setup == '2':
       # App name's go here 
       appname1 = "App name not assigned"
       appname2 = "App name not assigned"
       appname3 = "App name not assigned"
       # Manually add more app slots by copying a pasting the 2nd print statement.
       print("""
    
                                                            ╔═══╗
                                                            ║╔═╗║
                                                            ║║─║╠══╦══╦══╗
                                                            ║╚═╝║╔╗║╔╗║══╣
                                                            ║╔═╗║╚╝║╚╝╠══║
                                                            ╚╝─╚╣╔═╣╔═╩══╝
                                                            ────║║─║║
                                                            ────╚╝─╚╝
       """)
       print(f"""
                                                            [1] {appname1}
       """)
       print(f"""
                                                            [2] {appname2}
       """)
       print(f"""
                                                            [3] {appname3}
       """)

#Insert Apps Here
def appname1():
       print("No app data assigned")
def appname2():
       print("No app data assigned")
def appname3():
       print("No app data assigned")

if setup == '3':
       print("""
       
                                                ╔═══╗──╔╗─────────────╔═╗─╔╗──╔╗
                                                ║╔═╗║──║║─────────────║║╚╗║║─╔╝╚╗
                                                ║╚═╝╠══╣║╔══╦══╦══╦══╗║╔╗╚╝╠═╩╗╔╬══╦══╗
                                                ║╔╗╔╣║═╣║║║═╣╔╗║══╣║═╣║║╚╗║║╔╗║║║║═╣══╣
                                                ║║║╚╣║═╣╚╣║═╣╔╗╠══║║═╣║║─║║║╚╝║╚╣║═╬══║
                                                ╚╝╚═╩══╩═╩══╩╝╚╩══╩══╝╚╝─╚═╩══╩═╩══╩══╝
                                                      Welcome to FutrOS v1.1.0!

                                                        Minor Features:
                                          Upgraded Terminal - More commands in terminal.
                                                      Minor Software Fixes
                                    
       """)

if setup == 'routing':
      print ("""
      FutrOS Manual Routing.
      """)
if setup == 'v1':
      print ("""
      Thanks for using FutrOS, we hope you enjoy using v1.0.0!
      """)
if setup == 'codename':
    print("""
      V1
    """)
if setup == 'c':
        print("""
        (c) 2020 Futr. All rights reserved.
        """)
if setup =='switchverlocation':
        print("""
        Version specific location switching isn't available on this device.
        """)
if setup == 'upgrade':
      print ("""
      Upgrade to newer versions of FutrOS at https://bit.ly/futrosupdate.
      """)
if setup ==  'beta':
        print ("""         
This is a beta version of FutrOS
               """)
if setup == 'archive':
        print("""
This version of FutrOS is archived
        """)
if setup == 'ver':
       print("v1.1.0U (Universal)")
if setup == 'verletter':
       print("""
       U - Universal version of FutrOS - Currently installed version
       L - Lite version of FutrOS 
       E - Embedded system version of FutrOS 
       M - Modified version of FutrOS
       """)
if setup == 'verify':
    print("OS version is legitimate.")    
if setup == 'license':
    print("Public Beta License Installed.")
if setup == 'print':
    printopt = input("user: ")
    print(printopt)    
if setup == 'os':
    print("Beta Install")   
if setup == 'sd':
    print(f"""
    Stored Data:
    {name} - Name
    {pas} - Password
    {email} - Email
    {phone} - Phone Number 
    """)   
if setup == 'futr':
    print("""(c) 2020 Futr. All rights reserved. It is illegal to redistribute or rebrand this software without author permission.""")
if setup ==  'help':
        print ("""
All commands:
eos - End of Support Info
Routing - Routing Info
c - Copyright Info for FutrOS 0.1
Upgrade - How to upgrade FutrOS
beta - Beta Info
archive - OS Archive Info
ver - Finds version of FutrOS
verify - Verifies version of FutrOS
license - Shows license info
print - Prints to terminal
os - OS Info
sd - Shows stored data
futr - Shows copyright info
--------------------------------
Commands are case-sensitive. """)
if setup ==  'awesome':
        print ("""

╔══╦╗──────╔╗────────╔╗──────────────────────────╔╗───╔╗─────────╔╗
╚╗╔╣╚╦═╗╔═╦╣╠╗╔╦╦═╦╦╗║╚╦═╗╔═╦═╦═╦═╦╦╦╦╦═╦═╦╦═╗╔╦╦╣╚╦═╗║╚╦═╦╗╔═╦═╦╝║
─║║║║║╬╚╣║║║═╣║║║╬║║║║╔╣╬║║╩╬╗║╔╣╩╣╔╣║║╬║║║║╩╣║║║║║║╬║║║║╩╣╚╣╬║╩╣╬║
─╚╝╚╩╩══╩╩═╩╩╝╠╗╠═╩═╝╚═╩═╝╚═╝╚═╝╚═╩╝╠╗╠═╩╩═╩═╝╚══╩╩╩═╝╚╩╩═╩═╣╔╩═╩═╝
──────────────╚═╝───────────────────╚═╝─────────────────────╚╝
─────╔╗──╔══╗╔╗──╔═╦══╗
╔═╦═╦╝╠═╗║═╦╬╣╚╦╦╣║║══╣
║═╣╬║╬║╩╣║╔╣║║╔╣╔╣║╠══║
╚═╩═╩═╩═╝╚╝╚═╩═╩╝╚═╩══╝

               """)
