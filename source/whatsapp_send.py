import pywhatkit as wp
phone = input("phone > ")
message = input("message > ")
wp.sendwhatmsg(phone, message, 10, 30)