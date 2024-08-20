import os

os.system("cls && title Проверка... && color b")
active = False
print("Здраствуйте! Проверка...")
if os.path.exists('token.txt') == False:
  print("Помести свой дискорд токен в файл TOKEN.txt\nИ перезапусти програму")
  open('token.txt', 'w')
  while True:
    a = 0
    a + 1
    
active = False
import asyncio
import random
import discord
import time
import requests
from discord.ext import commands
client = commands.Bot(command_prefix = ".", self_bot = True)
client.remove_command("help")

theme = ["color b", "color d", "color s", "color c", "color e", "color 8", "color 3"]
oski = ["Вообще нахуя ты так с отцом разговариваешь", ', че замолк сын чудовища', ". Я бы тебя отпиздил, хуесос", ", че молчим", ", давай, метни стрелочку, лучница ебаная", " попизди на меня еще, хуесоска :)", " :heart:", " сразу рот прирыл", " с хуями во рту говорить не можешь? Псина", ", что молчишь, жертва двух озабоченых подростков и бутылки водки", ". И вообще ты жертва аборта", ". Давай, голос, пёс.", ". Че блядь, погавкал и все?", "мы тебя по кругу пускали, чорт", ", я тебя палкой хуярил", ", мать твоя видя мой огромный член течет, уебище", ". Твоя мать под моим столом кстати", ". Я тебя елдаком по голове уебашил", ". Ты - одноклеточное существо.", ". Кринжовый хуеплет", ". Запомни нахуй, я - твой хозяин, а ты секс-рабыня", " хули ты мне сосать перестал, я не разрешал нахуй", ", кстати я тебе команду голос не давал, хули пиздишь уеба", ". Я слышал твоя мать элитная шлюха, попроси ее заскочить ко мне, давно не ебались", ", я твоему бате шуруп в голову закрутил", ", я из волос твоей жирной мамаши самокрутку сделал", "дочка двух инвалидов ору", "пытками sаsеш мне", "закадрил тя хуjем ", "на доsуге епу тя ", "хуjем тя абделал", "ТЫ ПОНИМАЕШЬ ЧТО Я ПИЗДАК ВТЕОЙ МАТРЕИ НА СВОЙ УЙ КАК МАКАРОНИНУ НАМОТАЛ БЛЯДЬ И НАЧАЛ РАСКРУЧИВАТЬ ЕЁ ПОСЛЕ ЧЕГО ВЫКИНУЛ В КОСМОС ЧТОБ ЕЁ ТАМ ИНОПЛАНЕТЯНЫ ХУЯМИ РВАЛИ?)", "Говноед Насаси Уже МОй Хуй ", "Нашёл Твою Мать На Берегу Озере Она Пасасала Чет", "Ты Зачастую На Мой Хуй Садилса Чоли?", "Ποεβαλ Τια ΛαΨκα", "НаигралсЯ С Моим Хуем?", "После Того Как Я Вкрутил Все Саморезы Тебе В Башку Я Вкрутил Свой Хуй Твоей Матери В Горло", "Паебал Тя В Попачку", "ТЫ ПОНИМАЕШЬЧ ТО МОЙ ХУЙ В ПИЗДАКЕ ТВОЕЙ МТАЕРИ НЛО, И ВСЕ БЛОХИ КОТОРЫЕ ТАМ ЖИВУТ БЛЯДЬ, ПЫТАЮТСЯ ВЗЯТЬ ЕГО В ПЛЕННИКИ И ИЗУЧИТЬ, НО МОЯ ЗАЛУПА ИХ ВСЕХ ТРАВИТ))", "СЛЫШЬ, ИДИ ОТДАЙ МОЙ ХУЙ В АРЕНДУ СВОЕЙ МАМАШИ, ЧТОБ ОНА ЕГО СПОКОЙНО ПОЛИЗАЛА))", "Мне кристально похуй на твое мнение)))", "Сын бляди я твою маму на цепь ставил и кормил вас Ты мне должен пятки целовать чучело", "все вместе е6али твою мать ты чё наhуй написал сынуля шлюхи", "ору cbIHok wлюхи че пастb разинул? ща )(уй туда положу будеш отрабатывать waBka cJluтая", "ору cbIHok wлюхи ebaJL TBoi-0 MepTByi-0 Matb))", "твой папашка аутист что кончил в твою мамашу и родился такой еблан как ты", "Я опозорил твой род алкаша папашки который сосет за бутылку коньяка", "слышь ты араб арабсыкие истории потом расказывай", "да уж твоя матушка солнца боится потому что она думает это мои яйца", "нахуй ты высер ебаный моим хуем прикрываешься когда мусора тебя начинают трахать в жопу", "axaxaxa opy 4e pactb OTkPiL wa XuY tuda PoloJy otrobativatb Bydew", "все вместе е6али твою мать ты чё наhуй написал сынуля шлюхи", "бамбиш клаsна шолаvа", "ез ез sоsеш как архитектурныj", "хехе sаsала ты мне как многоsтупенчатыj", "ты понимаешь, что клитор твоей матери эта зона чрезвычайно опасная ??", "слышь, что может служить защитой от воздействия проникающей радиации в пизду твоей матери ? ??", "ебу тя ару нахуй", "на счет три ты будешь сосать ок?если согласен то напиши что то", "помнишь как ты пытался соси как твоя мамка?))))00 мне понравилось", "курю сигарету )а те дал хуй курить мой )", "стати, ты зря так стараешься, ведь ещё в Библии указано, что кусок говна не имеет право на личное мнение.", "Это тебе мать перед смертью шепнула", "И вновь прозвучал слив", "Ну, что, дружок, проебал вспышку?", "Я из пробирки, меня воспитывали боги, я с олимпа, ты с канавы!", "Для тебя слово (что), как собаке команда фас, только та бежит за жертвой, а ты повторяешь фразу!", "Ты своим мозгом можешь осознать, что апостериория это знания полученные опытным путем, а априории наоборот", "ʂơცƖąʑŋıƖ ɬɛცყ ƈƖɛŋơɱ ơƖųɧą☩🍂", "ɴᴀ ʀᴀʙᴏᴛᴇ ᴛᴠᴏʏ ᴍᴀᴍᴀᴡᴜ ʜᴜᴇᴍ ᴏᴠᴇᴢ⛈👾", "s ᴜᴛʀᴀ ᴛᴠᴏʏ ᴍᴀᴍᴀᴡᴜ ᴇʙᴜ⛈👾", "ᴛᴠᴏʏ ᴍᴀᴍᴀᴡᴜ ᴠ'ᴋɪɴᴜʟ ɪᴢ ᴏᴋɴᴀ ᴘᴏᴛᴏᴍ ᴏʙᴏssᴀʟ⛈👾", "ɴᴀ ʀᴇᴄᴋᴇ sᴏsᴇᴡ ᴄʟᴇɴ ᴛʀᴜʙᴏᴄɪsᴛᴀ⛈👾", "ᴡᴀʟᴀᴠᴀ ɴᴇ sᴍᴇɪ ᴘᴀᴅᴀᴛ' s ᴍᴏᴇɢᴏ ʜᴜʏ⛈👾", "ɴᴀ ᴢᴀɴʏᴛɪᴀʜ sᴏsᴇᴡ ᴄʟᴇɴ ᴛʀᴏʙᴏᴄɪsᴛᴀ⛈👾", "۷ƈɛཞą ɬཞąɧąƖ ɬɛცყ ƙąƙ ı ʂɛɠơɖŋყą☩🍂", "n𝖆 v𝖆kz𝖆l𝖊 x𝖞u s𝖆s𝖊sh", "x𝖊 d𝖗𝖞𝖔𝖈h𝖞 𝖙𝖞𝖆 k𝖆k  l𝖆k𝖔miu", "x𝖊 d𝖗𝖞𝖔𝖈h𝖞 𝖙𝖞𝖆 k𝖆k  l𝖆shp𝖊d z𝖆b𝖆uk𝖆lskiu", "𝖙v𝖔𝖞𝖆 m𝖆𝖙", "mn𝖊 h𝖞u vs𝖆s𝖆l𝖆 k𝖆k l𝖊𝖈h𝖊bn𝖔m𝖆m𝖞 𝖙v𝖔𝖞𝖔 p𝖔 kp𝖞g𝖞 p𝖞s𝖙il", "на маtepиke хуй øtsasываешь kak лøх изе лøл леxkø es ez blja ariruj"]
oski1 = ["срувалюшен нищий клиент",',в срувалюшене 5раток и 900ботнетов', "срувалюшен называют топ клиентом ток дауны которые в ратки", "срувалюшен самый нищий клиент в мире","ты в ратке срувалюшена","юзеры срувалюшены сливаются по фактам","срувалюшен сливается хаха", "срувалюшен слит", "обнов в срувалюшене не будет", ",ты за срувалюшен? ну нагинайся тогда", "срувалюшен позор", "в 10000обнове срувалюшена будет добовление изменения никовXD", "ак админа еволюшена снесли интересно почему наверно раточки кидал))", "ты за евалюшен? ну дебил", "срувалюшен слили создатели потомучто это говно", "еволюшен говно которое даже атернос не ложит", "в евалюшене 5 ботов кое какXD", "срувалюшен обижается потомучто снимает постановы", "ты думаеш срувалюшен что-то крашнет жду на арес майн ботов)))","срувалюшен не смог заддосить рилик а фейк сервер смог))"]
@client.event
async def on_ready():
    print("Loading...")  
    await asyncio.sleep(0.5)
    os.system("title B\ ")
    await asyncio.sleep(0.5)
    os.system("title Be\ ")
    await asyncio.sleep(0.5)
    os.system("title Beb\ ")
    await asyncio.sleep(0.5)
    os.system("title Bebr\ ")
    await asyncio.sleep(0.5)
    os.system("title Bebr\ ")
    await asyncio.sleep(0.5)
    os.system("title Bebra\ ")
    await asyncio.sleep(0.5)
    os.system("title Bebra \ ")
    await asyncio.sleep(0.5)
    os.system("title Bebra / ")
    await asyncio.sleep(0.5)
    os.system("title Bebra / TEST \ SelfBot")
    os.system("cls && color c")
    print("""
                              
                                Developed by Aprarm
                                created witch BebraNET 

░░░░░░░░░░░░░░░░░███████░░░███████░░███████░░░░████████░░░░░░████░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░██░░░░██░░██░░░░░░░██░░░░██░░░██░░░░░██░░░░██░░██░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░███████░░░██████░░░███████░░░░████████░░░░████████░░░░░░░░░░░
░░░░░░░░░░░░░░░░░██░░░░██░░██░░░░░░░██░░░░██░░░██░░░██░░░░░██░░░░██░░░░░░░░░░░
░░░░░░░░░░░░░░░░░███████░░░███████░░███████░░░░██░░░░░██░░░██░░░░██░░░░░░░░░░░

                               **  Version : TEST **
                                        """)


