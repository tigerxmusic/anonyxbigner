from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, CallbackQueryHandler, MessageHandler
from random import choice
import logging

CHANNEL_USERNAME = '@THESAMURAIJOURNEe'  # Replace with your channel's username
CHANNEL_LINK = 'https://t.me/+WxzELa3XPZAwOTQ1'  # Replace with your channel's invite link

can_show = False
admins = ['ITS_JASS_TOP']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

user_chat_ids = set()

def Random_choice():
    option = ['𝐁𝐈𝐆📈','𝐒𝐌𝐀𝐋𝐋📉']
    return choice(option)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # chat_id = update.message.chat_id
    chat_id = update.effective_chat.id if update.effective_chat else update.callback_query.message.chat_id
    user_id = update.effective_user.id
    chat_member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
    
    image_path = 'static/banner.jpeg'

    with open(image_path, 'rb') as image_file:
        if chat_member.status in ['left', 'kicked']:
            keyboard = [InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)]
            joined_status_no = [InlineKeyboardButton("Channel joined 🔴", callback_data="inactive")]
            # [[inactive_button1], [inactive_button2]]
            reply_markup = InlineKeyboardMarkup([keyboard ,joined_status_no])
            # await update.message.reply_text('Please join the channel to use this bot.', reply_markup=reply_markup)
            await context.bot.send_photo(chat_id=chat_id, photo=image_file, caption='💡 𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭.',reply_markup=reply_markup)
        else:

            user_chat_ids.add(chat_id)

            joined_status_yes = [[InlineKeyboardButton("Channel joined 🟢", callback_data="inactive")]]

            reply_markup2 = InlineKeyboardMarkup(joined_status_yes)

            prediction_button = [[KeyboardButton(text="🎰Colour Prediction")]]
            prediction_markup = ReplyKeyboardMarkup(prediction_button,resize_keyboard=True,one_time_keyboard=True)
            # await update.message.reply_text('Hello! You are a member of the channel. You can use the bot commands.')
            await context.bot.send_photo(chat_id=chat_id, photo=image_file, caption='𝐇𝐞𝐥𝐥𝐨! 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐚 𝐦𝐞𝐦𝐛𝐞𝐫 𝐨𝐟 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥. 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬.',reply_markup=reply_markup2)
            
            await context.bot.send_message(chat_id=chat_id, text='''👋 Hey! Welcome to our Bot.

❤️‍🔥 Get 99.99% accurate colour prediction!

💡 This Prediction Bot will only work when you have Register with bellow links.

TirangaGames:
https://tirangacasino.in/#/register?invitationCode=3252569730


📑 If you follow with above links, there will be upto 99% chance of right prediction.''',reply_markup=prediction_markup)
            # await update.message.reply_text('play the games',reply_markup=prediction_markup)

    # with open(image_path, 'rb') as image_file:
    #     await context.bot.send_photo(chat_id=chat_id, photo=image_file)



async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    # Check if the "inactive" button was clicked
    if query.data == "inactive":
        # Optionally, send a notification to the user that this button is inactive
        # await query.answer(text="This button is inactive.", show_alert=True)
        # chat_id = update.message.chat_id
        await start(update, context)

async def choose(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id if update.effective_chat else update.callback_query.message.chat_id
    user_id = update.effective_user.id
    chat_member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
    if not (chat_member.status in ['left', 'kicked']):
        print("yea");
        tiranga = [KeyboardButton(text="⚀ Tiranga Games")]
        
        choose_markup = ReplyKeyboardMarkup([tiranga],resize_keyboard=True,one_time_keyboard=True)
        await context.bot.send_message(chat_id=chat_id, text="choose",reply_markup=choose_markup)
    else:
        pass

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id if update.effective_chat else update.callback_query.message.chat_id
    user_id = update.effective_user.id
    user_name = update.message.from_user.username
    chat_member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

    # if user_name in admins:
    #     print("it works")
    # else:
    #     print("chiken")
    #     print(user_name)

    if not (chat_member.status in ['left', 'kicked']) and context.args and (user_name in admins): #and (user_name in admins) and context.args:
        message = ' '.join(context.args)
        for chat_id in user_chat_ids:
            try:
                await context.bot.send_message(chat_id=chat_id, text=message)
            except Exception as e:
                logging.error(f"Error sending message to {chat_id}: {e}")
    else:

        await context.bot.send_message(chat_id=chat_id, text="error")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    global can_show
    # Custom logic based on the text of the button pressed
    if text == "🎰Colour Prediction":
        await update.message.reply_text("💻 Select game for prediction:",reply_markup=ReplyKeyboardRemove())
        await choose(update, context)

    elif text == "fuck you":
        await update.message.reply_text("no, fuck you")
    
    elif text == "⚀ Tiranga Games" or text == "⚡ Next Prediction ⚡":

        await update.message.reply_text("🎮 Enter Period last 3 digits.",reply_markup=ReplyKeyboardRemove())
        text = update.message.text
        can_show = True

    elif text.isdigit() and len(text)== 3 and can_show:
        result = Random_choice()
        next_prediction = [KeyboardButton(text="⚡ Next Prediction ⚡")]

        back_press = [KeyboardButton(text="🔙 back")]

        next_markup = ReplyKeyboardMarkup([next_prediction,back_press],resize_keyboard=True,one_time_keyboard=True)


        pred = f"✅Prediction Result:\n👨‍💻Period No: {text}\n⚡Result: {result} \n\n Powered by 😈 : ◤𝙏𝙄𝙍𝘼𝙉𝙂𝘼◢~JASS "

        can_show = False

        await update.message.reply_text(text=pred,reply_markup=next_markup)
    
    elif text == "🔙 back" and can_show:
        can_show = False;
        await update.message.reply_text("you will be given to choose",reply_markup=ReplyKeyboardRemove())
        

    elif text == "🔙 back" and not can_show:
        await choose(update, context)

    else:
        await update.message.reply_text("Unrecognized option")
    
    print(can_show)
    
application = ApplicationBuilder().token("7081960525:AAH23LZ7B429ZTVTQqHluB9HQAuwdrB4u58").build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("broadcast", broadcast))
application.add_handler(CallbackQueryHandler(button_callback))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,handle_message))

application.run_polling()
            
