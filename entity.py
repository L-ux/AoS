from consts import *
from itertools import cycle


class Entity:

    def __init__(self, entity_type, sprites, x, y, target_x, target_y, direction, current_turn, moves, made_move):
        self.entity_type = entity_type
        self.sprites = sprites
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.bottom_x = x + TILE_SIZE
        self.bottom_y = y + TILE_SIZE
        self.direction = direction
        self.current_turn = current_turn
        self.moves = moves
        self.made_move = made_move

    def convert_entity_type(self, entity_type):
        entity_type_dictionary = {"player": 0, "enemy": 1, "environment": 2}
        sprite_set = entity_type_dictionary[entity_type]
        return sprite_set

    def incremental_movement(self, x, y, target_x, target_y, movement_check):
        if x > target_x:
            if movement_check:
                return True
            else:
                x -= SPEED
        elif x < target_x:
            if movement_check:
                return True
            else:
                x += SPEED

        if y > target_y:
            if movement_check:
                return True
            else:
                y -= SPEED
        elif y < target_y:
            if movement_check:
                return True
            else:
                y += SPEED

        if movement_check:
            return False
        return x, y

    def collision_detection(self, location, array):
        cyc = cycle(([0, -1], [1, 0], [0, 1], [-1, 0]))
        # creates a cycle for getting adjacent tile location in order

        collision_bools = [True, True, True, True]
        for i in range(4):
            mod = next(cyc)
            x_check = location[0] + mod[0]
            y_check = location[1] + mod[1]
            if array[y_check][x_check] == 1:
                collision_bools[i] = False
        return collision_bools

    def special_tile_check(self, location, array):

        if array[location[1]][location[0]] == 2:
            return "PIT"
        elif array[location[1]][location[0]] == 'U':
            return "TOP DOOR"
        elif array[location[1]][location[0]] == 'R':
            return "RIGHT DOOR"
        elif array[location[1]][location[0]] == 'D':
            return "BOTTOM DOOR"
        elif array[location[1]][location[0]] == 'L':
            return "LEFT DOOR"
        else: return "NONE"

    def turn_order(self, current_turn, moves, made_move):
        if current_turn:
            if moves > 0:
                if made_move:
                    self.moves -= 1
                    self.made_move = False
                    print("Moves: ", moves)
            if moves <= 0:
                self.current_turn = False

    def start_turn(self):
        self.current_turn = True
        self.moves = MOVES
