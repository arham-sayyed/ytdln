from pytube import YouTube
import random 
from time import time , ctime
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5638103834:AAFzfnDDRnC6JTAKPYw5ynEl7a8pods742k",
				use_context=True)

loaders = [ 'https://media.tenor.com/PlT4DtiUuvYAAAAM/i-get-the-job-done-cat.gif' , 'https://64.media.tumblr.com/f678ce38eb896bc1d4aaa911958af087/tumblr_n2eccv6Dev1rgpzseo1_1280.gif' , 'https://i.pinimg.com/originals/bf/34/61/bf34611d89cb4e9e62fc4997a1d329f2.gif' , 'https://miro.medium.com/max/720/1*3zTTejN8RKtodF2pkycGow.gif' , 'https://miro.medium.com/max/720/1*kWggO1y6n1sdfGpxZaAAGA.gif', 'https://images.squarespace-cdn.com/content/v1/54e2089fe4b0cc0f0867f658/1427813547778-UMUV7CWR2XT7D0HVQG5R/BikerBot.gif' , 'https://cdn.dribbble.com/users/1129235/screenshots/3017888/robo-1_1.gif' , 'https://i.pinimg.com/originals/b0/05/10/b0051024e16fb23cefe70c8499e76664.gif' , 'https://bugfender.com/wp-content/uploads/2018/10/automated.gif']


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello There, Just Send Me The link of YouTube Video you want to Download ")




def getlink(update: Update, context: CallbackContext):
    ytlink = str(update.message.text)
    try:
        dl_link = get_dl_link(ytlink)
        if dl_link == False:
            update.message.reply_text("invalid")
        else:
            loading = update.message.reply_animation(animation = str(random.choice(loaders)) , caption = str(f"sending.... {yt_title}"))
            # sending = update.message.reply_text(f"sending.... {yt_title}")
            update.message.reply_video(caption = yt_title , video = dl_link)
            context.bot.delete_message(message_id = loading.message_id , chat_id = update.message.chat_id)

        
    except Exception as error:
        update.message.reply_text("erroorrrr, try my another bot @VideoDownloadBot")
        update.message.reply_text(str(error))
        print(error)




def get_dl_link(link):
    try:
        global yt_title
        url = YouTube(link)
        video = url.streams.get_highest_resolution()
        yt_title = video.title
        return video.url
    except:
        return False




updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(Filters.text, getlink))


updater.start_polling()
print("polling started...")
