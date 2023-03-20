## a list of keycodes attained by letting the listener run and manually pressing all keys on my keyboard
## (since I could not figure out how to extract alphanumeric keycodes from pynput's classes, so..)
## it appears that you can only get the vk (virtual keycodes) from a key but the reverse is not true: you cannot obtain all alphanumeric letters from knowing it's keycode, therefore we have to use on_press() to print all the
#it appears that you need to use on_press() to get a key object. From this key object, you can obtain the key's string and vk (virtual key). However, when holding modification keys, such as shift or ctrl, and calling on_press on another key, the key's string will be modified, therefore strings printed become irregular. I.e., receiving the string from a vk is indeterministic because a vk can have multiple strings assigned to it. Therefore we need to use this list and search up the value with the vk as dictionary key.


#key combos received by event listener
res = [[27, 'esc'], [112, 'f1'], [113, 'f2'], [114, 'f3'], [115, 'f4'], [116, 'f5'], ['f6', 117], [118, 'f7'], ['f8', 119], [120, 'f9'], [121, 'f10'], ['f11', 122], [123, 'f12'], ['media_volume_up', 175], ['alt_l', 164], [44, 'print_screen'], [27, 'esc'], ['^', 220], [49, '1'], [50, '2'], [51, '3'], [52, '4'], [53, '5'], ['6', 54], ['7', 55], [56, '8'], [57, '9'], [48, '0'], ['ß', 219], ['´', 221], [8, 'backspace'], [45, 'insert'], ['home', 36], [33, 'page_up'], ['delete', 46], [35, 'end'], ['page_down', 34], [144, 'num_lock'], [111, '-'], [106, '*'], [109, '-'], [9, 'tab'], [81, 'q'], ['w', 87], ['e', 69], [82, 'r'], ['t', 84], [90, 'z'], [85, 'u'], ['i', 73], ['o', 79], [80, 'p'], ['ü', 186], [187, '+'], ['enter', 13], ['delete', 46], [35, 'end'], ['page_down', 34], ['NumPad7', 103], [104, 'NumPad8'], [105, 'NumPad9'], [107, '+'], ['caps_lock', 20], ['a', 65], ['s', 83], ['d', 68], ['f', 70], ['g', 71], [72, 'h'], [74, 'j'], [75, 'k'], [76, 'l'], [192, 'ö'], ['ä', 222], ['#', 191], [100, 'NumPad4'], ['NumPad5', 101], ['NumPad6', 102], [107, '+'], [160, 'shift'], [226, '<'], [89, 'y'], [88, 'x'], ['c', 67], ['v', 86], [66, 'b'], ['n', 78], [77, 'm'], [188, ','], ['.', 190], [189, '-'], [161, 'shift_r'], ['up', 38], ['NumPad1', 97], [98, 'NumPad2'], [99, 'NumPad3'], ['enter', 13], [162, 'ctrl_l'], [91, 'cmd'], ['alt_l', 164], [32, 'space'], [162, 165, 'ctrl_l', 'alt_gr'], [163, 'ctrl_r'], ['left', 37], [40, 'down'], [39, 'right'], [96, 'NumPad0'], ['NumPad_Del', 110]]

#reorder numbers to be first element
for list in res:
    if isinstance(list[1], int):
        list[0], list[1] = list[1], list[0]

#sort list elements by number
rescopy = res
for i, list in zip(range(len(rescopy)), rescopy):
    for i, list in zip(range(len(rescopy)-1), rescopy):
        if res[i][0] > res[i+1][0]:
            res[i], res[i+1] = res[i+1], res[i]

#remove duplicates
b = []
for sublist in res:
    if sublist not in b:
        b.append(sublist)

#sorted and cleaned hotkey list
finallist = [[8, 'backspace'], [9, 'tab'], [13, 'enter'], [20, 'caps_lock'], [27, 'esc'], [32, 'space'], [33, 'page_up'], [34, 'page_down'], [35, 'end'], [36, 'home'], [37, 'left'], [38, 'up'], [39, 'right'], [40, 'down'], [44, 'print_screen'], [45, 'insert'], [46, 'delete'], [48, '0'], [49, '1'], [50, '2'], [51, '3'], [52, '4'], [53, '5'], [54, '6'], [55, '7'], [56, '8'], [57, '9'], [65, 'a'], [66, 'b'], [67, 'c'], [68, 'd'], [69, 'e'], [70, 'f'], [71, 'g'], [72, 'h'], [73, 'i'], [74, 'j'], [75, 'k'], [76, 'l'], [77, 'm'], [78, 'n'], [79, 'o'], [80, 'p'], [81, 'q'], [82, 'r'], [83, 's'], [84, 't'], [85, 'u'], [86, 'v'], [87, 'w'], [88, 'x'], [89, 'y'], [90, 'z'], [91, 'cmd'], [96, 'NumPad0'], [97, 'NumPad1'], [98, 'NumPad2'], [99, 'NumPad3'], [100, 'NumPad4'], [101, 'NumPad5'], [102, 'NumPad6'], [103, 'NumPad7'], [104, 'NumPad8'], [105, 'NumPad9'], [106, '*'], [107, '+'], [109, '-'], [110, 'NumPad_Del'], [111, '-'], [112, 'f1'], [113, 'f2'], [114, 'f3'], [115, 'f4'], [116, 'f5'], [117, 'f6'], [118, 'f7'], [119, 'f8'], [120, 'f9'], [121, 'f10'], [122, 'f11'], [123, 'f12'], [144, 'num_lock'], [160, 'shift'], [161, 'shift_r'], [162, 'ctrl_l'], [163, 'ctrl_r'], [164, 'alt_l'], [165, 162, 'ctrl_l', 'alt_gr'], [175, 'media_volume_up'], [186, 'ü'], [187, '+'], [188, ','], [189, '-'], [190, '.'], [191, '#'], [192, 'ö'], [219, 'ß'], [220, '^'], [221, '´'], [222, 'ä'], [226, '<']]