################ S  E  T  T  I  N  G S #######################
token = open('token.txt', 'r').readline()
################ B  U  L  L  I  N  G  ########################
active = True

@client.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send("**Bebra TEST **\n`.says - хелп меню для того чтобы писать разными шрифтами`\n`.spam(количество)(текст) - спамит сообщением`\n`.osk (задержка) - буллит человека `\n`.invspam(количество) - спам невидимыми сообщениями`\n`.lagspam(количество) - заставляет лагать дискорд`\n`.zalgospam(количество) - спамит зальго (на телефоне лаги)`\n`.stoposk - останавливает буллинг`\n`.evo - буллинг срувалюшена`\n`.stopevo - останавливает буллинг срувалюшена`")

@client.command()
async def osk(ctx):
    global stop_spam_flag
    stop_spam_flag = False
    active = True
    await ctx.message.delete()
    while active:
      if stop_spam_flag:
          break
      await ctx.send(random.choice(oski))
      time.sleep(5)

@client.command(name="stoposk")
async def stoposk(ctx):
    await ctx.message.delete()
    global stop_spam_flag
    stop_spam_flag = True
    await ctx.send("чел жоско слит по фактам")
    
@client.command()
async def evo(ctx):
    global stop_spam_flag
    stop_spam_flag = False
    active = True
    await ctx.message.delete()
    while active:
      if stop_spam_flag:
          break
      await ctx.send(random.choice(oski1))
      time.sleep(5)

