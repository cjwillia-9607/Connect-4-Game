from nn_bot import NeuralNetworkBot
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.optimizers import Adam
from connect_four import ConnectFour
from random_bot import RandomBot
from logic_bot import LogicBot
from logic_bot import MinMaxBot

def manual_play(bot):
    c4 = ConnectFour()
    while c4.state == 'UNFINISHED':
        print(c4)
        if c4.current_piece == 'X':
            col = bot.choose_column(c4)
        else:
            col = int(input('Enter column: ')) - 1
        try:
            c4.insert(col, c4.current_piece)
        except ValueError:
            print('Column is full')
    print(c4)

def random_play(bot2):
    c4 = ConnectFour()
    bot1 = RandomBot('X')
    while c4.state == 'UNFINISHED':
        print(c4)
        if c4.current_piece == 'X':
            col = bot1.choose_column(c4)
        else:
            col = bot2.choose_column(c4)
        try:
            c4.insert(col, c4.current_piece)
        except ValueError:
            print('Column is full')

def human_play():
    c4 = ConnectFour()
    bot = LogicBot('O')
    while c4.state == 'UNFINISHED':
        print(c4)
        if c4.current_piece == 'X':
            col = int(input('Enter column: ')) - 1
        else:
            col = bot.choose_column(c4)
            print("chose: ", col)
        try:
            c4.insert(col, c4.current_piece)
        except ValueError:
            print('Column is full')
    print(c4)
    
def non_ai_play(bot):
    c4 = ConnectFour()
    # bot = LogicBot('O')
    while c4.state == 'UNFINISHED':
        print(c4)
        if c4.current_piece == 'X':
            col = int(input('Enter column: ')) - 1
        else:
            col = bot.choose_column(c4)
            print("chose: ", col)
        try:
            c4.insert(col, c4.current_piece)
        except ValueError:
            print('Column is full')
    print(c4)

def no_player(bot_1, bot_2):
    c4 = ConnectFour()
    while c4.state == 'UNFINISHED':
        print(c4)
        if c4.current_piece == 'X':
            col = bot_1.choose_column(c4)
        else:
            col = bot_2.choose_column(c4)
        try:
            c4.insert(col, c4.current_piece)
        except ValueError:
            print('Column is full')

        input("Press Enter to continue")
    print(c4.state)
    print(c4)
        


if __name__ == '__main__':
    c4 = ConnectFour()
    game_type = input('Enter game type (ai/minmax/human): ')
    if game_type == "ai" or game_type == "bots":
        model_path = input('Enter model path: ')
        bot = NeuralNetworkBot('X', tf.keras.models.load_model(model_path))
    
    
    if game_type == 'ai':
        manual_play(bot)
    elif game_type == 'minmax':
        non_ai_play(MinMaxBot('X', 4))
    elif game_type == 'human':
        human_play()
    elif game_type == 'bots':
        no_player(bot, MinMaxBot('O', 2))
    else:
        print('Invalid game type')