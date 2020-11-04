import requests, emoji
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

SAFE   = 0
ADOPT  = 1
GENDER = 2
INFO   = 3
TIP    = 4


'''------------------------------------------------------------------------------------------
                                           LIBRARIES
------------------------------------------------------------------------------------------'''
yes = {'sim', 'claro', 'certeza', 'vamos', 'quero', 'obvio', 'óbvio', 'tá', 'ta', 'ok', 'yep'}
no  = {'nao', 'não', 'apenas', 'já', 'saber', 'sobre', 'nope', 'no'}
op_1 = {'1', 'cuidados', 'cuidado', 'cuidar', 'cuida', 'cuido'}
op_2 = {'2', 'alimentacao', 'alimentação', 'alimento', 'ração', 'racao', 'comida', 'come'}
op_3 = {'3', 'castração', 'castracao', 'castrar', 'castrado', 'castro'}
op_4 = {'4', 'vacina', 'vacinas', 'vacinação', 'vacinacao', 'vacinar', 'vacino'}
male_gender = {'macho', 'machinho', 'homem', 'gato', 'menino', 'gatinho'}
female_gender = {'femea', 'fêmea', 'menina', 'gata', 'mulher', 'gatinha', 'femeazinha'}


'''------------------------------------------------------------------------------------------
                                           INTERACTIONS
------------------------------------------------------------------------------------------'''
# (HELLO)  FIRST MESSAGE TO THE USER
def hello(update, context):
    try:
        user_name = update.message.from_user.first_name
        message = '😺   Olá, ' + user_name + '!  😺\nVocê quer adotar um gatinho?  😻'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return SAFE
    except Exception as error:
        print(error)

# (SAFE)  ASKING ABOUT SAFETY
def safety(update, context):
    try:
        answer = set(str(update.message.text).lower().split(' '))
        if  answer.intersection(yes):
            message = 'Sua casa é segura ?'
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return ADOPT
        elif answer.intersection(no):
            message = 'Vamos falar sobre alguns cuidados, então?'
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return INFO
        else:
            message = "Não entendi. Poderia repetir, por favor?"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return ADOPT
    except Exception as error:
        print(error)


# (ADOPT)  CHOSING ABOUT ADOPTION OR INFORMATIONS
def adoption_question(update, context):
    try:
        answer = set(str(update.message.text).lower().split(' '))
        if  answer.intersection(yes):
            message = 'Quer um macho ou uma fêmea?'
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return GENDER
        elif answer.intersection(no):
            message = 'Você precisa de alguma informação sobre gatinhos?'
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return INFO
        else:
            message = "Não entendi. Poderia repetir, por favor?"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return ADOPT
    except Exception as error:
        print(error)
    

# CHOSING THE GENDER
def gender(update, context):
    try:
        answer = set(str(update.message.text).lower().split(' '))
        if answer.intersection(male_gender):
            message = 'Siga por aqui e escolha seu peludinho\nhttps://www.sogatinhos.com.br/gatinhos\nEspero você aqui na Cats para retirar seu novo bebê !!!'          
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return ConversationHandler.END
        elif answer.intersection(female_gender):
            message = 'Siga por aqui e escolha sua peludinha\nhttps://www.sogatinhos.com.br/gatinhos\nEspero você aqui na Cats para retirar sua nova bebezinha !!!'           
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return ConversationHandler.END
        else:
            message = "Não entendi. Poderia repetir, por favor?"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return GENDER
    except Exception as error:
        print(error)


# CHOSING THE INFORMATION
def info(update, context):
    try:
        user_name = update.message.from_user.first_name
        answer = set(str(update.message.text).lower().split(' '))
        if answer.intersection(yes):
            message = menu(user_name)        
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return TIP
        elif answer.intersection(no):
            message = 'Ok. Até mais !! Lambeijos !'           
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return ConversationHandler.END
        else:
            message = "Não entendi. Poderia repetir, por favor?"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return INFO
    except Exception as error:
        print(error)


#CARE TIPS
def tip(update, context):
    try:
        answer = set(str(update.message.text).lower().split(' '))
        if answer.intersection(op_1):
            message = care()       
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return INFO
        elif answer.intersection(op_2):
            message = feed()           
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return INFO
        elif answer.intersection(op_3):
            message = castration()           
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return INFO
        elif answer.intersection(op_4):
            message = vacination()           
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return INFO
        else:
            message = "Não entendi. Poderia repetir, por favor?"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return INFO
    except Exception as error:
        print(error)


