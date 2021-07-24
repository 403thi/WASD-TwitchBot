# IMPORTS
from twitchio.ext import commands
import pydirectinput, sys, time
#pydirectinput da certo na maioria das vezes
#pyautogui falha em alguns jogos :c

# INIT
token = "oauth:TOKEN"
clientid = "CLIENT_ID"
bot = commands.Bot(
    irc_token=token,
    client_id=clientid,
    nick='meubot_teste', #seu nick
    prefix='!', #prefixo (exemplo: !teste)
    initial_channels=['ufirtz'], # canais para entrar
)
tecla_sendo_pressionada = None

# FUNÇÕES
def segurar_tecla(tecla:str):
    global tecla_sendo_pressionada
    if tecla_sendo_pressionada != None:
        pydirectinput.keyUp(tecla_sendo_pressionada)
    pydirectinput.keyDown(tecla)
    tecla_sendo_pressionada = tecla

def mover_mouse(x : int, y : int = 0):
    pydirectinput.move(x, y)

def apertar_tecla(tecla : str):
    pydirectinput.press(tecla)

def segurar_tecla_sem_parar(tecla : str):
    pydirectinput.keyDown(tecla)

def parar_de_segurar(tecla : str):
    pydirectinput.keyUp(tecla)

# COMANDOS

@bot.command(name='ping', aliases=['p']) #name= nome do comando, aliases: apelidos, a função sera chamada pelo nome e os apelidos. aliases não é obrigatorio nos parâmetros 
async def funcao_teste(ctx): # o nome da função pode ser qualquer um
    await ctx.send(f'Ping! {ctx.author.name}') #igual ao discord.py

@bot.command(name="w")
async def tecla_w(ctx):
    segurar_tecla("w")

@bot.command(name="a")
async def tecla_s(ctx):
    segurar_tecla("a")

@bot.command(name="s")
async def tecla_w(ctx):
    segurar_tecla("s")

@bot.command(name="d")
async def tecla_s(ctx):
    segurar_tecla("d")

@bot.command(name="virar")
async def virar_mouse(ctx):
    mover_mouse(x=300)

@bot.command(name="pula")
async def pular(ctx):
    apertar_tecla("space")

@bot.command(name="ctrl")
async def corre(ctx):
    segurar_tecla_sem_parar("ctrl")

@bot.command(name="shift")
async def shift(ctx):
    segurar_tecla_sem_parar("shift")

'''
# OPCIONAL: "!exit" no chat para parar de rodar o código
# Para ativar isso no código tire as 3 aspas simples em cima e em baixo
@bot.command(name="exit")
async def exit_(ctx):
    await ctx.send("Saindo...")
    pydirectinput.keyUp(tecla_sendo_pressionada)
    sys.exit()
'''

# RUN
if __name__ == "__main__": # esse "if" é para rodar o bot quando o código estiver pronto para ser executado
    print("Rodando...")
    bot.run() # roda o bot
