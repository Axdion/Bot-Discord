# By Axdion
# libraries
import discord
import string
from discord.ext import commands
from random import randint, uniform, random
import datetime

import urllib.parse, urllib.request, re

# Initial configuration

client = commands.Bot(command_prefix='>', descripcion="Este es un bot basado en Ahri.   By: Axdion")  # Prefijo


#
# Configure intents (1.5.0)

#

# Commands
@client.command()
async def ping(ctx):
    await ctx.send('pong')



@client.command()
async def iris(ctx):
    await ctx.send('Larga vida a Iris \:v/')


@client.command()
async def latencia(ctx):
    await ctx.send(f'Latencia: {round(client.latency * 1000)}ms')


@client.command()
async def phasmophobia(ctx, cadena: str):
    lista = cadena.split('-')
    elegido = randint(0, len(lista) - 1)
    await ctx.send('El que hablará con el fantasma será: ' + lista[elegido])

@client.command()
async def champ(ctx):
    lista = ['AATROX', 'AHRI', 'AKALI', 'AKSHAN', 'ALISTAR', 'AMUMU', 'ANIVIA', 'ANNIE', 'APHELIOS', 'ASHE', 'AURELION SOL', 'AZIR', 'BARDO', 'BLITZCRANK', 'BRAND', 'BRAUM', 'CAITLYN', 'CAMILLE', 'CASSIOPEIA', "CHO'GATH", 'CORKI', 'DARIUS', 'DIANA', 'DR. MUNDO', 'DRAVEN', 'EKKO', 'ELISE', 'EVELYNN', 'EZREAL', 'FIDDLESTICKS', 'FIORA', 'FIZZ', 'GALIO', 'GANGPLANK', 'GAREN', 'GNAR', 'GRAGAS', 'GRAVES', 'GWEN', 'HECARIM', 'HEIMERDINGER', 'ILLAOI', 'IRELIA', 'IVERN', 'JANNA', 'JARVAN IV', 'JAX', 'JAYCE', 'JHIN', 'JINX', "KAI'SA", 'KALISTA', 'KARMA', 'KARTHUS', 'KASSADIN', 'KATARINA', 'KAYLE', 'KAYN', 'KENNEN', "KHA'ZIX", 'KINDRED', 'KLED', "KOG'MAW", 'LEBLANC', 'LEE SIN', 'LEONA', 'LILLIA', 'LISSANDRA', 'LUCIAN', 'LULU', 'LUX', 'MAESTRO YI', 'MALPHITE', 'MALZAHAR', 'MAOKAI', 'MISS FORTUNE', 'MORDEKAISER', 'MORGANA', 'NAMI', 'NASUS', 'NAUTILUS', 
'NEEKO', 'NIDALEE', 'NOCTURNE', 'NUNU Y WILLUMP', 'OLAF', 'ORIANNA', 'ORNN', 'PANTHEON', 'POPPY', 'PYKE', 'QIYANA', 'QUINN', 'RAKAN', 'RAMMUS', "REK'SAI", 'RELL', 'RENEKTON', 'RENGAR', 'RIVEN', 'RUMBLE', 'RYZE', 'SAMIRA', 'SEJUANI', 'SENNA', 'SERAPHINE', 'SETT', 'SHACO', 'SHEN', 
'SHYVANA', 'SINGED', 'SION', 'SIVIR', 'SKARNER', 'SONA', 'SORAKA', 'SWAIN', 'SYLAS', 'SYNDRA', 'TAHM KENCH', 'TALIYAH', 'TALON', 'TARIC', 'TEEMO', 'THRESH', 'TRISTANA', 'TRUNDLE', 'TRYNDAMERE', 'TWISTED FATE', 'TWITCH', 'UDYR', 'URGOT', 'VARUS', 'VAYNE', 'VEIGAR', "VEL'KOZ", 'VI', 'VIEGO', 'VIKTOR', 'VLADIMIR', 'VOLIBEAR', 'WARWICK', 'WUKONG', 'XAYAH', 'XERATH', 'XIN ZHAO', 'YASUO', 'YONE', 'YORICK', 'YUUMI', 'ZAC', 
'ZED', 'ZIGGS', 'ZILEAN', 'ZOE', 'ZYRA']


    await ctx.send('Los personajes que puedes usar son: '+lista[randint(0, len(lista)-1)]+', '+lista[randint(0, len(lista)-1)]+' y '+lista[randint(0, len(lista)-1)])
    


@client.command()
async def info(ctx):
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        description="Servidor para League of Legends y videojuegos en general.",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.red()
    )
    embed.add_field(name="Server creado en: ", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Región del Server: ", value=f"{ctx.guild.region}")
    embed.set_thumbnail(url="https://i.pinimg.com/736x/46/50/af/4650afca1c1acfc8037e4b6c59dfe8d0.jpg")
    await ctx.send(embed=embed)


@client.command()
async def youtube(ctx, *, search):
    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    html_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )
    search_result = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_result[0])
    # I will put just the first result, you can loop the response to show more results


