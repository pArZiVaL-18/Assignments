class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def has_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def is_complete_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word


def find_next_empty(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.':
                return r, c
    return None

def get_horizontal_word(grid, r, c, letter):
    col = c
    while col > 0 and grid[r][col - 1] != '#':
        col -= 1

    word = []
    while col < len(grid[0]) and grid[r][col] != '#':
        if col == c:
            word.append(letter)
        else:
            word.append(grid[r][col])
        col += 1

    return ''.join(word)

def get_vertical_word(grid, r, c, letter):
    row = r
    while row > 0 and grid[row - 1][c] != '#':
        row -= 1

    word = []
    while row < len(grid) and grid[row][c] != '#':
        if row == r:
            word.append(letter)
        else:
            word.append(grid[row][c])
        row += 1

    return ''.join(word)


def word_must_end_horizontally(grid, r, c):
    return c == len(grid[0]) - 1 or grid[r][c + 1] == '#'


def word_must_end_vertically(grid, r, c):
    return r == len(grid) - 1 or grid[r + 1][c] == '#'


def can_place(grid, trie, r, c, letter):
    # Horizontal check
    h_word = get_horizontal_word(grid, r, c, letter)
    if not trie.has_prefix(h_word):
        return False
    if word_must_end_horizontally(grid, r, c):
        if not trie.is_complete_word(h_word):
            return False

    # Vertical check
    v_word = get_vertical_word(grid, r, c, letter)
    if not trie.has_prefix(v_word):
        return False
    if word_must_end_vertically(grid, r, c):
        if not trie.is_complete_word(v_word):
            return False

    return True


def solve_crossword(grid, trie):
    cell = find_next_empty(grid)
    if not cell:
        return True  # solved

    r, c = cell

    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if can_place(grid, trie, r, c, ch):
            grid[r][c] = ch
            if solve_crossword(grid, trie):
                return True
            grid[r][c] = '.'  # backtrack

    return False


# grid = [
#     ['#', '#', '#', '#', '#'],
#     ['#', '.', '.', '.', '#'],
#     ['#', '#', '.', '#', '.'],
#     ['.', '.', '.', '#', '.'],
#     ['#', '#', '#', '#', '.']
# ]

# grid = [
#     ['#', '.', '.', '#'],
#     ['.', '.', '.', '.'],
#     ['#', '.', '.', '#']
# ]

grid = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

# words = ["CAT", "ARE", "TEA", "CAR"]

words = ["CAT", "ARE", "TEA"]

# words = ["ACT", "RAT", "CAT", "TOP"]

trie = Trie()
for w in words:
    trie.insert(w)

if solve_crossword(grid, trie):
    for row in grid:
        print(' '.join(row))
else:
    print("No solution")
