import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, 
                            CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

STATE1 = 1
STATE2 = 2

def inicio(update, context):
    try:
        first_name = update.message.from_user.first_name
        message = 'Olá, ' + username + '!'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as error:
        print(str(error))

def resposta(update, context):
    try:
        message =
        '''Que informação deseja ?\n
        1 - Cuidados com felinos\n
        2 - Alimentação\n
        3 - Castração\n
        4 - Vacinação\n'''
        # envia a mesagem para o usuario e guarda a resposta dele 
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE1
    except Exception as e:
        print(str(e))


def resposta1(update, context):
    resposta = update.message.text
    print(resposta)
    if (resposta=='1' or resposta=='cuidados' or resposta=='cuidar'):
        message =''' Ok.. vamos falar sobre cuidados com seus peludinhos\n'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    elif (resposta=='2' or resposta=='alimentacao' or resposta=='alimentação' or resposta=='alimento'
                or resposta=='ração' or resposta=='racao' or resposta=='comida' ):
        message = '''  Ok.. vamos falar sobre a alimentação dos seus peludinhos\n'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    elif (resposta=='3' or resposta=='castração' or resposta=='castracao' or resposta=='castrar'
                or resposta=='castrado'):
        message = '''  Ok.. vamos falar sobre castração\n'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END


def resposta2(update, context):
    resposta = update.message.text
    message = "Muito obrigada pela visita!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END


def cancel(update, context):
    return ConversationHandler.END


def main():
    try:
        # token = os.getenv('TELEGRAM_BOT_TOKEN', None)
        token = '1300724353:AAGRE-9-bMyX3RLAbCRn7-dPha2NZF1EoHs'
        updater = Updater(token=token, use_context=True)

        updater.dispatcher.add_handler(CommandHandler('start', inicio))

        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('feedback', resposta)],
            states={
                STATE1: [MessageHandler(Filters.text, resposta1)],
                STATE2: [MessageHandler(Filters.text, resposta2)]
            },
            # caso o usuário desista da conversa
            fallbacks=[CommandHandler('cancel', cancel)])
        updater.dispatcher.add_handler(conversation_handler)
        print("Updater no ar: " + str(updater))
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

