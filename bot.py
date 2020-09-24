from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    message = 'Olá, ' + update.message.from_user.first_name + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token = '1300724353:AAGRE-9-bMyX3RLAbCRn7-dPha2NZF1EoHs'
    updater = Updater(token=token, use_context=True) 
    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()




'''#Bibliotecas que nós instalamos.
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from selenium import webdriver

class wppbot:
#Setamos o caminho de nossa aplicação.
    dir_path = os.getcwd()
#Nosso contrutor terá a entrada do nome do nosso 
    bot.def __init__(self, nome_bot):
#Setamos nosso bot e a forma que ele irá treinar.
        self.bot = ChatBot(nome_bot)
        self.bot.set_trainer(ListTrainer)
#Setamos onde está nosso chromedriver.
        self.chrome = self.dir_path+'\chromedriver.exe'
#Configuramos um profile no chrome para não precisar logar no whats toda vez que iniciar o bot.
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir="+self.dir_path+"\profile\wpp")
#Iniciamos o driver.
        self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)

def inicia(self,nome_contato):
#Selenium irá entrar no whats e aguardar 15 segundos até o dom estiver pronto.
    self.driver.get('https://web.whatsapp.com/')
    self.driver.implicitly_wait(15)
#Selecionamos o elemento da caixa de pesquisa do whats pela classe.
    self.caixa_de_pesquisa = self.driver.find_element_by_class_name('jN-F5')

#Escreveremos o nome do contato na caixa de pesquisa e aguardaremos 2 segundos.
    self.caixa_de_pesquisa.send_keys(nome_contato)
    time.sleep(2)
#Vamos procurar o contato/grupo que está em um span e possui o título igual que buscamos e vamos clicar.   
    self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
    self.contato.click()
    time.sleep(2)'''