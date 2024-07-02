import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN= os.getenv("TOKEN")


def start(update,context):
    update.message.reply_text("""
    Hello welcome to KIIT University Bot.
    
    Presented by :

    SOHAM PATRA (Final year Student Of at B.Tech 
    Computer Science And Engineering at Kiit University)
    

   Address:  Chandaka Industrial Estate, K I I T University, Patia, Bhubaneswar, Odisha 751024
                                                                                              
    To explore further click on ---> /help

    """)


def helps(update,context):
    update.message.reply_text(
        """
        /start - To start the conversation
                   
            Welcome to KIIT
            Which branch information do you want to know about ??


            /Engineering 
            /Medical_Sciences
            /Biotechnology  
            /Law
            /Applied_Science
            /Management
        """
    )

def Engineering (update,context) :
    update.message.reply_text("""
            Welcome to KIIT School of Engineering

            The School of Engineering has got the following branches:


            /Computer Engineering 
            /Electronics Engineering 
            /Electrical Engineering
            /Mechanical Engineering 
            /Civil Engineering
            /Aerospace Engineering
            
                                                                   
    To know detailed information of any School of Engineering ,click on the above options 
    /help """)

def Medical_Sciences (update,context) :
        update.message.reply_text(""".
         To know more about KIMS visit : https://kims.kiit.ac.in/

         Directions : https://tinyurl.com/378bn2dh 
                             
        /help

        
        """)

def Biotechnology (update,context) :
         update.message.reply_text("""
         To know more about School of BioTechnology visit : https://biotech.kiit.ac.in/
         
          Directions : https://tinyurl.com/3jsp3859


          /help
         """)
def Law (update,context) :
         update.message.reply_text("""
         To know more about School of LAW visit : https://law.kiit.ac.in/

          Directions : https://tinyurl.com/5fvs7ua4


          /help
         """)

def Applied_Science (update,context) :
         update.message.reply_text("""


         To know more about Applied Sciences visit : https://ksas.kiit.ac.in/

         Directions :https://tinyurl.com/y25yth2t

         /help
         """)

def Management (update,context) :
         update.message.reply_text("""
         To know more about KSOM visit : https://ksom.ac.in/
         
         Directions : https://tinyurl.com/4fyyakk7


         /help
         """)
def Computer (update,context) :
         update.message.reply_text("""
         To know more about CSE please visit : https://cse.kiit.ac.in/

         Directions : https://tinyurl.com/ywedp3vf


          Where do you want to go from here??
          
          /Electronics_Campus
          /Electrical_Campus
          /Computer_Campus_BLOCK_C
          /Computer_Campus_BLOCK_A__B
          /Law_Campus
          /Medical_Sciences_Campus
          /Applied_Science_Campus
          /Management_Campus

          
          Do you want to another requirements??

          /kings_palace
          /Queens_castle
          /medicine_shop
          /Hotels
          /saloon
          /Food_court
          /Resturants
          /Bar
          /Book_shop



          /help
         """)
def Electronics (update,context) :
         update.message.reply_text("""
         To know more about Electronics please visit : https://electronics.kiit.ac.in/

         Directions : https://tinyurl.com/rh2v2wh4
           

           What do you want to go from here??
                     
            /Computer_Campus_BLOCK_C
            /Electronics_Campus
            /Electrical_Campus
            /Law_Campus
            /Medical_Sciences_Campus
            /Applied_Science_Campus
            /Management_Campus
          
            
         /help
         """)
def Electrical (update,context) :
         update.message.reply_text("""
         To know more about Electrical please visit : https://electrical.kiit.ac.in/

         Directions : https://tinyurl.com/52kr4cjp



          /help
         """)
def Mechanical (update,context) :
         update.message.reply_text("""
         To know more about Mechanical please Visit : https://mechanical.kiit.ac.in/

         Directions : https://tinyurl.com/ysd5utsj


         /help
         """)
def Civil (update,context) :
         update.message.reply_text(""".
         To know more about Civil please vist : https://civil.kiit.ac.in/

         Directions : https://tinyurl.com/2p8zjssf 

          /help 
         """)
def Aerospace (update,context) :
         update.message.reply_text("""
         To know more about Aerospace please vist: https://mechanical.kiit.ac.in/b-tech-aerospace-engineering/

         Directions : https://tinyurl.com/3j5pzub2

          /help 
         """)
def Electronics_Campus (update,context) :
        update.message.reply_text("""
        Directions: https://bit.ly/491dx1X
        

        /help
        """)
def Electrical_Campus (update,context) :
            update.message.reply_text("""
            Directions: https://t.ly/nJcpj
            
            /help
            """)
def Computer_Campus_BLOCK_C (update,context) :
            update.message.reply_text("""
            Directions: https://t.ly/ewJwt
            

            /help
            """)
