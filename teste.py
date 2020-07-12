import discord
import nest_asyncio
import googlesearch as gl
import requests as rq
from bs4 import BeautifulSoup as BS
from discord.ext import commands
from random import choice
from collections import Counter
from resq import Filme
nest_asyncio.apply()
import os
from time import sleep
import datetime
import rule34 as r34


tk = os.environ['DISCORD_BOT_TEST']


server = '254326088002437122'


reacoes = ['\U0001F534', '\U0001F7E2', '\U0001F7E3', '\U0001F535', '\U0001F7E1']


sayuris = [f".\\simple_images\\sayuri mattar\\{sayuri.name}" for sayuri in os.scandir('.\\simple_images\\sayuri mattar\\')]

            
carnes = [f".\\simple_images\\churrasco\\{carne.name}" for carne in os.scandir('.\\simple_images\\churrasco\\')]
    

mayumis = [f".\\simple_images\\mayumi lol\\{mayumi.name}" for mayumi in os.scandir('.\\simple_images\\mayumi lol\\')]


mikasas = [f".\\simple_images\\mikasa ackerman\\{mikasa.name}" for mikasa in os.scandir('.\\simple_images\\mikasa ackerman\\')]


megumins = [f".\\simple_images\\megumin\\{megumin.name}" for megumin in os.scandir('.\\simple_images\\megumin\\')]


harrys = [f".\\simple_images\\harry styles\\{harry.name}" for harry in os.scandir('.\\simple_images\\harry styles\\')]


jotaros = [f".\\simple_images\\jotaro\\{jotaro.name}" for jotaro in os.scandir('.\\simple_images\\jotaro\\')]


josephs = [f".\\simple_images\\joseph joestar\\{joseph.name}" for joseph in os.scandir('.\\simple_images\\joseph joestar\\')]


giovannas = [f".\\simple_images\\giorno giovanna\\{giovanna.name}" for giovanna in os.scandir('.\\simple_images\\giorno giovanna\\')]


josukes = [f".\\simple_images\\josuke\\{josuke.name}" for josuke in os.scandir('.\\simple_images\\josuke\\')]


asunas = [f".\\simple_images\\asuna\\{asuna.name}" for asuna in os.scandir('.\\simple_images\\asuna\\')]


zero_twos = [f".\\simple_images\\zero two\\{zero.name}" for zero in os.scandir('.\\simple_images\\zero two\\')]


jonathans = [f".\\simple_images\\jonathan joestar\\{jonathan.name}" for jonathan in os.scandir('.\\simple_images\\jonathan joestar\\')]

bot = commands.Bot(command_prefix='>')
bot.remove_command('help')
filmes = []
msg_vot = 0

@bot.command(description='Adiciona filme na lista de filmes')
async def filme_add(ctx, *args):
    arg = ' '.join(args)
    if len(filmes) < 5:
        filme = Filme(arg)
        filmes.append({filme.tit: filme.rotten()})
        await ctx.channel.send(f'Filme {filme.tit} foi adicionado a lista!')
    elif len(filmes) == 5:
        await ctx.channel.send('A lista esta cheia, digite !list_filmes para ver a lista ou !filmes_clear para limpar a lista de filmes')
        


@bot.command(description='Mostra a lista de filmes')
async def list_filmes(ctx):
    filme_t = ''
    if len(filmes) == 5:
        for filme in filmes:
            filme_t += f'{list(filme.keys())[0]} - {list(filme.values())[0]}\n'
        await ctx.channel.send(filme_t)
    else:
        for filme in filmes:
            filme_t += f'{list(filme.keys())[0]} - {list(filme.values())[0]}\n'
        await ctx.channel.send(filme_t)
        await ctx.channel.send(f'A lista não esta cheia, faltam {5 - len(filmes)}')
        


@bot.command(description='Limpa a lista de filmes')
async def filmes_clear(ctx):
    filmes.clear()
    await ctx.channel.send('A lista de filmes esta vazia agora')
    


@bot.command(description='Remove um determinado filme da lista de filmes')
async def filmes_remove(ctx, *args):
    arg = ' '.join(args)
    for filme in filmes:
        if arg.title() == list(filme.keys())[0]:
            filmes.remove(filme)
            await ctx.channel.send(f'O filme {arg.title()} foi removido da lista')
        


