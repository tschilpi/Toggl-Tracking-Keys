from pynput.keyboard import Key, KeyCode, Listener
import main_test
import config
from functools import partial
import time

## Code used from this website: https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/?utm_source=pocket_saves
## Code has been altered to fit the needs of this application

def execute_hotkeys(hotkeylist):
    def function_1(project_value):
        """ One of your functions to be executed by a combination """
        if not config.tracking1:
            main_test.start_tracking(project_value)
            config.tracking1 = True
            print('Started tracking.')

        else:
            main_test.end_tracking(config.time_entry)
            config.tracking1 = False
            print('Ended tracking.')


    # Create a mapping of keys to function (use frozenset as sets/lists are not hashable - so they can't be used as keys)
    # Note the missing `()` after function_1 and function_2 as want to pass the function, not the return value of the function
    combination_to_function = {}

    print(hotkeylist)
    for i, tuple in enumerate(hotkeylist):
        combination_to_function[tuple[0]] = partial(function_1, tuple[1])


    # The currently pressed keys (initially empty)
    pressed_vks = set()


    def get_vk(key):
        """
        Get the virtual key code from a key.
        These are used so case/shift modifications are ignored.
        """
        return key.vk if hasattr(key, 'vk') else key.value.vk


    def is_combination_pressed(combination):
        """ Check if a combination is satisfied using the keys pressed in pressed_vks """
        return combination == pressed_vks


    def on_press(key):
        if get_vk(key) not in pressed_vks:
            """ When a key is pressed """
            vk = get_vk(key)  # Get the key's vk
            pressed_vks.add(vk)  # Add it to the set of currently pressed keys

            print(pressed_vks)

            for combination in combination_to_function:  # Loop through each combination
                if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
                    print(config.tracking1)
                    pressed_vks.clear()
                    combination_to_function[combination]()  # If so, execute the function


    def on_release(key):
        pass# """ When a key is released """
        # vk = get_vk(key)  # Get the key's vk
        # pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys


    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    return(listener)
