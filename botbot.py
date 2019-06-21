import discord

TOKEN = 'NTgxOTUwODA5Mzc4NTIxMTI4.XQAOuA.wPq1RhoqaQvqqf3gBUlApKNoDMI'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('Hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        elif message.content.startswith("BotBot"):
            await message.channel.send('What\'s up {0.author.mention}'.format(message))

client = MyClient()
client.run(TOKEN)