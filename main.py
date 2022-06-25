import discord
from discord.ext import commands
from discord_components import DiscordComponents, Select, SelectOption, Button
from random import randint

with open('BotToken.txt') as f:
    TOKEN = f.read()

bot = commands.Bot(command_prefix='$')

player1 = ''
player2 = ''
next_player = ''

@bot.event
async def on_ready():
    '''
    Runs when the bot has logged onto the server
    '''
    DiscordComponents(bot)
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def hello(ctx):
    '''
    responds to the command $hello
    '''
    await ctx.send('Hello!')

@bot.command()
async def play(ctx, p2: discord.Member):
    '''
    responds to the command $play with a drop down menu of games
    '''

    global player2
    global player1
    player2 = p2
    player1 = ctx.author

    await ctx.send(
    'Player 1: ' + str(player1) + '\nPlayer 2: ' + str(player2) +
    '\nWhat game do you want to play?', # message body
    components = [
    Select(
        id='game selection',
        placeholder = 'Game',
        options = [ # drop down menu options
            SelectOption(label='Tic tac toe', value='value1'),
            SelectOption(label='Rock paper scisors', value='value2'),
            ])])

@bot.event
async def on_select_option(interaction):
    '''
    runs when a played uses the drop down menu
    '''
    if interaction.custom_id == 'game selection':
        await interaction.respond(type=6)
        channel = interaction.channel 
        if interaction.values[0] == 'value1': # tic tac toe selected
            global next_player
            next_player = player1 if randint(0,1) else player2 # randomly selects turn order

            global button1
            global button2
            global button3
            global button4
            global button5
            global button6
            global button7
            global button8
            global button9

            button1 = Button(label='_', custom_id='button1') # initializes all
            button2 = Button(label='_', custom_id='button2') # the buttons
            button3 = Button(label='_', custom_id='button3') # for the board
            button4 = Button(label='_', custom_id='button4')
            button5 = Button(label='_', custom_id='button5')
            button6 = Button(label='_', custom_id='button6')
            button7 = Button(label='_', custom_id='button7')
            button8 = Button(label='_', custom_id='button8')
            button9 = Button(label='_', custom_id='button9')

            # sends a 3x3 grid of buttons as the board
            await interaction.send('', components = [[button1, button2, button3]])
            await channel.send('', components = [[button4, button5, button6]])
            await channel.send('', components = [[button7, button8, button9]])
            await channel.send(f'It\'s {next_player.mention}\'s turn')

        elif interaction.values[0] == 'value2': # rock paper scissors selected
            global r_button
            global p_button
            global s_button

            r_button = Button(label='Rock', custom_id='r_button', emoji='🪨')
            p_button = Button(label='Paper', custom_id='p_button', emoji='📜')
            s_button = Button(label='Scissors', custom_id='s_button', emoji='✂️')

            await interaction.send('pick your move', components = 
            [[r_button, p_button, s_button]])

