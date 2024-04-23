import re


def split_row(base_row: str) -> list[str]:
    row_list = re.split(r'\s+(?=[^()]*(?:\(|$))', base_row)
    for i in range(len(row_list)):
        if row_list[i].startswith('(image'):
            image = {k[0]: k[1] for k in (p.split('=') for p in row_list[i][:-1].split()[1:])}
            row_list[i] = image
    return row_list


def get_fragments(y: int):
    fragments.clear()
    current_imgs = [(k[2], k[3]) for k in surrounded if k[0] <= y < k[1]]
    current_imgs.append((0, 0))
    current_imgs.append((w, w))
    current_imgs.sort()
    for i in range(1, len(current_imgs)):
        added = (current_imgs[i - 1][1], current_imgs[i][0])
        fragments.append(added)


def insert_word(x: int, y: int, f: int, h: int, word_length: int, space: int) -> tuple:
    if x != fragments[f][0] and x + word_length + space <= fragments[f][1]:
        x += word_length + space
    elif x == fragments[f][0] and x + word_length <= fragments[f][1]:
        x += word_length
    else:
        for i in range(f + 1, len(fragments)):
            fragment = fragments[i]
            if word_length <= fragment[1] - fragment[0]:
                x = fragment[0] + word_length
                f = i
                break
        else:
            y += h
            h = h_global
            get_fragments(y)
            exit_circle_flag = False
            while True:
                for j in range(len(fragments)):
                    fragment = fragments[j]
                    if word_length <= fragment[1] - fragment[0]:
                        x = fragment[0] + word_length
                        f = j
                        exit_circle_flag = True
                        break
                else:
                    y += h
                    get_fragments(y)
                if exit_circle_flag:
                    break
    return x, y, f, h


def insert_embedded(x: int, y: int, f: int, h: int, image: dict) -> tuple:
    width = int(image["width"])
    x, y, f, h = insert_word(x, y, f, h, width, c)
    print(x - width, y)
    h_row = max(h, int(image["height"]))
    return x, y, f, h_row


def insert_surrounded(x: int, y: int, f: int, h: int, image: dict) -> tuple:
    width = int(image["width"])
    height = int(image["height"])
    x, y, f, h = insert_word(x, y, f, h, width, 0)
    print(x - width, y)
    surrounded.append((y, y + height, x - width, x))
    get_fragments(y)
    for i in range(len(fragments)):
        if fragments[i][0] <= x <= fragments[i][1]:
            f = i
            break
    return x, y, f, h


def insert_floating(x: int, y: int, f: int, image: dict) -> tuple:
    width = int(image["width"])
    x_left = x + int(image["dx"])
    x_right = x_left + width
    y_top = y + int(image["dy"])
    if x_left < 0:
        x_left = 0
        x_right = x_left + width
    if x_right > w:
        x_right = w
        x_left = x_right - width
    print(x_left, y_top)
    return x_right, y_top


def paragraph_layout(par, y_start, h_current) -> int:
    surrounded.clear()
    y = y_start
    get_fragments(y)
    x = 0
    flag_f = False
    current_fragment = 0

    for word in par:
        if isinstance(word, dict):
            if word['layout'] == 'embedded':
                x, y, current_fragment, h_current = insert_embedded(x, y, current_fragment, h_current, word)
                flag_f = False
            elif word['layout'] == 'surrounded':
                x, y, current_fragment, h_current = insert_surrounded(x, y, current_fragment, h_current, word)
                flag_f = False
            else:
                if flag_f:
                    x_f, y_f = insert_floating(x_f, y_f, current_fragment, word)
                else:
                    x_f, y_f = insert_floating(x, y, current_fragment, word)
                    flag_f = True
        else:
            x, y, current_fragment, h_current = insert_word(x, y, current_fragment, h_current, len(word) * c, c)
            flag_f = False

    y_max_sur = y
    for image in surrounded:
        if image[1] > y_max_sur:
            y_max_sur = image[1]
    y_end = max(y + h_current, y_max_sur)
    return y_end


paragraphs = []
with open('input.txt', 'r') as file:
    w, h_global, c = map(int, file.readline().strip().split())
    row = file.readline()
    while row:
        row = row.strip()
        paragraph = []
        while row:
            paragraph.append(row)
            row = file.readline().strip()
        paragraph = split_row(' '.join(paragraph))
        paragraphs.append(paragraph)
        row = file.readline()
y_current = 0
fragments = [] # fragments for current row x_start, x_end
surrounded = []  # coordinates of surrounded images y_start, y_end, x_start, x_end
for paragraph in paragraphs:
    y_current = paragraph_layout(paragraph, y_current, h_global)

