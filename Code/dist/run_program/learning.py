from pynput import keyboard
import time

# The key combination to check
COMBINATIONS = []

# The currently active modifiers
current = set()
current2 = set()

def main():
    def execute():
        print (f"Hotkeys {current} pressed")

    def on_press(key):
        if hasattr(key, 'vk'):
            current.add(key.vk)
            current2.add(key)

        else:
            current.add(key.value.vk)
            current2.add(key)


    def on_release(key):
        if len(COMBINATIONS) != 1:
            COMBINATIONS.append(set(current))
            COMBINATIONS.append(set(current2))
            current.clear()

        print(current)
        print(COMBINATIONS)


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

main()
