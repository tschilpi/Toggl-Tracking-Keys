from pynput import keyboard
import hotkeys_finalversion
import time
import re

#sorted and cleaned hotkey list
finallist = [[8, 'backspace'], [9, 'tab'], [13, 'enter'], [20, 'caps_lock'], [27, 'esc'], [32, 'space'], [33, 'page_up'], [34, 'page_down'], [35, 'end'], [36, 'home'], [37, 'left'], [38, 'up'], [39, 'right'], [40, 'down'], [44, 'print_screen'], [45, 'insert'], [46, 'delete'], [48, '0'], [49, '1'], [50, '2'], [51, '3'], [52, '4'], [53, '5'], [54, '6'], [55, '7'], [56, '8'], [57, '9'], [65, 'a'], [66, 'b'], [67, 'c'], [68, 'd'], [69, 'e'], [70, 'f'], [71, 'g'], [72, 'h'], [73, 'i'], [74, 'j'], [75, 'k'], [76, 'l'], [77, 'm'], [78, 'n'], [79, 'o'], [80, 'p'], [81, 'q'], [82, 'r'], [83, 's'], [84, 't'], [85, 'u'], [86, 'v'], [87, 'w'], [88, 'x'], [89, 'y'], [90, 'z'], [91, 'cmd'], [96, 'NumPad0'], [97, 'NumPad1'], [98, 'NumPad2'], [99, 'NumPad3'], [100, 'NumPad4'], [101, 'NumPad5'], [102, 'NumPad6'], [103, 'NumPad7'], [104, 'NumPad8'], [105, 'NumPad9'], [106, '*'], [107, '+'], [109, '-'], [110, 'NumPad_Del'], [111, '-'], [112, 'f1'], [113, 'f2'], [114, 'f3'], [115, 'f4'], [116, 'f5'], [117, 'f6'], [118, 'f7'], [119, 'f8'], [120, 'f9'], [121, 'f10'], [122, 'f11'], [123, 'f12'], [144, 'num_lock'], [160, 'shift'], [161, 'shift_r'], [162, 'ctrl_l'], [163, 'ctrl_r'], [164, 'alt_l'], [165, 'alt_gr'], [175, 'media_volume_up'], [186, 'ü'], [187, '+'], [188, ','], [189, '-'], [190, '.'], [191, '#'], [192, 'ö'], [219, 'ß'], [220, '^'], [221, '´'], [222, 'ä'], [226, '<']]

# The key combination to check
COMBINATIONS = []

# The currently active modifiers
current = set()

def main():

    def on_press(key):

        #only allow 2 hotkeys to be recorded

        if len(current) < 2:
            if hasattr(key, 'vk'):
                current.add(key.vk)
            else:
                current.add(key.value.vk)


    def on_release(key):

        if len(COMBINATIONS) !=1:
            COMBINATIONS.append(set(current))
            current.clear()

        return False



    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


    my_dict = {lst[0]: lst[1] for lst in finallist}

    if len(COMBINATIONS[0]) != 1:

        # Initialize an empty list to hold the values of the keys
        value_list = []

        # Loop over the keys in the set and fetch the corresponding values
        for key in COMBINATIONS[0]:
            value_list.append(my_dict[key])

        # Concatenate the values with a '+' operator
        concatenated_string = " ".join(value_list)

        if concatenated_string[0].isdigit() and len(concatenated_string) == 3:
            # swap digits with letters
            output_string = concatenated_string[2] + ' + ' + concatenated_string[0]
            return(output_string.title())

        # Capitalize the concatenated string
        capitalized_string = concatenated_string.title()

        # Split the capitalized string into a list of words and sort by their length
        sorted_words = sorted(capitalized_string.split(), key=len, reverse=True)

        # Join the sorted words back into a single string with a space in between them
        two_hotkeys = " + ".join(sorted_words)
        return(two_hotkeys)


    else:
        for key in COMBINATIONS[0]:
            one_hotkey = my_dict[key].capitalize()
            return(one_hotkey)


    # gg
    #
    # time.sleep(2)

#hotkeys_finalversion.execute_hotkeys(fset)