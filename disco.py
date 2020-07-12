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
import dropbox
import asyncio


tk = os.environ['DISCORD_BOT']


client = dropbox.Dropbox(os.environ['DROPBOX_TOKEN'])


server = '254326088002437122'


reacoes = ['\U0001F534', '\U0001F7E2', '\U0001F7E3', '\U0001F535', '\U0001F7E1']


sayuris = [sayuri for sayuri in client.files_list_folder('/simple_images/sayuri mattar').entries]

            
carnes = [carne for carne in client.files_list_folder('/simple_images/churrasco').entries]
    

mayumis = [mayumi for mayumi in client.files_list_folder('/simple_images/mayumi lol').entries]


mikasas = [mikasa for mikasa in client.files_list_folder('/simple_images/mikasa ackerman').entries]


megumins = [megumin for megumin in client.files_list_folder('/simple_images/megumin').entries]


harrys = [harry for harry in client.files_list_folder('/simple_images/harry styles').entries]


jotaros = [jotaro for jotaro in client.files_list_folder('/simple_images/jotaro').entries]


josephs = [joseph for joseph in client.files_list_folder('/simple_images/joseph joestar').entries]


giovannas = [giovanna for giovanna in client.files_list_folder('/simple_images/giorno giovanna').entries]


josukes = [josuke for josuke in client.files_list_folder('/simple_images/josuke').entries]


asunas = [asuna for asuna in client.files_list_folder('/simple_images/asuna').entries]


zero_twos = [zero for zero in client.files_list_folder('/simple_images/zero two').entries]


jonathans = [jonathan for jonathan in client.files_list_folder('/simple_images/jonathan joestar').entries]


hentais = [hentai for hentai in client.files_list_folder('/hentais').entries]


skylabs = [sky for sky in client.files_list_folder('/skylab').entries]


bot = commands.Bot(command_prefix='!')
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
        sayuris = [sayuri for sayuri in client.files_list_folder('/simple_images/sayuri mattar').entries]
        sayuri = choice(sayuris)
        sayuris.remove(sayuri)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        sayuri = choice(sayuris)
        sayuris.remove(sayuri)
    client.files_download_to_file(sayuri.name, sayuri.path_display)
    msg = await ctx.channel.send(f'Faltam {len(sayuris)} para o reset', file=discord.File(sayuri.name))
    msg
    os.remove(sayuri.name)


@bot.command(description='Mostra uma foto aleatoria de churrasco')
async def churrasco(ctx):
    global carnes
    if len(carnes) == 0:
        carnes = [carne for carne in client.files_list_folder('/simple_images/churrasco').entries]
        carne = choice(carnes)
        carnes.remove(carne)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        carne = choice(carnes)
        carnes.remove(carne)
    client.files_download_to_file(carne.name, carne.path_display)
    msg = await ctx.channel.send(f'Faltam {len(carnes)} para o reset', file=discord.File(carne.name))
    msg
    os.remove(carne.name)
    


@bot.command(description='Mostra uma foto aleatoria da Julia Mayumi')
async def mayumi(ctx):
    global mayumis
    if len(mayumis) == 0:
        mayumis = [mayumi for mayumi in client.files_list_folder('/simple_images/mayumi lol').entries]
        mayumi = choice(mayumis)
        mayumis.remove(mayumi)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        mayumi = choice(mayumis)
        mayumis.remove(mayumi)
    client.files_download_to_file(mayumi.name, mayumi.path_display)
    msg = await ctx.channel.send(f'Faltam {len(mayumis)} para o reset', file=discord.File(mayumi.name))
    msg
    os.remove(mayumi.name)




