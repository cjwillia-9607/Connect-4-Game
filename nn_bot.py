import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
import random
from connect_four import ConnectFour

class NeuralNetworkBot:
    def __init__(self, piece, model=None):
        self.piece = piece
        self.model = model or self.build_model()

    def build_model(self):
        model = Sequential([
            Input(shape=(7 * 6,)),  # Specify input shape here
            Dense(128, activation='relu'),  # Increased number of neurons
            Dense(256, activation='relu'),  # Added an additional layer
            Dense(256, activation='relu'),  # Added an additional layer
            Dense(128, activation='relu'),  # Added an additional layer
            Dense(64, activation='relu'),
            Dense(64, activation='relu'),
            Dense(32, activation='relu'),
            Dense(7, activation='linear')
        ])
        model.compile(optimizer=Adam(), loss='mse')
        return model
    
    def convert_board(self, board):
        x_val = 1 if self.piece == 'X' else -1
        o_val = 1 if self.piece == 'O' else -1
        piece_to_number = {' ': 0, 'X': x_val, 'O': o_val}
        return np.array([piece_to_number[cell] for cell in board]).reshape(1, -1)

    def choose_column(self, game):
        state = self.convert_board(game.board)
        q_values = self.model.predict(state, verbose=0)
        available_columns = [c for c in range(game.width) if game.board[c] == ' ']
        q_values[0, [c for c in range(game.width) if c not in available_columns]] = -np.inf
        return np.argmax(q_values)
    
    def mutate(self, mutation_rate=0.01):
        weights = self.model.get_weights()
        new_weights = []
        for weight in weights:
            if np.ndim(weight) == 1:
                new_weights.append(weight + mutation_rate * np.random.randn(*weight.shape))
            else:
                new_weights.append(weight + mutation_rate * np.random.randn(*weight.shape))
        self.model.set_weights(new_weights)

    def crossover(self, other):
        new_model = self.build_model()
        new_weights = []
        weights1 = self.model.get_weights()
        weights2 = other.model.get_weights()
        for w1, w2 in zip(weights1, weights2):
            mask = np.random.rand(*w1.shape) > 0.5
            new_weights.append(np.where(mask, w1, w2))
        new_model.set_weights(new_weights)
        return NeuralNetworkBot(self.piece, new_model)