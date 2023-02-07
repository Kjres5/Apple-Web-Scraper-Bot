import requests
import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import time
import yaml

global bot
global TOKEN
global productAvail
productAvail = False

stream = open("config.yaml", 'r')
dictionary = yaml.load(stream, Loader=yaml.FullLoader)

TOKEN = dictionary["BOT_TOKEN"]
bot = telepot.Bot(TOKEN)


def handle(msg):
    pprint(msg)


MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while True:
    url = "https://www.apple.com/sg/shop/configUpdate/MPHE3ZP/A?node=home%2Fshop_mac%2Ffamily%2Fmacbook_pro%2Fconfig&option.processor_and_graphics_aos_phantom_z17g=065-CDW1&option.memory_aos_phantom_z17g=065-CDW6&option.hard_drivesolid_state_drive_aos_phantom_z17g=065-CDWC&option.power_adapter_aos_phantom_z17g=065-CDWJ&option.keyboard_and_documentation_z17g=065-CFDJ&option.sw_final_cut_pro_z17g=065-CF1L&option.sw_logic_pro_z17g=065-CF1N&bfil=0"

    if productAvail == False:
        r = requests.get(url)

        if str(r.status_code)[0] == "4" or str(r.status_code)[0] == "5":
            print(f"Error: {r.status_code}")
        else:
            if r.json()["body"]["replace"]["purchaseInfo"]["isBuyable"]:
                bot.sendMessage(
                    dictionary["OWNER_CHAT_ID"], "Product is available to buy!")
                productAvail = True

    time.sleep(1)
