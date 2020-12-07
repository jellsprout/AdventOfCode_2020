import re


def scan_bags_for_colors(bag_dict, color_set):
    bags = set()
    for key, bag in bag_dict.items():
        if color_set & bag.contained_colors and len(bag.contained_colors):
            bags.add(key)
    return bags


def count_contained_bags(bag, bag_dict):
    if bag.contained_colors:
        contained_bags = 0
        for inner_bag in bag.contents:
            contained_bags += inner_bag.quantity * count_contained_bags(bag_dict[inner_bag.color], bag_dict)
        return contained_bags + 1
    else:
        return 1


class Bag:
    def __init__(self):
        self.description = ''
        self.bag_string = ''
        self.contents_string = ''
        self.color = ''
        self.contents = []
        self.contained_colors = set()

    def process_description(self, descriptor_string):
        self.description = descriptor_string
        self.bag_string, self.contents_string = self.description.split(' bags contain ')
        self.color = self.bag_string
        self.contents = self.process_contents()
        self.contained_colors = self.get_content_colors()

    def process_contents(self):
        bags = []
        for s in self.contents_string.split(', '):
            bag = self.ContentBag(s)
            bags.append(bag)
        return bags

    def get_content_colors(self):
        colors = set()
        for bag in self.contents:
            if bag.color:
                colors.add(bag.color)
        return colors

    class ContentBag:
        def __init__(self, contents_string):
            split_string = re.fullmatch(r'(\d+) (.*) (bags?)(\.?\s*)', contents_string)
            if split_string:
                self.quantity = int(split_string.group(1))
                self.color = split_string.group(2)
            else:
                self.quantity = 0
                self.color = None
