# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

from datetime import datetime, date
from tkcalendar import Calendar, DateEntry
import calendar


""" params = ['eric', 'kang'] """

#--------------------------------------------------------------------------------#

def printLine(params):
    print (cannedGmail(params))

def firstLast(params):
    # Name: John Apple
    # result: john.apple@douglasemmett.com
    return params[0] + "." + params[1] + "@douglasemmett.com"

def firstLastNoEmail(params):
    # Name: John Apple
    # result: john.apple
    return params[0] + "." + params[1]

#--------------------------------------------------------------------------------#

def smtpEmail(params):
    #   If input is eric kang
    #   returns SMTP:eric.kang@douglasemmett.com
    return "SMTP:" + firstLast(params)


def temp_password(cal):
    #   Takes in the selected date from tkcalendar app
    #   returns string of 'mmdd'
    #   ex: May 2nd turns into 0502
    starting_date = DateEntry.get_date(cal)
    start_month_date = starting_date.strftime('%m%d')

    #   DateEntry.get_date returns value of datetime.date()
    #   Format= YYYY-MM-DD
    #   .weekday() returns value of 0 - 6 with 0 being Monday
    #   .day_name[] takes value from above and converts it to actual date    
    date_of_week = calendar.day_name[DateEntry.get_date(cal).weekday()]

    return start_month_date + date_of_week + "?"

#--------------------------------------------------------------------------------#

# Related to Canned Response

def cannedGmail(params):
    name = params[0].capitalize() + " " + params[1].capitalize()
    first_name = params[0].capitalize()    
    canned_response =   '< >,\n\nPlease assist ' + name + ' to access email.\n\nInstruct ' + first_name + ' to go to:\n\nhttps://www.gmail.com\n\n' \
                        'The email address assigned is:\n\n' + firstLast(params) + '\n\nand the temporary password is:\n\n/Temp_Password/\n\n' \
                        'It will force ' + first_name + ' to change the password.\n\nOne of these two 8 digit backup codes will be needed to access the account:\n\n' \
                        'BACKUPCODE1\nBACKUPCODE2\n\n' \
                        'Since 2 Step Verification is mandatory but not yet enforced, please assist ' + first_name + ' by enrolling the cell phone and turning on 2 Step verification.\n\n' \
                        'All the necessary credentials were sent via email to the applications that ' + first_name + ' will need.\n\n' \
                        'Should you have any questions, please call 424.234.3578 or email techsupport@douglasemmett.com.\n\n' \
                        'Thank you very much.'
    return canned_response

def cannedNexus():
    canned_reponse =    'Your password for account USER has been set to the temporary password: 2024@Douglas\n\n' \
                        'Click here to login into Nexus.\n\n When you log in, Nexus will prompt you to change your password..\n\n' \
                        'Let me know if you have any questions.'
    return canned_reponse

def cannedMRI():

    return None

""" printLine(params) """