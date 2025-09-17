import schedule
import time

def sudo_placement():
    print("Running sudo placement...")

def good_luck():
    print("Running good luck...")

def work():
    print("Running work...")

def bedtime():
    print("Running bedtime...")

def geeks():
    print("Running geeks...")

# Schedule the tasks
schedule.every(1).minutes.do(geeks)

schedule.every().hour.do(geeks)

schedule.every().day.at("00:00").do(bedtime)

schedule.every(2).to(3).minutes.do(work)

schedule.every().monday.do(good_luck)

schedule.every().tuesday.at("18:00").do(sudo_placement)


while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for a second to avoid busy waiting