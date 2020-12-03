tree_symbol = '#'


class TobogganRunner:
    def __init__(self, input_map, x_speed = 3, y_speed = 1):
        self.map = input_map
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.position = [0, 0]
        self.map_height = len(self.map) - 1
        self.map_width = len(self.map[0]) - 1
        self.trees_hit = 0

    def count_trees_on_path(self):
        while self.position[1] <= self.map_height:
            self.trees_hit += self.check_space_for_tree()
            self.make_step()
        return self.trees_hit

    def make_step(self):
        self.position[1] += self.y_speed
        self.position[0] += self.x_speed
        self.position[0] %= self.map_width

    def check_space_for_tree(self):
        return self.get_space_content() == tree_symbol

    def get_space_content(self):
        return self.map[self.position[1]][self.position[0]]