@bot.command(description='Remove o ultimo filme adicionado')       
async def filmes_remove_last(ctx):
    rem = filmes.pop()
    await ctx.channel.send(f'o filme {list(rem.keys())[0]} foi removido')



@bot.command(description='Da as classicaçoes e o link da pagina do filme no rotten tomatoes')
async def info_filme(ctx, *args):
    arg = ' '.join(args)
    filme = Filme(arg)
    await ctx.channel.send(f'{filme.tit} - {filme.rotten()} \n {filme.link}')



@bot.command(description='Mostra todos os comandos')
async def help(ctx):
    comandos = ''
    for comando in bot.commands:
        comandos += f'{bot.command_prefix}{comando} - {comando.description}\n'
    await ctx.channel.send(comandos)
    


@bot.command(description='Mostra todos os comandos')
async def ajuda(ctx):
    comandos = ''
    for comando in bot.commands:
        comandos += f'{bot.command_prefix}{comando} - {comando.description}\n'
    await ctx.channel.send(comandos)



@bot.command(description='Menciona alguem aleatorio do S P A C E G I R L S')
async def gostosa(ctx):
    gostosas = []
    gostosas_id = 696894726485442580
    #gostosas_id = 715109054321655868
    pessoas = [pessoa for pessoa in ctx.guild.members]
    #pessoas_roles = [[role.id for role in pessoa.roles] for pessoa in pessoas]
    for pessoa in pessoas:
        for role in pessoa.roles:
            if role.id == gostosas_id:
                gostosas.append(pessoa)
    a_gostosa = choice(gostosas)
    await ctx.channel.send(f'<@{a_gostosa.id}> é a mais gostosa do {ctx.guild.name}')



@bot.command(description='Menciona alguem aleatorio do S P A C E D O G S')
async def gostoso(ctx):
    gostosos = []
    gostosos_id = 550176858717552642
    #gostosas_id = 715109054321655868
    pessoas = [pessoa for pessoa in ctx.guild.members]
    #pessoas_roles = [[role.id for role in pessoa.roles] for pessoa in pessoas]
    for pessoa in pessoas:
        for role in pessoa.roles:
            if role.id == gostosos_id:
                gostosos.append(pessoa)
    o_gostoso = choice(gostosos)
    await ctx.channel.send(f'<@{o_gostoso.id}> é o mais gostoso do {ctx.guild.name}')



@bot.command(description='Chama alguem aleatorio de ruim')
async def ruim(ctx):
    pessoas = [pessoa for pessoa in ctx.guild.members]
    pessoa = choice(pessoas)
    await ctx.channel.send(f'<@{pessoa.id}> é mt ruim')



@bot.command(description='Chama o beto de gordo')
async def gordao(ctx):
    await ctx.channel.send('<@235490273843478529> é mt gordao \u26BD')



@bot.command(description='Chama alguem aleatorio de gordo')
async def gordo(ctx):
    pessoas = [pessoa for pessoa in ctx.guild.members]
    pessoa = choice(pessoas)
    await ctx.channel.send(f'<@{pessoa.id}> é gordo(a)')   



@bot.command(description='Chama o rqn de lindo')
async def lindo(ctx):
    await ctx.channel.send(f'<@407726106527924224> é lindissimo \u2665')



@bot.command(description='Da uma descrição do augusto')
async def gago(ctx):
    await ctx.channel.send("<@136580480278593536> é nosso gago de estimação, e comunista \u262D \u262D \u262D")



@bot.command(description='Chama o beto de talarico')
async def talarico(ctx):
    await ctx.channel.send("<@235490273843478529> É O MAIOR TALARICO DO SERVER \n TALARICO MORRE CEDO \u2620")



@bot.command(description='Rola um dados com os a quantidade de lados definida')
async def dado(ctx, args):
    lados = int(args)
    max = 100
    if lados <= max:
        dado1 = [i for i in range(1, lados + 1)]
        await ctx.channel.send(f'O dado de {lados} lados rodou, e caiu: {choice(dado1)}')
    else:
        await ctx.channel.send(f'PQ CARALHOS VC QR UM DADOS DE {lados} LADOS? VAI SE FODER')



