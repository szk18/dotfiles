# -*- coding: utf-8 -*-


import re
from xkeysnail.transform import *

define_modmap({
    Key.LEFT_META: Key.LEFT_CTRL,
    Key.LEFT_ALT: Key.LEFT_META,
    # Key.LEFT_CTRL: Key.INSERT,
    Key.RIGHT_META: Key.RIGHT_CTRL,
})


# Global keymap
define_keymap(None, {
    # Vim
    K("C-h"): K("Left"),
    K("C-j"): K("Down"),
    K("C-k"): K("Up"),
    K("C-l"): K("Right"),

    # Mac
    K("RC-Backspace"): [K("Shift-Home"), K("Backspace")],

})
