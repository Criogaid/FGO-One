from cards.Cards import *
from cards.kind import *
from config import screenshot_path
from util.filter import *
from util.cvs import *
from PIL import Image


def init():

    a = Card()
    b = Card()
    c = Card()
    d = Card()
    e = Card()
    global cards
    cards = [a, b, c, d, e]


def init_cards():

    im = Image.open(screenshot_path)
    img_size = im.size
    gap = (img_size[0] - 1920) / 2

    card_types = [quick_card, arts_card, buster_card]
    mark_types = [resistance_mark, restraint_mark]
    # get the coordinates, mark and type of the card
    for i in range(5):
        for card_type in card_types:
            sh = f"./temp/{i}.png"
            tmpl = f"./assets/battle/{card_type}.png"
            if check(sh, tmpl, 0.9) == 1:
                pos = filter_crd(sh, tmpl, 0.9)
                x = pos[0][0] + gap + (i * 384)
                y = pos[0][1] + (img_size[1] / 2) - 100
                cards[i].crd = [x, y]
                cards[i].type = card_type
        for mark_type in mark_types:
            sh = f"./temp/{i}.png"
            tmpl = f"./assets/battle/{mark_type}.png"
            if check(sh, tmpl, 0.9) == 1:
                cards[i].mark = mark_type

    return cards


def positioning():
    init()
    result = init_cards()
    return result