@bot.command(description='Mostra uma foto aleatoria da Mikasa Ackerman')
async def mikasa(ctx):
    global mikasas
    if len(mikasas) == 0:
        mikasas = [mikasa for mikasa in client.files_list_folder('/simple_images/mikasa ackerman').entries]
        mikasa = choice(mikasas)
        mikasas.remove(mikasa)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        mikasa = choice(mikasas)
        mikasas.remove(mikasa)
    client.files_download_to_file(mikasa.name, mikasa.path_display)
    msg = await ctx.channel.send(f'Faltam {len(mikasas)} para o reset', file=discord.File(mikasa.name))
    msg
    os.remove(mikasa.name)



@bot.command(description='Mostra uma foto aleatoria da Asuna')
async def asuna(ctx):
    global asunas
    if len(asunas) == 0:
        asunas = [asuna for asuna in client.files_list_folder('/simple_images/asuna').entries]
        asuna = choice(asunas)
        asunas.remove(asuna)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        asuna = choice(asunas)
        asunas.remove(asuna)
    client.files_download_to_file(asuna.name, asuna.path_display)
    msg = await ctx.channel.send(f'Faltam {len(asunas)} para o reset', file=discord.File(asuna.name))
    msg
    os.remove(asuna.name)



@bot.command(description='Mostra uma foto aleatoria da Megumin')
async def megumin(ctx):
    global megumins
    if len(megumins) == 0:
        megumins = [megumin for megumin in client.files_list_folder('/simple_images/megumin').entries]
        megumin = choice(megumins)
        megumins.remove(megumin)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        megumin = choice(megumins)
        megumins.remove(megumin)
    client.files_download_to_file(megumin.name, megumin.path_display)
    msg = await ctx.channel.send(f'Faltam {len(megumins)} para o reset', file=discord.File(megumin.name))
    msg
    os.remove(megumin.name)
    
    
@bot.command(description='Mostra uma foto aleatoria da Zero Two')
async def zero_two(ctx):
    global zero_twos
    if len(zero_twos) == 0:
        zero_twos = [zero for zero in client.files_list_folder('/simple_images/zero two').entries]
        zero = choice(zero_twos)
        zero_twos.remove(zero)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        zero = choice(zero_twos)
        zero_twos.remove(zero)
    client.files_download_to_file(zero.name, zero.path_display)
    msg = await ctx.channel.send(f'Faltam {len(zero_twos)} para o reset', file=discord.File(zero.name))
    msg
    os.remove(zero.name)



@bot.command(description='Mostra uma foto aleatoria do Harry Styles (pedido da lolo)')
async def harry(ctx):
    global harrys
    if len(harrys) == 0:
        harrys = [harry for harry in client.files_list_folder('/simple_images/harry styles').entries]
        harry = choice(harrys)
        harrys.remove(harry)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        harry = choice(harrys)
        harrys.remove(harry)
    client.files_download_to_file(harry.name, harry.path_display)
    msg = await ctx.channel.send(f'Faltam {len(harrys)} para o reset', file=discord.File(harry.name))
    msg
    os.remove(harry.name)


@bot.command(description='Mostra uma foto aleatoria do Kujo Jotaro')
async def jotaro(ctx):
    global jotaros
    if len(jotaros) == 0:
        jotaros = [jotaro for jotaro in client.files_list_folder('/simple_images/jotaro').entries]
        jotaro = choice(jotaros)
        jotaros.remove(jotaro)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        jotaro = choice(jotaros)
        jotaros.remove(jotaro)
    client.files_download_to_file(jotaro.name, jotaro.path_display)
    msg = await ctx.channel.send(f'Faltam {len(jotaros)} para o reset', file=discord.File(jotaro.name))
    msg
    os.remove(jotaro.name)



@bot.command(description='Mostra uma foto aleatoria do Jonathan Joestar')
async def jonathan(ctx):
    global jonathans
    if len(jonathans) == 0:
        jonathans = [jonathan for jonathan in client.files_list_folder('/simple_images/jonathan joestar').entries]
        jonathan = choice(jonathans)
        jonathans.remove(jonathan)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        jonathan = choice(jonathans)
        jonathans.remove(jonathan)
    client.files_download_to_file(jonathan.name, jonathan.path_display)
    msg = await ctx.channel.send(f'Faltam {len(jonathans)} para o reset', file=discord.File(jonathan.name))
    msg
    os.remove(jonathan.name)




