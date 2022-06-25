import discord
import BotCommands
import tictactoe

with open('BotToken.txt') as f:
    TOKEN = f.read()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$calculate'):
        result = BotCommands.calculate(msg)
        await message.channel.send('{:.2f}'.format(result))

    if msg.startswith('$play'):
        await message.channel.send('what do you want to play? $tictactoe , ')

    if msg.startswith('$tictactoe'):
        game = 'tictactoe'
        print(message)
        player = message.author.id
        await message.channel.send(f'player is <@' + str(player) + '>')
        tictactoe.start_game(player, message)

client.run(TOKEN)