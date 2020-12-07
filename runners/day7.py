import tools.common
import scripts.bags
from scripts.bags import Bag


def execute_part(part):
    input_text = tools.common.get_input(7, 1)
    bags = {}
    for description in input_text:
        bag = Bag()
        bag.process_description(description)
        bags[bag.color] = bag
    if part == 1:
        selected_bag_colors = set()
        new_bag_colors = {'shiny gold'}
        while not new_bag_colors.issubset(selected_bag_colors):
            selected_bag_colors.update(new_bag_colors)
            new_bag_colors = scripts.bags.scan_bags_for_colors(bags, selected_bag_colors)
        return len(selected_bag_colors) - 1
    if part == 2:
        return scripts.bags.count_contained_bags(bags['shiny gold'], bags) - 1
