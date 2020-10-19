# TwilioChoreSMS
 Python Script to Send Chore Reminders
 
 Instructions:
 -------------
 1. You need to have the Twilio API installed and a Twilio Account.
 2. Login and visit the console/dashboard of your Twilio Account.
 3. Open the credential.py and fill in the necessary information.
 4. If you do not have the upgraded version of Twilio, please verify each phone number you are sending
 messages to.
 5. Note: Inserting the contact information as [Name, Phone Number] is vital! 
       Phone Number should be formatted as such: "+12345678901" No Spaces and Add "+(Country Code)"
 5. Go into the config.txt file and change the "Reminder Date" to your preferred date to send reminders
    as well as adding chores to the chore list in the format: Chore List = chore1,chore2,chore3,etc.
 6. Note: Last Reminder Date should not be changed! It should automatically update from None to a value
       after the first use!
 7. You should be all set to go!

Why I Made This:
----------------
I was interested in the Twilio API and wanted to create a small project with it! Chores are usually a hassle to divy up and so 
I randomized the assignment and sent texts to my roommates so they wouldn't forget! In this project I learn to use the Twilio API
as well as brush up on my file reading and writing skills. One thing to note is the sphagetti code when reading and writing within
my sendSMS.py. I couldn't figure out how to truncate the pre-existing file and write over it without opening and closing two instances.
Though it works, it does look a little repititve. In the future I hope to add a GUI but as of right now, I don't really have time.
Anyways, I hope this was useful to someone(? ... maybe?)

Last Updated: 10/19/2020

