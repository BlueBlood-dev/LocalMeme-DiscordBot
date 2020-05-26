import discord, random, requests
from discord.ext import commands


TOKEN = 'your token'
randomPhrases = [
    'your vocabulary of phrases outta here
]

def getWheather():
    try:
        city_id = 498817 #you can check for your city id
        appid = 'your API id here'
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        return data
    except Exception as e:
        print("Exception (weather):", e)
        pass


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #if (message.author == client.user):
     #   return
    if (message.content.startswith('!hi')):
        myid = '<user id u want to mention>'
        await message.channel.send('%s базарит:ЗДАРОВА БАНДИТЫ' %myid)
    if (message.content.startswith('!hug')):
       myid = '<user id u want to mention>'
       await message.channel.send( '%sобнял вас' % myid)
    if (message.content.startswith('!image')):
        num = random.randint(1,34)#the amount might differ
        await message.channel.send(file=discord.File('nikita'+str(num)+'.jpg'))#all images must be named like in example  and have to be in the same directory where bot.py is
    if (message.content.startswith('!phrase')):
        await message.channel.send(random.choice(randomPhrases))
    if(message.content.startswith('!audio')):#all audios might be named like in example 1,2,3... and have to be in the same directory where bot.py is
        num = random.randint(1,27)#the amount might differ
        await message.channel.send(file=discord.File('audio'+ str(num) + '.mp3'))
    if(message.content.startswith('!wheather')):
        data = getWheather()
        await message.channel.send('в Санкт-Петербурге: '+str(data['weather'][0]['description']) + '\n' + 'температура на данный момент:' + str(data['main']['temp']) + 
        'градусов\n' + 'максимальная температура:' + str(data['main']['temp_max'])+ ' градусов\n' + 'минимальная температура:' + str(data['main']['temp_min'])+' градусов')

client.run(TOKEN)




