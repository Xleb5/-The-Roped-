import os
import sys
import pygame
import csv


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def update_csv_cell(address, new_value):
    row_num, col_num = address
    with open('data/profiles.csv',  encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        lines = []
        for current_line in reader:
            if reader.line_num == row_num + 1:
                current_line[col_num] = new_value
            lines.append(current_line)
    with open('data/profiles.csv', 'w', newline='') as csvfile:
        csvfile.truncate()
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in lines:
           writer.writerow(i)


def music(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(fade_ms=-1)


def profiles(login, password):
    with open('data/profiles.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for ind, row in enumerate(reader):
            if row[0] == login and row[1] == password:
                return ind, row
    a = ind + 1
    with open('data/profiles.csv',  encoding="utf8") as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))
    reader.append([login, password, '0', 'idle '])
    with open('data/profiles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"')
        for i in reader:
            writer.writerow(i)
        return a, [login, password, '0', 'idle ']