def cancel(update, context):
    return ConversationHandler.END


'''------------------------------------------------------------------------------------------
                                          FUNCTIONS
------------------------------------------------------------------------------------------'''
# INFORMATION OPTIONS
def menu(user_name):
    #user_name = update.message.from_user.first_name
    message = 'Sobre o que você tem dúvidas, ' + user_name + '?\n1 - Cuidados gerais\n2 - Alimentação\n3 - Castração\n4 - Vacinação'
    return message

#----------------       OPTIONS      ------------------
def care():
    message ='''Vamos falar sobre cuidados com os peludinhos.
    Água - Sempre deixe água fresca e limpa disponível para seu bichano para evitar qualquer problema de saúde..
    Comida - Dê alimentos de boa qualidade ok.. não queremos essa fofura doente né..
    Cama - Gatos dormem de 12 e 16 horas por dia, é normal. Mas atente-se caso o peludinho ande muito pra baixo ok..
    Brincadeiras - Gatos AMAM brincadeiras. E não precisa gastar muito com brinquedos.. uma bolinha de papel já os deixam felizes rssss
    Higiene - Sim, gatos tomam banho. Isso ajuda a eliminar pêlos mortos que o fazem vomitar.
    Mantenha a caixa de areia sempre limpa para evitar doenças e use areia própria para gatos..
    Saúde - Leve seu bebê pelo menos 1 vez ao ano no veterinário para as vacinações e um check-up..
    Castração - Castre sempre!

    E aí, gostou?? Quer falar sobre outro tópico??'''
    return message

def feed():
    message = '''Vamos falar sobre alimentação dos peludinhos.
    Gatos são hipercarnívoros, ou seja, necessitam de muita proteína.. dê alimentos/rações com porções generosas de carne
    Ofereça rações não coloridas, pois estas contém muito sódio, o que prejudica a saúde do felino.
    Há no mercado diversas opções de rações, para todos os tipos de situação:
    - para gatos castrados;
    - para gatos obesos;
    - para as fases de idade dos felinos (filhote, adulto e senior);
    - entre outras.
    Adeque a ração de acordo com a situação de seu bebê.

    E aí, gostou?? Quer falar sobre outro tópico??'''
    return message

def castration():
    message = ''' Castração é um assunto polêmico. Mas o mais importante.. CASTRE SEMPRE !!
    Recomenda-se que seja feita entre 5 e 7 meses de idade, mas gatos mais velhos também podem ser castrados.
    A castração deixa seus peludinhos mais calmos e reduz, consideravelmente, a probabilidade de futuros tipos de câncer.
    Outra coisa, castre machos e fêmeas OK?
    Machos também tem cio, e costumam urinar bastante nesse período de forma a marcar território.
    Se quiser outros filhotinhos basta adotar outro, há muitos por aí precisando de amor
    
    E aí, gostou?? Quer falar sobre outro tópico??'''
    return message

def vacination():
    message = ''' Vacinação é algo muito importante e deve ser feita anualmente.
    Para gatos é usual a V4 ou a V5. É aplicada a partir do 60º dia de vida e inclui proteção contra:
    - rinotraqueíte;
    - calicevirose;
    - clamidiose;
    - panleucopenia;
    - e, no caso da V5, leucemia felina(FeLV)
    Além, é claro, de vacinar contra raiva e vermifugar. 
    
    E aí, gostou?? Quer falar sobre outro tópico??'''
    return message


'''------------------------------------------------------------------------------------------
                                          MAIN
------------------------------------------------------------------------------------------'''
def main():
    try:
        token = '1300724353:AAGRE-9-bMyX3RLAbCRn7-dPha2NZF1EoHs'
        updater = Updater(token=token, use_context=True)
        dispatcher = updater.dispatcher

        #updater.dispatcher.add_handler(CommandHandler('start', welcome))

        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('start', hello)],
            states={
                SAFE:   [MessageHandler(Filters.text, safety)],
                ADOPT:  [MessageHandler(Filters.text, adoption_question)],
                GENDER: [MessageHandler(Filters.text, gender)],
                INFO:   [MessageHandler(Filters.text, info)],
                TIP:    [MessageHandler(Filters.text, tip)]
            },
            fallbacks=[CommandHandler('cancel', cancel)])
        updater.dispatcher.add_handler(conversation_handler)

        print("Updater no ar: " + str(updater))
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
