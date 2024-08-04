import smtplib
import string
import random
import time
import os
import subprocess

def open_instagram():
    command = "am start -a android.intent.action.VIEW -d instagram://user?username=zerr.ace"
    
    subprocess.run(command, shell=True)


N = 1000


def clear_terminal():
    # Check if the system is Windows or not
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux and macOS

time.sleep(2)

clear_terminal()

print("Follow instagram zeru dulu dong bos! :v")

open_instagram()

time.sleep(5)

input("kalo udah enter ae")

clear_terminal()

time.sleep(2)

print("""\033[31m
       NO!                          MNO!
     MNO!!         [NBK]          MNNOO!
   MMNO!                           MNNOO!!
 MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!
 !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!
       ! MMMMMMMMMMMMMPPPPOOOOIII! !
        MMMMMMMMMMMMPPPPPOOOOOOII!!
        MMMMMOOOOOOPPPPPPPPOOOOMII!
        MMMMM..    OPPMMP    .,OMI!
        MMMM::   o.,OPMP,.o   ::I!!
          NNM:::.,,OOPM!P,.::::!!
         MMNNNNNOOOOPMO!!IIPPO!!O!
         MMMMMNNNNOO:!!:!!IPPPPOO!
          MMMMMNNOOMMNNIIIPPPOO!!
             MMMONNMMNNNIIIOO!
           MN MOMMMNNNIIIIIO! OO
          MNO! IiiiiiiiiiiiI OOOO
     NNN.MNO!   O!!!!!!!!!O   OONO NO!
    MNNNNNO!    OOOOOOOOOOO    MMNNON!
      MNNNNO!    PPPPPPPPP    MMNON!
         OO!                   ON!\033[0m
""")

email = input('masukan Email mu sebagai pengirim spam : ')
target_email = input('Masukan email target mu : ')

subjek = input('Masukan subjek : ')
pesan = input('Masukan Pesan email : ')
spam = input("Apakah kamu mau spam? (y/n) : ")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login("zeruprogram@gmail.com", "fiqi jqbb cfzn qtcp")

teks = f"Subject: {subjek}\n\n{pesan}"

if spam == "y" or spam == "":
    lengthSpam = int(input("berapa kali kamu ingin spam email? : "))
    res = ""
    for x in range(lengthSpam):
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        teks = f"Subject: {str(res)}\n\n{str(res)}"
        server.sendmail(email, target_email, teks)
        print('berhasil mengirim email ke ', x)
else:
    server.sendmail(email, target_email, teks)
    print('berhasil mengirim email!')