@client.command(name="stopevo")
async def stopevo(ctx):
    await ctx.message.delete()
    global stop_spam_flag
    stop_spam_flag = True
    await ctx.send("срувалюшен жоско слит по фактам")
    
@client.command()
async def lagspam(ctx, number):
    for i in range(int(number)):
        await ctx.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: ")
        time.sleep(0.10)
        
@client.command()
async def zalgospam(ctx, number): 
    for i in range(int(number)):
        await ctx.send("⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟")
        time.sleep(0.10)

@client.command()
async def says(ctx):
    await ctx.message.delete()
    await ctx.send("**Разные шрифты **\n`.rsay(текст) - ᴨᴎсᴀᴛь вᴏᴛ ᴛᴀᴋᴎм вᴏᴛ шᴩᴎфᴛᴏм`\n`.fsay(текст) - вꂦт пример те𝙠⼕та`\n`.gsay(текст) - п͇𝖕̶͇име͇𝖕 ̶ш͇𝖕̶͇и͇𝖋͇𝖙𝖆`")
    
@client.command()
async def fsay(ctx, *, text):
    await ctx.message.delete()
    replacing = text.replace("о", "ꂦ").replace("г", "ᴦ").replace("у", "ꌩ").replace("ц", "ц̲").replace("к", "𝙠").replace("ш", "ⲱ").replace("л", "ᴫ").replace("х", "ⅹ").replace("с", "⼕").replace("у", "у").replace("ы", "͇ы")
    await ctx.send(replacing)