@bot.event
async def on_button_click(interaction):
    global player1
    global player2
    global next_player
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9

    if interaction.custom_id == 'button1':
        if interaction.author == next_player:
            await interaction.respond(type=6)
            if next_player == player1:
                next_player = player2
                button1 = Button(style=3, custom_id='button1', disabled=True, emoji='❌')
                await interaction.send('', components = [[button1, button2, button3]])
            elif next_player == player2:
                next_player = player1
                button1 = Button(style=1, custom_id='button1', disabled=True, emoji='⭕')
                await interaction.send('', components = [[button1, button2, button3]])

            await check_win(interaction)
    
    elif interaction.custom_id == 'button2':
        if interaction.author == next_player:
            await interaction.respond(type=6)
            if next_player == player1:
                next_player = player2
                button2 = Button(style=3, custom_id='button2', disabled=True, emoji='❌')
                await interaction.send('', components = [[button1, button2, button3]])
            elif next_player == player2:
                next_player = player1
                button2 = Button(style=1, custom_id='button2', disabled=True, emoji='⭕')
                await interaction.send('', components = [[button1, button2, button3]])

            await check_win(interaction)

    elif interaction.custom_id == 'button3':
        if interaction.author == next_player:
            await interaction.respond(type=6)
            if next_player == player1:
                next_player = player2
                button3 = Button(style=3, custom_id='button3', disabled=True, emoji='❌')
                await interaction.send('', components = [[button1, button2, button3]])
            elif next_player == player2:
                next_player = player1
                button3 = Button(style=1, custom_id='button3', disabled=True, emoji='⭕')
                await interaction.send('', components = [[button1, button2, button3]])
            
            await check_win(interaction)
    
    elif interaction.custom_id == 'button4':
        if interaction.author == next_player:
            await interaction.respond(type=6)
            if next_player == player1:
                next_player = player2
                button4 = Button(style=3, custom_id='button4', disabled=True, emoji='❌')
                await interaction.send('', components = [[button4, button5, button6]])
            elif next_player == player2:
                next_player = player1
                button4 = Button(style=1, custom_id='button4', disabled=True, emoji='⭕')
                await interaction.send('', components = [[button4, button5, button6]])

            await check_win(interaction)

    elif interaction.custom_id == 'button5':
        if interaction.author == next_player:
            await interaction.respond(type=6)
            if next_player == player1:
                next_player = player2
                button5 = Button(style=3, custom_id='button5', disabled=True, emoji='❌')
                await interaction.send('', components = [[button4, button5, button6]])
            elif next_player == player2:
                next_player = player1
                button5 = Button(style=1, custom_id='button5', disabled=True, emoji='⭕')
                await interaction.send('', components = [[button4, button5, button6]])

            await check_win(interaction)

    elif interaction.custom_id == 'button6':
        if interaction.author == next_player:
            await interaction.respond(type=6)
            if next_player == player1:
                next_player = player2
                button6 = Button(style=3, custom_id='button6', disabled=True, emoji='❌')
                await interaction.send('', components = [[button4, button5, button6]])
            elif next_player == player2:
                next_player = player1
                button6 = Button(style=1, custom_id='button6', disabled=True, emoji='⭕')
                await interaction.send('', components = [[button4, button5, button6]])

            await check_win(interaction)

    elif interaction.custom_id == 'button7':
        if interaction.author == next_player:
            await interaction.respond(type=6)
            if next_player == player1:
                next_player = player2
                button7 = Button(style=3, custom_id='button7', disabled=True, emoji='❌')
                await interaction.send('', components = [[button7, button8, button9]])
            elif next_player == player2:
                next_player = player1
                button7 = Button(style=1, custom_id='button7', disabled=True, emoji='⭕')
                await interaction.send('', components = [[button7, button8, button9]])

            await check_win(interaction)

    elif interaction.custom_id == 'button8':
        if interaction.author == next_player:
            await interaction.respond(type=6)
            if next_player == player1:
                next_player = player2
                button8 = Button(style=3, custom_id='button8', disabled=True, emoji='❌')
                await interaction.send('', components = [[button7, button8, button9]])
            elif next_player == player2:
                next_player = player1
                button8 = Button(style=1, custom_id='button8', disabled=True, emoji='⭕')
                await interaction.send('', components = [[button7, button8, button9]])

            await check_win(interaction)

    elif interaction.custom_id == 'button9':
        if interaction.author == next_player:
            await interaction.respond(type=6)
            if next_player == player1:
                next_player = player2
                button9 = Button(style=3, custom_id='button9', disabled=True, emoji='❌')
                await interaction.send('', components = [[button7, button8, button9]])
            elif next_player == player2:
                next_player = player1
                button9 = Button(style=1, custom_id='button9', disabled=True, emoji='⭕')
                await interaction.send('', components = [[button7, button8, button9]])

            await check_win(interaction)


async def check_win(interaction):
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global player1
    global player2
    global next_player

    if (button1.style == button2.style == button3.style == 3) or \
       (button4.style == button5.style == button6.style == 3) or \
       (button7.style == button8.style == button9.style == 3) or \
       (button1.style == button4.style == button7.style == 3) or \
       (button2.style == button5.style == button8.style == 3) or \
       (button3.style == button6.style == button9.style == 3) or \
       (button1.style == button5.style == button9.style == 3) or \
       (button7.style == button5.style == button3.style == 3):
        next_player = None
        await interaction.channel.send(f'{interaction.author.mention} is the winner!')

    elif (button1.style == button2.style == button3.style == 1) or \
         (button4.style == button5.style == button6.style == 1) or \
         (button7.style == button8.style == button9.style == 1) or \
         (button1.style == button4.style == button7.style == 1) or \
         (button2.style == button5.style == button8.style == 1) or \
         (button3.style == button6.style == button9.style == 1) or \
         (button1.style == button5.style == button9.style == 1) or \
         (button7.style == button5.style == button3.style == 1):
        next_player = None
        await interaction.channel.send(f'{interaction.author.mention} is the winner!')

    elif (button1.style != 2 and button2.style != 2 and button3.style != 2 and \
          button4.style != 2 and button5.style != 2 and button6.style != 2 and \
          button7.style != 2 and button8.style != 2 and button9.style != 2):
        next_player = None
        await interaction.channel.send('It\'s a draw :(')

    else:
        await interaction.channel.send(f'It\'s {next_player.mention}\'s turn')
    return

bot.run(TOKEN)