@bot.command(description='Mostra uma foto aleatoria da Sayuri Mattar')
async def sayu(ctx):
    global sayuris
    if len(sayuris) == 0:
        sayuris = [f".\\simple_images\\sayuri mattar\\{sayuri.name}" for sayuri in os.scandir('.\\simple_images\\sayuri mattar\\')]
        sayuri = choice(sayuris)
        sayuris.remove(sayuri)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        sayuri = choice(sayuris)
        sayuris.remove(sayuri)
    msg = await ctx.channel.send(f'Faltam {len(sayuris)} para o reset', file=discord.File(sayuri))
    msg


@bot.command(description='Mostra uma foto aleatoria de churrasco')
async def churrasco(ctx):
    global carnes
    if len(carnes) == 0:
        carnes = [f".\\simple_images\\churrasco\\{carne.name}" for carne in os.scandir('.\\simple_images\\churrasco\\')]
        carne = choice(carnes)
        carnes.remove(carne)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        carne = choice(carnes)
        carnes.remove(carne)
    msg = await ctx.channel.send(f'Faltam {len(carnes)} para o reset', file=discord.File(carne))
    msg
    


@bot.command(description='Mostra uma foto aleatoria da Julia Mayumi')
async def mayumi(ctx):
    global mayumis
    if len(mayumis) == 0:
        mayumis = [f".\\simple_images\\mayumi lol\\{mayumi.name}" for mayumi in os.scandir('.\\simple_images\\mayumi lol\\')]
        a_mayumi = choice(mayumis)
        mayumis.remove(a_mayumi)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        a_mayumi = choice(mayumis)
        mayumis.remove(a_mayumi)
    msg = await ctx.channel.send(f'Faltam {len(mayumis)} para o reset', file=discord.File(a_mayumi))
    msg




@bot.command(description='Mostra uma foto aleatoria da Mikasa Ackerman')
async def mikasa(ctx):
    global mikasas
    if len(mikasas) == 0:
        mikasas = [f".\\simple_images\\mikasa ackerman\\{mikasa.name}" for mikasa in os.scandir('.\\simple_images\\mikasa ackerman\\')]
        a_mikasa = choice(mikasas)
        mikasas.remove(a_mikasa)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        a_mikasa = choice(mikasas)
        mikasas.remove(a_mikasa)
    msg = await ctx.channel.send(f'Faltam {len(mikasas)} para o reset', file=discord.File(a_mikasa))
    msg



@bot.command(description='Mostra uma foto aleatoria da Asuna')
async def asuna(ctx):
    global asunas
    if len(asunas) == 0:
        asunas = [f".\\simple_images\\asuna\\{asuna.name}" for asuna in os.scandir('.\\simple_images\\asuna\\')]
        a_asuna = choice(asunas)
        asunas.remove(a_asuna)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        a_asuna = choice(asunas)
        asunas.remove(a_asuna)
    msg = await ctx.channel.send(f'Faltam {len(asunas)} para o reset', file=discord.File(a_asuna))
    msg



@bot.command(description='Mostra uma foto aleatoria da Megumin')
async def megumin(ctx):
    global megumins
    if len(megumins) == 0:
        megumins = [f".\\simple_images\\megumin\\{megumin.name}" for megumin in os.scandir('.\\simple_images\\megumin\\')]
        a_megumin = choice(megumins)
        megumins.remove(a_megumin)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        a_megumin = choice(megumins)
        megumins.remove(a_megumin)
    msg = await ctx.channel.send(f'Faltam {len(megumins)} para o reset', file=discord.File(a_megumin))
    msg
    
    
@bot.command(description='Mostra uma foto aleatoria da Zero Two')
async def zero_two(ctx):
    global zero_twos
    if len(zero_twos) == 0:
        zero_twos = [f".\\simple_images\\zero two\\{zero.name}" for zero in os.scandir('.\\simple_images\\zero two\\')]
        a_zero = choice(zero_twos)
        zero_twos.remove(a_zero)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        a_zero = choice(zero_twos)
        zero_twos.remove(a_zero)
    msg = await ctx.channel.send(f'Faltam {len(zero_twos)} para o reset', file=discord.File(a_zero))
    msg



@bot.command(description='Mostra uma foto aleatoria do Harry Styles (pedido da lolo)')
async def harry(ctx):
    global harrys
    if len(harrys) == 0:
        harrys = [f".\\simple_images\\harry styles\\{harry.name}" for harry in os.scandir('.\\simple_images\\harry styles\\')]
        o_harry = choice(harrys)
        harrys.remove(o_harry)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        o_harry = choice(harrys)
        harrys.remove(o_harry)
    msg = await ctx.channel.send(f'Faltam {len(harrys)} para o reset', file=discord.File(o_harry))
    msg


