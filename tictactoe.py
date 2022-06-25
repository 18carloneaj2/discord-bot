from turtle import TurtleScreen
from discord.ext import commands
from random import randint
from discord_components import DiscordComponents, Select, SelectOption, Button, ButtonStyle

player1 = ''
player2 = ''
bot = ''
board = []
turn = 1
nextplayer = ''

async def draw_board(ctx):
    global board
    await ctx.send(f'It\'s {nextplayer}\'s turn:\n' + 
                   board[0][0] + '      ' + board[0][1] + '      ' +
                   board[0][2] + '\n\n' + board[1][0] + '      ' +
                   board[1][1] + '      ' + board[1][2] + '\n\n' + 
                   board[2][0] + '      ' + board[2][1] + '      ' +
                   board[2][2], components = [])

async def start_game(p1, p2, ctx, client):
    '''
    '''
    global player1
    global player2
    global bot
    global board
    global turn
    global nextplayer

    turn = 1
    player1 = p1
    player2 = p2
    bot = client
    board = [[':white_large_square:', ':white_large_square:', ':white_large_square:'],
             [':white_large_square:', ':white_large_square:', ':white_large_square:'],
             [':white_large_square:', ':white_large_square:', ':white_large_square:']]
    
    await draw_board(ctx)

    if randint(0,1):
        nextplayer = player1
        await draw_board(ctx)
    else:
        nextplayer = player2
        await draw_board(ctx)

#def go_second(brd, player, message):

#def player_turn(brd, player, message):
    '''
    '''
