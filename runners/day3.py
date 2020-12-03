import tools.common
from scripts.toboggan_runner import TobogganRunner


def execute_part(part):
    input_text = tools.common.get_input(3, 1)
    if part == 1:
        runner = TobogganRunner(input_text)
        return runner.count_trees_on_path()
    if part == 2:
        input_slopes = [[1, 1],
                        [3, 1],
                        [5, 1],
                        [7, 1],
                        [1, 2]]
        product_of_slopes = 1
        for input_slope in input_slopes:
            runner = TobogganRunner(input_text, input_slope[0], input_slope[1])
            product_of_slopes *= runner.count_trees_on_path()
        return product_of_slopes