@bot.command(description='Mostra uma foto aleatoria do Juko Jotaro')
async def jotaro(ctx):
    global jotaros
    if len(jotaros) == 0:
        jotaros = [f".\\simple_images\\jotaro\\{jotaro.name}" for jotaro in os.scandir('.\\simple_images\\jotaro\\')]
        o_jotaro = choice(jotaros)
        jotaros.remove(o_jotaro)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        o_jotaro = choice(jotaros)
        jotaros.remove(o_jotaro)
    msg = await ctx.channel.send(f'Faltam {len(jotaros)} para o reset', file=discord.File(o_jotaro))
    msg



@bot.command(description='Mostra uma foto aleatoria do Jonathan Joestar')
async def jonathan(ctx):
    global jonathans
    if len(jonathans) == 0:
        jonathans = [f".\\simple_images\\jonathan joestar\\{jonathan.name}" for jonathan in os.scandir('.\\simple_images\\jonathan joestar\\')]
        o_jonathan = choice(jonathans)
        jonathans.remove(o_jonathan)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        o_jonathan = choice(jonathans)
        jonathans.remove(o_jonathan)
    msg = await ctx.channel.send(f'Faltam {len(jonathans)} para o reset', file=discord.File(o_jonathan))
    msg




@bot.command(description='Mostra uma foto aleatoria do Joseph Joestar')
async def joseph(ctx):
    global josephs
    if len(josephs) == 0:
        josephs = [f".\\simple_images\\joseph joestar\\{joseph.name}" for joseph in os.scandir('.\\simple_images\\joseph joestar\\')]
        o_joseph = choice(josephs)
        josephs.remove(o_joseph)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        o_joseph = choice(josephs)
        josephs.remove(o_joseph)
    msg = await ctx.channel.send(f'Faltam {len(josephs)} para o reset', file=discord.File(o_joseph))
    msg



@bot.command(description='Mostra uma foto aleatoria do Josuke Higashikata')
async def josuke(ctx):
    global josukes
    if len(josukes) == 0:
        josukes = [f".\\simple_images\\josuke\\{josuke.name}" for josuke in os.scandir('.\\simple_images\\josuke\\')]
        o_josuke = choice(josukes)
        josukes.remove(o_josuke)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        o_josuke = choice(josukes)
        josukes.remove(o_josuke)
    msg = await ctx.channel.send(f'Faltam {len(josukes)} para o reset', file=discord.File(o_josuke))
    msg



@bot.command(description='Mostra uma foto aleatoria do Giorno Giovanna')
async def giorno(ctx):
    global giovannas
    if len(giovannas) == 0:
        giovannas = [f".\\simple_images\\giorno giovanna\\{giovanna.name}" for giovanna in os.scandir('.\\simple_images\\giorno giovanna\\')]
        o_giorno = choice(giovannas)
        giovannas.remove(o_giorno)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        o_giorno = choice(giovannas)
        giovannas.remove(o_giorno)
    msg = await ctx.channel.send(f'Faltam {len(giovannas)} para o reset' , file=discord.File(o_giorno))
    msg



@bot.command(description='Geme igual hentai')
async def ahegao(ctx):
    hentais = list(os.scandir('.\\hentais'))
    hentai = choice(hentais)
    pessoa = ctx.author
    canal = pessoa.voice.channel
    try:
        client = await canal.connect()
        client
        client.play(discord.FFmpegPCMAudio(f'hentais\\{hentai.name}'))
        print(os.getcwd())
        while client.is_playing():
            sleep(1)
        await client.disconnect()
    except:
        await ctx.channel.send(f'{pessoa.mention} seu merda, vc ta me quebrando')
    



@bot.command(description='Skylab')
async def skylab(ctx):
    musicas = list(os.scandir('.\\skylab'))
    mus = choice(musicas)
    pessoa = ctx.author
    canal = pessoa.voice.channel
    try:
        client = await canal.connect()
        client
        client.play(discord.FFmpegPCMAudio(f'skylab\\{mus.name}'))
        print(os.getcwd())
        while client.is_playing():
            sleep(1)
        await client.disconnect()
    except:
        await ctx.channel.send(f'{pessoa.mention} seu merda, vc ta me quebrando')




