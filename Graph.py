from Node import Node
from Edge import Edge

def main():
    joe = Node()
    joe.set('name', 'Joe')

    minecraft = Node('game')
    minecraft.set('name', 'Minecraft')

    likes = Edge('likes')
    likes.link(joe, minecraft)

    notch = Node('person', {'name': 'Notch'})
    created = Edge('created').link(notch, minecraft)

if __name__ == '__main__':
    main()