@client.command()
async def gsay(ctx, *, text):
    await ctx.message.delete()
    replacing = text.replace("о", "𝖔").replace("г", "̶г").replace("у", "𝖚").replace("ц", "̶ц").replace("к", "ꮶ").replace("ш", "̶ш").replace("л", "͟л").replace("х", "𝖝").replace("с", "𝖈").replace("у", "⦑y⦒").replace("ы", "͇ы").replace("р", "͇𝖕").replace("ф", "͇𝖋").replace("т", "͇𝖙").replace("и", "̶͇и").replace("а", "͇𝖆")
    await ctx.send(replacing)

@client.command()
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

@client.command()
async def rsay(ctx, *, text):
    await ctx.message.delete()
    replacing = text.replace("й", "й").replace("ц", "ц").replace("у", "у").replace("к", "ᴋ").replace("ё", "ё").replace("г", "ᴦ").replace("ш", "ш").replace("ч", "ч").replace("е", "ᴇ").replace("и", "ᴎ").replace("о", "ᴏ").replace("я", "ᴙ").replace("х", "ⅹ").replace("п", "ᴨ").replace("р", "ᴩ").replace("з", "ᴈ").replace("л", "ᴫ").replace("с", "с").replace("ю", "ꙕ").replace("а", "ᴀ")
    await ctx.send(replacing)

@client.command()
async def spam(ctx, kv, *, text):
    await ctx.message.delete()
    print("спамер активирован...")
    while int(kv) !=0:
        await ctx.send(text)
        kv = int(kv)-1

@client.command()
async def invspam(ctx, number):
    await ctx.message.delete()
    print("невидимый спам включен...")
    for i in range(int(number)):
        await ctx.send("||\n||")
        time.sleep(0.10)

@client.command()
async def ruletka(ctx):
    stepen = ["*Чик* Выстрела не было", "*Чик* Выстрела не было", "*Чик* Выстрела не было", "*Чик* Выстрела не было", "*ПАФ* Вы умерли от свинцовой пули револьвера", "*ПАФ* Вы умерли от свинцовой пули револьвера"]

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        print("LOG: Комманды не существует!")
        await ctx.message.delete()

client.run(token, bot = False)