@bot.command(description='Inicia uma votação para a lista de filmes')
async def votacao(ctx):
    global reacoes
    filmes_v = f'{reacoes[0]} => {list(filmes[0].keys())[0]} - {list(filmes[0].values())[0]}\n'\
             f'{reacoes[1]} => {list(filmes[1].keys())[0]} - {list(filmes[1].values())[0]}\n'\
             f'{reacoes[2]} => {list(filmes[2].keys())[0]} - {list(filmes[2].values())[0]}\n'\
             f'{reacoes[3]} => {list(filmes[3].keys())[0]} - {list(filmes[3].values())[0]}\n'\
             f'{reacoes[4]} => {list(filmes[4].keys())[0]} - {list(filmes[4].values())[0]}\n'
    if len(filmes) == 5:
        msg = await ctx.channel.send(filmes_v)
        global msg_vot
        msg_vot = msg
        msg
        for emoji in reacoes:
            await msg.add_reaction(emoji)
    else:
        for filme in filmes:
            await ctx.channel.send(f'{list(filme.keys())[0]} - {list(filme.values())[0]}')
        await ctx.channel.send(f'A lista não esta cheia, faltam {5 - len(filmes)}')



@bot.command(description='Flooda uma determinada msg N vezes')
async def floodar(ctx, *args):
    max = 30
    pessoa = ctx.author
    arg = list(args)
    msgid = ctx.message.id
    msg = ' '.join(arg[:len(arg) - 1])
    quant = args[-1]
    quant = abs(int(quant))
    print(msg, quant, pessoa.name)
    try:
        with open('log_spam.txt', 'a') as log:
            log.write(f'Mensagem: {msg}\nMensagem ID:{msgid}\nQuantidade: {quant}\nPessoa: {pessoa.name}\nID Pessoa: {pessoa.id}\nNome Server: {ctx.guild.name}\nID Server: {ctx.guild.id}\nData: {datetime.datetime.now().strftime("%H:%M:%S - %d/%m/%Y")}\n------------------------------\n')
    except:
        with open('log_spam.txt', 'a') as log:
            log.write(f'Mensagem ID: {msgid}\nQuantidade: {quant}\nID Pessoa: {pessoa.id}\nNome Server: {ctx.guild.name}\nID Server: {ctx.guild.id}\nData: {datetime.datetime.now().strftime("%H:%M:%S - %d/%m/%Y")}\n------------------------------\n')

    if quant <= max:
        for i in range(quant):
            await ctx.channel.send(f'{msg} - {i + 1} de {int(quant)}')
    else:
       await ctx.channel.send(f'Ow namoralzinha ai {pessoa.mention}, vai se foder, floodar {quant} msgs é coisa de psicopata, flooda {max} ai namoral') 


@bot.command(description='Encerra a votaçao da lista de filmes')
async def encerrar_votacao(ctx):
    global msg_vot
    msg_vot = await ctx.channel.fetch_message(msg_vot.id)
    #msg_vot = await ctx.channel.fetch_message(715853586340380743)
    print(msg_vot.content)
    #print(msg_vot.reactions.emoji)
    reacoes_count = {str(reacao.emoji): reacao.count for reacao in msg_vot.reactions}
    #await ctx.channel.send(reacoes_count)
    contador = Counter(reacoes_count).most_common()
    vencedor = contador[0][0]
    votos_vencedor = contador[0][1]
    filme_ve = reacoes.index(vencedor)
    #await ctx.channel.send(filme_ve)
    #await ctx.channel.send(type(filmes))
    #await ctx.channel.send(filmes)
    await ctx.channel.send(f'O vencedor foi: {list(filmes[filme_ve].keys())[0]} com {votos_vencedor - 1} voto(s)')

@bot.command(description='Busca uma imagem de rule34.xxx')
async def rule34(ctx, *args):
    global r
    arg = ' '.join(args)
    img = await r.getImages(arg)
    img = choice(img).file_url
    img = await r.download(img)
    await ctx.channel.send(file=discord.File(img))
    os.remove(img)
    await ctx.channel.send(f"Nao foi possivel encontrar {arg}")
	

@bot.event
async def on_ready():
    print("O bot teste esta sendo executado")
r = r34.Rule34(None)
bot.run(tk)
