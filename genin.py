#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The hotspots dictionary was generated by running the following command in the
# source directory [1] ../adwaita-icon-theme/src/cursors/pngs/
#
# $ grep ^24 *.in | sed -r 's/^([^:].*)\.in:24 ([0-9]+) ([0-9]+).*/"\1": [\2, \3],/' | sort | uniq
#
# [1]: https://github.com/GNOME/adwaita-icon-theme/tree/mainline/src/cursors/pngs

import sys

HOTSPOTS = {
    "all-scroll": [13, 11],
    "bd_double_arrow": [11, 11],
    "bottom_left_corner": [10, 15],
    "bottom_right_corner": [15, 15],
    "bottom_side": [13, 18],
    "bottom_tee": [12, 19],
    "circle": [20, 4],
    "context-menu": [20, 4],
    "copy": [20, 4],
    "cross": [13, 11],
    "crossed_circle": [12, 12],
    "crosshair": [13, 11],
    "dnd-ask": [15, 9],
    "dnd-copy": [15, 9],
    "dnd-link": [15, 9],
    "dnd-move": [15, 9],
    "dnd-no-drop": [15, 9],
    "dnd-none": [12, 11],
    "dotbox": [13, 11],
    "fd_double_arrow": [11, 11],
    "grabbing": [12, 11],
    "hand1": [13, 7],
    "hand2": [16, 5],
    "left_ptr": [20, 4],
    "left_side": [6, 13],
    "left_tee": [6, 12],
    "link": [20, 4],
    "ll_angle": [4, 19],
    "lr_angle": [20, 19],
    "move": [12, 11],
    "pencil": [17, 21],
    "plus": [14, 11],
    "pointer-move": [20, 4],
    "question_arrow": [12, 21],
    "right_ptr": [3, 4],
    "right_side": [19, 13],
    "right_tee": [20, 12],
    "sb_down_arrow": [12, 19],
    "sb_h_double_arrow": [12, 12],
    "sb_left_arrow": [6, 12],
    "sb_right_arrow": [19, 12],
    "sb_up_arrow": [12, 3],
    "sb_v_double_arrow": [12, 13],
    "tcross": [12, 12],
    "top_left_corner": [10, 10],
    "top_right_corner": [15, 10],
    "top_side": [13, 6],
    "top_tee": [12, 5],
    "ul_angle": [4, 5],
    "ur_angle": [20, 5],
    "vertical-text": [12, 11],
    "X_cursor": [12, 12],
    "xterm": [13, 12],
    "zoom-in": [13, 10],
    "zoom-out": [13, 10],
}

HOTSPOTS_ANIMATED = {
    "watch": [13, 11, 16],
    "left_ptr_watch": [20, 3, 16],
}

if len(sys.argv) > 1:
    SIZES = [int(size) for size in sys.argv[1:]]
else:
    SIZES = range(24, 96 + 1, 6)

for name, hs in HOTSPOTS_ANIMATED.items():
    with open(name + ".in", "w") as fd:
        for size in SIZES:
            for i in range(1, 60 + 1):
                fd.write(
                    "{size} {xhot} {yhot} png/{size}x{size}/{name}_{i:04d}.png {ms}\n".format(
                        size=size,
                        xhot=round(hs[0] / 24 * size),
                        yhot=round(hs[1] / 24 * size),
                        name=name,
                        i=i,
                        ms=hs[2],
                    )
                )

for name, hs in HOTSPOTS.items():
    with open(name + ".in", "w") as fd:
        for size in SIZES:
            fd.write(
                "{size} {xhot} {yhot} png/{size}x{size}/{name}.png\n".format(
                    size=size,
                    xhot=round(hs[0] / 24 * size),
                    yhot=round(hs[1] / 24 * size),
                    name=name,
                )
            )