@bot.command(description='Mostra uma foto aleatoria do Joseph Joestar')
async def joseph(ctx):
    global josephs
    if len(josephs) == 0:
        josephs = [joseph for joseph in client.files_list_folder('/simple_images/joseph joestar').entries]
        joseph = choice(josephs)
        josephs.remove(joseph)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        joseph = choice(josephs)
        josephs.remove(joseph)
    client.files_download_to_file(joseph.name, joseph.path_display)
    msg = await ctx.channel.send(f'Faltam {len(josephs)} para o reset', file=discord.File(joseph.name))
    msg
    os.remove(joseph.name)



@bot.command(description='Mostra uma foto aleatoria do Josuke Higashikata')
async def josuke(ctx):
    global josukes
    if len(josukes) == 0:
        josukes = [josuke for josuke in client.files_list_folder('/simple_images/josuke').entries]
        josuke = choice(josukes)
        josukes.remove(josuke)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        josuke = choice(josukes)
        josukes.remove(josuke)
    client.files_download_to_file(josuke.name, josuke.path_display)
    msg = await ctx.channel.send(f'Faltam {len(josukes)} para o reset', file=discord.File(josuke.name))
    msg
    os.remove(josuke.name)



@bot.command(description='Mostra uma foto aleatoria do Giorno Giovanna')
async def giorno(ctx):
    global giovannas
    if len(giovannas) == 0:
        giovannas = [giovanna for giovanna in client.files_list_folder('/simple_images/giorno giovanna').entries]
        giorno = choice(giovannas)
        giovannas.remove(giorno)
        await ctx.channel.send("As imagens foram resetadas")
    else:
        giorno = choice(giovannas)
        giovannas.remove(giorno)
    client.files_download_to_file(giorno.name, giorno.path_display)
    msg = await ctx.channel.send(f'Faltam {len(giovannas)} para o reset' , file=discord.File(giorno.name))
    msg
    os.remove(giorno.name)



@bot.command(description='Geme igual hentai')
async def ahegao(ctx):
    global hentais
    hentai = choice(hentais)
    pessoa = ctx.author
    canal = pessoa.voice.channel
    client.files_download_to_file(hentai.name, hentai.path_display)
    try:
        client1 = await canal.connect()
        client1
        client1.play(discord.FFmpegPCMAudio(hentai.name))
        print(os.getcwd())
        while client1.is_playing():
            sleep(1)
        await client1.disconnect()
    except:
        await ctx.channel.send(f'{pessoa.mention} seu merda, vc ta me quebrando')
    os.remove(hentai.name)
    



@bot.command(description='Skylab')
async def skylab(ctx):
    global skylabs
    mus = choice(skylabs)
    pessoa = ctx.author
    canal = pessoa.voice.channel
    client.files_download_to_file(mus.name, mus.path_display)
    try:
        client1 = await canal.connect()
        client1
        client1.play(discord.FFmpegPCMAudio(mus.name))
        print(os.getcwd())
        while client1.is_playing():
            sleep(1)
        await client1.disconnect()
    except:
        await ctx.channel.send(f'{pessoa.mention} seu merda, vc ta me quebrando')
    os.remove(mus.name)




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
    try:
        img = await r.getImages(arg)
        img = choice(img).file_url
        img = await r.download(img)
        await ctx.channel.send(file=discord.File(img))
        os.remove(img)
    except:
        await ctx.channel.send(f"Nao foi possivel encontrar {arg}")
	

@bot.event
async def on_ready():
    print("O bot principal 1 esta sendo executado")

r = r34.Rule34(None)
asyncio.run(bot.start(tk))