def Computer_Campus_BLOCK_A__B (update,context) :
            update.message.reply_text("""
             You are already in here. 
            

            /help
            """)
def Law_Campus (update,context) :
                update.message.reply_text("""
                Directions: https://t.ly/d_5xR         


                /help                        
            """)
def Medical_Sciences_Campus (update,context) :
                update.message.reply_text("""
                Directions: https://t.ly/SNzFK           


                /help

             """)
def Applied_Science_Campus (update,context) :
                update.message.reply_text("""
                Directions: https://t.ly/cUWRq         


                 /help

             """)
def Management_Campus (update,context) :
                update.message.reply_text("""
                Directions: https://rb.gy/3uc62     


                 /help                       
             """)
def Aerospace_Campus (update,context) :
                update.message.reply_text("""
                Directions: https://rb.gy/ltkzh     


                 /help                                                           
                """)
def  kings_palace(update,context) :
                update.message.reply_text("""

                Which King's palace you want to go??


                /kings_palace_1
                /kings_palace_2
                /kings_palace_5
                /kings_palace_6
                /kings_palace_7
                /kings_palace_8
                /kings_palace_9
                /kings_palace_15     


                 /help                                                                                               
                """)
def  Queens_castle(update,context) :
                update.message.reply_text("""

                Which King's palace you want to go??


                /Queens_castle_Medical 
                /Queens_castle_Engineering
                /Queens_castle_International
                /Queens_castle_Nursing 
                /Queens_castle_Management 
                /Queens_castle_LAW
                

                /help
                """)
def  Hotels(update,context) :
               update.message.reply_text("""

               Direction: https://rb.gy/t65sd


                /help

                """)
def  saloon(update,context) :
              update.message.reply_text("""

              Direction: https://rb.gy/bpcn1


                /help


                """)
def  Food_court(update,context) :
              update.message.reply_text("""

              Direction: https://rb.gy/3aowv


                /help

                """)
def  Bar(update,context) :
              update.message.reply_text("""

              Direction: https://tinyurl.com/45p3y8pj


                /help

                """)
def  Book_shop(update,context) :
              update.message.reply_text("""

              Direction: https://tinyurl.com/2nahn3cf


                /help

                """)
def  Resturants(update,context) :
              update.message.reply_text("""

              Direction: https://tinyurl.com/399b6ctw


                /help

               """)
def  kings_palace_1(update,context) :
             update.message.reply_text("""
             
              Direction: https://tinyurl.com/bd2rfvee
                /help
            """)
def  kings_palace_2(update,context) :
              update.message.reply_text("""
                           
               Direction: https://tinyurl.com/2yzn6jfp
                /help
            """)
def  kings_palace_5(update,context) :
               update.message.reply_text("""
                            
                Direction: https://tinyurl.com/mw7unb3x
                    /help
            """)
def  kings_palace_6(update,context) :
                update.message.reply_text("""
                             
                Direction: https://tinyurl.com/mpwpf4jb
                /help
            """)
def  kings_palace_7(update,context) :
                 update.message.reply_text("""
                              
                Direction: https://tinyurl.com/23apbfa3
                /help
            """)
def  kings_palace_8(update,context) :
                  update.message.reply_text("""
                               
                  Direction: https://tinyurl.com/yc2f99fk
                 /help
                """)
def  kings_palace_9(update,context) :
                   update.message.reply_text("""
                                
                    Direction: https://tinyurl.com/nezbvhxn
                        /help
                """)
def  kings_palace_15(update,context) :
                   update.message.reply_text("""
                                
                    Direction: https://tinyurl.com/d86trhxp
                    /help
                """)    
def  Queens_castle_Medical(update,context) :
                   update.message.reply_text("""
                                
                    Direction: https://tinyurl.com/4bau2uk2
                /help
                """)
def  Queens_castle_Engineering(update,context) :
                   update.message.reply_text("""
                                
                    Direction: https://tinyurl.com/yj9v657j
                    /help
                """)
def  Queens_castle_International(update,context) :
                   update.message.reply_text("""
                                
                    Direction: https://tinyurl.com/5ahnprn6
                    /help
                """)
def  Queens_castle_Nursing(update,context) :
                   update.message.reply_text("""
                                
                    Direction: https://tinyurl.com/49ftdzx2
                    /help
                """)
def  Queens_castle_Management(update,context) :
                   update.message.reply_text("""
                                
                    Direction: https://tinyurl.com/yu4ffmdn
                    /help
                    """)
def  Queens_castle_LAW(update,context) :
                    update.message.reply_text("""
                                 
                    Direction: https://tinyurl.com/3ktn73h3
                    /help
                """)