@client.command()
async def anime(ctx):
    lista_imagenes = [
        'https://media1.tenor.com/images/b654429c5896ebda949f7834ef2c77a0/tenor.gif?itemid=5409075',
        'https://media1.tenor.com/images/73afb40f4becbab10aee349b75a6b4ab/tenor.gif?itemid=12069252',
        'https://media1.tenor.com/images/bddf2872f32eea960e56bd76093dd3c9/tenor.gif?itemid=6035620',
        'https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?itemid=5184314',
        'https://media1.tenor.com/images/8a4496aaefcafe7cc4338e15b29d1129/tenor.gif?itemid=5628679',
        'https://media.tenor.com/images/b2555827ed9c551c7a414f3b62cd4e67/tenor.gif',
        'https://media1.tenor.com/images/e68e8a42cd4c646670db504d5a9f32f5/tenor.gif?itemid=8798310',
        'https://media1.tenor.com/images/bc086ae360e56e595021a8266cbadf98/tenor.gif?itemid=7714753',
        'https://media1.tenor.com/images/5c77728d33be7142b497946c8b274b42/tenor.gif?itemid=16524623',
        'https://media1.tenor.com/images/be4a63a9c7bc780a09244f863f3cb8e0/tenor.gif?itemid=4928092',
        'https://media1.tenor.com/images/f53fd37fae8ef980dea04ed4cf6e916c/tenor.gif?itemid=12409029',
        'https://media1.tenor.com/images/bc8913076b1b7267c0ed71da91b44546/tenor.gif?itemid=19172108',
        'https://media.tenor.com/images/5b46491ca301ee7c231ca9aba80f4c1a/tenor.gif',
        'https://media1.tenor.com/images/5d50ac5e7d7008e6f672481f49d39a9c/tenor.gif?itemid=5451841'
    ]

    await ctx.send(lista_imagenes[randint(0, len(lista_imagenes) - 1)])


@client.command()
async def genshin(ctx):
    lista_imagenes = [
        'https://i.redd.it/dpn0da8hhir51.png',
        'https://upload-os-bbs.mihoyo.com/upload/2020/07/24/1096276/89b4b3a073c923c352ffcb968b627ffb_4393450001248327237.png',
        'https://media.tenor.com/images/d24b8df225ae714955a25c5363c58a99/tenor.gif',
        'https://media1.tenor.com/images/3a5a93f305a1de6395c933539534bb70/tenor.gif?itemid=18640817',
        'https://media1.tenor.com/images/e8fc1cd862716e1ebd6a0abdd62e3760/tenor.gif?itemid=18797395',
        'https://media1.tenor.com/images/a75c55bfe2b651b0ca2f381f625a5d9a/tenor.gif?itemid=18714751',
        'https://upload-os-bbs.mihoyo.com/upload/2020/07/12/6602702/fe33324823b15bbdf51873065b453784_1111154943076719560.png?x-oss-process=image/resize,s_740/quality,q_80/auto-orient,0/interlace,1/format,png',
        'https://upload-os-bbs.mihoyo.com/upload/2020/04/18/1009234/8d6319be2d523b1d1da80f2dfaca2c8a_2174643146423605917.jpg?x-oss-process=image/resize,s_740/quality,q_80/auto-orient,0/interlace,1/format,jpg',
        'https://i.imgflip.com/4f6ea2.jpg',
        'https://upload-os-bbs.mihoyo.com/upload/2020/05/20/1096276/05d82ba904ee456c5a138c512c7ae479_1775424614624590453.png?x-oss-process=image/resize,s_740/quality,q_80/auto-orient,0/interlace,1/format,png',
        'https://i.imgur.com/uFUrYfB.png', 'https://i.imgur.com/kG3KmOc.png',
        'https://i.imgur.com/sHCykr7.png', 'https://i.imgur.com/pIugk2S.png',
        'https://i.imgur.com/U4G55Ja.png', 'https://i.imgur.com/2FmFwa0.png',
        'https://pbs.twimg.com/media/EmvPvsRXEAAG4RV.jpg:large', 'https://i.imgur.com/kaBVtUd.jpg',
        'https://i.imgur.com/HEzw9ig.jpg', 'https://i.imgur.com/brJrMEm.jpg'
    ]
    await ctx.send(lista_imagenes[randint(0, len(lista_imagenes) - 1)])


@client.command()
async def dog(ctx):
    await ctx.send('https://i.imgur.com/RU07gdg.jpg')


@client.command()
async def contra(ctx):
    cadena = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
    contra = ''
    try:
        for i in range(9):
            contra = contra + cadena[randint(0, len(cadena) - 1)]
        await ctx.send(contra)
    except Exception as e:
        await ctx.send(f'Esta ocurriendo el error {e}')

# Eventos
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch"))
    print('My bot is Ready')



# Execution
client.run('Acá viene le token del bot, por seguridad este nunca debe mostrarse')

