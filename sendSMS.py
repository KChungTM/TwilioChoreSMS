from twilio.rest import Client
from credentials import account_sid, auth_token, my_twilio, phone_Nums
from datetime import date
import random

try:
    # READS CONFIG FILE FOR CONTENT
    file = open("config.txt", "r")
    content = file.readlines()
    file.close()

    # CLEANS UP CONTENT
    content[4] = content[4].split("=")[1].strip()
    content[5] = content[5].split("=")[1].strip()

    # ASSIGNS VARIABLES BASED ON CONFIG
    reminder_day = content[4]
    if content[5] != "None":
        last_sent = content[5].split("=")
        last_sent = date(int(last_sent[0]), int(last_sent[1]), int(last_sent[2]))
    else:
        last_sent = None

    # CHECKS THE DATE AND LAST REMINDER SENT
    current_date = date.today()
    if (last_sent is None or last_sent != current_date) and current_date.strftime('%A').lower() == reminder_day.lower():
        # INITIALIZES CLIENT (YOU CAN IGNORE!)
        client = Client(account_sid, auth_token)

        # ENTER THE CHORES YOU WANT TO ASSIGN HERE
        # (SEPARATE BY COMMAS AND USE QUOTES FOR EACH ITEM)
        chore_list = content[6].split("=")
        chore_list = chore_list[1].split(",")
        chore_list = [chore_list[index].strip() for index in range(len(chore_list))]
        chore_list_copy = list(chore_list)

        # RANDOMIZES CHORES AND CREATES MESSAGE
        message = "{} {}, {} This Week's Chores:\n--------------------".format(current_date.strftime('%B'),
                                                                               current_date.day,
                                                                               current_date.year)
        for people in phone_Nums:
            chore = random.choice(chore_list_copy)
            message += "\n{}: {}".format(people[0], chore)
            chore_list_copy.remove(chore)

        # SENDS MESSAGE TO EACH PERSON
        for phone in phone_Nums:
            client.messages.create(to=phone[1], from_=my_twilio, body=message)
        print("Sent reminder to all people...")

        config = "Reminder Date = {}\nLast Reminder Date = {},{},{}\n".format(reminder_day,
                                                                            current_date.year,
                                                                            current_date.month,
                                                                            current_date.day)
        chores = "Chore List = " + ','.join(chore_list)

        # REWRITES FILE
        file = open("config.txt", "w")
        file.truncate()
        file.write(content[0]+content[1]+content[2]+content[3]+config+chores)
        file.close()

        print("Successfully read/wrote file...")
    else:
        print("Not Yet Time to Send Reminder")
except IndexError:
    print("Please Double Check config.txt Only Contains \"Remind Date\" and \"Last Reminder Sent\"")