updater = telegram.ext.Updater(TOKEN, use_context = True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start',start))
dispatch.add_handler(telegram.ext.CommandHandler('help',helps))
dispatch.add_handler(telegram.ext.CommandHandler('Engineering',Engineering))
dispatch.add_handler(telegram.ext.CommandHandler('Medical_Sciences',Medical_Sciences))
dispatch.add_handler(telegram.ext.CommandHandler('Law',Law))
dispatch.add_handler(telegram.ext.CommandHandler('Applied_Science',Applied_Science))
dispatch.add_handler(telegram.ext.CommandHandler('Management',Management))
dispatch.add_handler(telegram.ext.CommandHandler('Computer',Computer))
dispatch.add_handler(telegram.ext.CommandHandler('Electronics',Electronics))
dispatch.add_handler(telegram.ext.CommandHandler('Electrical',Electrical))
dispatch.add_handler(telegram.ext.CommandHandler('Mechanical',Mechanical))
dispatch.add_handler(telegram.ext.CommandHandler('Civil',Civil))
dispatch.add_handler(telegram.ext.CommandHandler('Aerospace',Aerospace))
dispatch.add_handler(telegram.ext.CommandHandler('Electronics_Campus',Electronics_Campus))
dispatch.add_handler(telegram.ext.CommandHandler('Aerospace_Campus',Aerospace_Campus))
#dispatch.add_handler(telegram.ext.CommandHandler('Civil_Campus',Civil_Campus))
#dispatch.add_handler(telegram.ext.CommandHandler('Mechanical_Campus',Mechanical_Campus))
dispatch.add_handler(telegram.ext.CommandHandler('Electrical_Campus',Electrical_Campus))
#dispatch.add_handler(telegram.ext.CommandHandler('Computer_Campus_BLOCK_A__B',Computer_Campus_BLOCK_A_&_B))
dispatch.add_handler(telegram.ext.CommandHandler('Computer_Campus_BLOCK_C',Computer_Campus_BLOCK_C))
dispatch.add_handler(telegram.ext.CommandHandler('Medical_Sciences_Campus',Medical_Sciences_Campus))
dispatch.add_handler(telegram.ext.CommandHandler('Law_Campus',Law_Campus))
dispatch.add_handler(telegram.ext.CommandHandler('Applied_Science_Campus',Applied_Science_Campus))
dispatch.add_handler(telegram.ext.CommandHandler('Management_Campus',Management_Campus))
dispatch.add_handler(telegram.ext.CommandHandler('kings_palace',kings_palace))
dispatch.add_handler(telegram.ext.CommandHandler('Queens_castle',Queens_castle))
dispatch.add_handler(telegram.ext.CommandHandler('Hotels',Hotels))
dispatch.add_handler(telegram.ext.CommandHandler('saloon',saloon))
dispatch.add_handler(telegram.ext.CommandHandler('Food_court',Food_court))
dispatch.add_handler(telegram.ext.CommandHandler('Bar',Bar))
dispatch.add_handler(telegram.ext.CommandHandler('Book_shop',Book_shop))
dispatch.add_handler(telegram.ext.CommandHandler('Resturants',Resturants))
dispatch.add_handler(telegram.ext.CommandHandler('kings_palace_1',kings_palace_1))
dispatch.add_handler(telegram.ext.CommandHandler('kings_palace_2',kings_palace_2))
dispatch.add_handler(telegram.ext.CommandHandler('kings_palace_5',kings_palace_5))
dispatch.add_handler(telegram.ext.CommandHandler('kings_palace_6',kings_palace_6))
dispatch.add_handler(telegram.ext.CommandHandler('kings_palace_7',kings_palace_7))
dispatch.add_handler(telegram.ext.CommandHandler('kings_palace_8',kings_palace_8))
dispatch.add_handler(telegram.ext.CommandHandler('kings_palace_9',kings_palace_9))
dispatch.add_handler(telegram.ext.CommandHandler('kings_palace_15',kings_palace_15))
dispatch.add_handler(telegram.ext.CommandHandler('Queens_castle_Medical',Queens_castle_Medical))
dispatch.add_handler(telegram.ext.CommandHandler('Queens_castle_Engineering',Queens_castle_Engineering))
dispatch.add_handler(telegram.ext.CommandHandler('Queens_castle_International', Queens_castle_International))
dispatch.add_handler(telegram.ext.CommandHandler('Queens_castle_Nursing', Queens_castle_Nursing))
dispatch.add_handler(telegram.ext.CommandHandler('Queens_castle_Management',Queens_castle_Management))
dispatch.add_handler(telegram.ext.CommandHandler('Queens_castle_LAW',Queens_castle_LAW))

updater.start_polling()
updater.idle()
