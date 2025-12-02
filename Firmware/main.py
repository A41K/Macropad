import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.layers import Layers 

keyboard = KMKKeyboard()

# --- Modules ---
macros = Macros()
keyboard.modules.append(macros)

layers = Layers()
keyboard.modules.append(layers)

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

FN_KEY = KC.MO(1) 

keyboard.keymap = [
    [
        KC.A,                         # Pin D3: Simple letter 'A'
        KC.DELETE,                    # Pin D4: Delete
        KC.LCMD(KC.S),                # Pin D2: Save (Cmd+S) - Simplified syntax!
        FN_KEY,                       # Pin D1: Hold this to access Layer 1
    ],
    
    [
        KC.KB_VOLUME_UP,              # Pin D3: Vol Up
        KC.KB_VOLUME_DOWN,            # Pin D4: Vol Down
        KC.KB_MUTE,                   # Pin D2: Mute
        KC.TRNS,                      # Pin D1: Transparent (Does nothing, since it's held)
    ]
]

if __name__ == '__main__':
    keyboard.go()