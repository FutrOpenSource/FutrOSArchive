#(c) 2020 Futr. All rights reserved.#
#It is illegal to redistribute or rebrand this software without Author permission.

print("""
███████╗██╗░░░██╗████████╗██████╗░░█████╗░░██████╗
██╔════╝██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
█████╗░░██║░░░██║░░░██║░░░██████╔╝██║░░██║╚█████╗░
██╔══╝░░██║░░░██║░░░██║░░░██╔══██╗██║░░██║░╚═══██╗
██║░░░░░╚██████╔╝░░░██║░░░██║░░██║╚█████╔╝██████╔╝
╚═╝░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░ 
                    Pre-Dev
      (c) 2020 Futr. All rights reserved
Type a command or find a list of all commands using the 'help' command
          Commands are Case Sensitive.
""")

setup = input("user: ")

  if setup == 'Ver':
    print("Pre-Dev")
    
  if setup == 'Verify':
    print("OS version is legitimate.")
    
  if setup == 'License':
    print("Pre-Dev Beta License Installed.")
  
  if setup == 'print':
    printopt = input("user: ")
    print(printopt)
    
  if setup == 'OS':
    print("Pre-Dev Install")
   
  if setup == 'SD':
    print("No stored data found.")
   
  if setup == 'Futr':
    print("""(c) 2020 Futr. All rights reserved. It is illegal to redistribute or rebrand this software without Author permission.""")
   
  if setup == 'Awesome':
    print("""
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
    
  if setup == 'help':
    print("""
    Ver - Finds version of FutrOS
    Verify - Verifies version of FutrOS
    License - Shows license info
    Print - Prints to terminal
    OS - OS Info
    SD - Shows stored data
    Futr - Shows copyright info
    "")

