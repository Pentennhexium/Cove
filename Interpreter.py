from enum import Enum

memory = {}

classes = {
    "Num": [],
    "Char": []
}


# Get Commands as Text from the File
def getLines(text):
    lines = []
    while len(text) != 0:
        lines.append(text[:text.find(";")])
        text = text[text.find(";") + 2:]
    return lines


class CommandType(Enum):
    Create = 0
    Call = 1
    CreateCall = 2


class Command:
    def __init__(self, type, text):
        self.type = type
        self.text = text


# Turns Line Strings into Commands
def parse(file):
    text = open(file, "r").read()
    lines = getLines(text)

    commands = []
    for line in lines:
        if classes.__contains__(line[0: line.find(" ")]):
            if not line.__contains__('='):  # Create
                commands.append(Command(CommandType.Create, line))
            else:
                commands.append(Command(CommandType.CreateCall, line))
        elif line.__contains__('='):
            commands.append(Command(CommandType.Call, line))

    return commands


def main(file):
    print(parse(file))


if __name__ == "__main__":
    main("code.cove")
    # main(input("Cove p0.1: "))
