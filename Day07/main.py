from anytree import Node, RenderTree

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return self.name + ": " + self.size


def save_input():
    with open("input", "r") as file:
        lines = [line.strip() for line in file]
        return lines


lines = save_input()
root = Node("/")


def print_tree(node):
    for pre, fill, node in RenderTree(node):
        print("%s%s" % (pre, node.name if type(node.name) == str else str(node.name)))



def process_commands():
    current_node = root
    for command in lines:
        commands_split = command.split(" ")
        if commands_split[1] == "cd":
            if commands_split[2] == "..":
                current_node = current_node.parent
            else:
                for i in current_node.children:
                    if i.name == commands_split[2]:
                        current_node = i

        elif commands_split[0] == "dir":
            Node(commands_split[1], current_node)

        elif commands_split[1] == "ls":
            ...
        elif type(int(commands_split[0])) == int:
            Node(File(commands_split[1], commands_split[0]), current_node)


process_commands()


# Part One
all_sums = 0

def give_sum_of_directory(node):
    sum = 0
    for element in node.children:
        if isinstance(element.name, File):
            sum += int(element.name.size)
        elif element.children != ():
            sum += give_sum_of_directory(element)
    if sum <= 100000 and not isinstance(node.name, File):
        global all_sums
        all_sums += sum
    return sum


#Ergebnis Part One
give_sum_of_directory(root)
print("Summe aller Directories: " + str(all_sums))

# Part Two
total_available_space = 70000000
needed_available_space = 30000000

root_space = give_sum_of_directory(root)
unused_space = total_available_space - root_space
needed_space = needed_available_space - unused_space
print("Platz der benötigt wird: " +  str(needed_space))

best_node = None
best_space = total_available_space

def print_nodes_of_valuable_size(node):
    sum = 0
    for element in node.children:
        if isinstance(element.name, File):
            sum += int(element.name.size)
        elif element.children != ():
            sum += print_nodes_of_valuable_size(element)
    if sum >= needed_space:
        global best_space
        global best_node
        if sum < best_space:
            best_space = sum
            best_node = node
    return sum


print_nodes_of_valuable_size(root)
print(best_node, best_space)
