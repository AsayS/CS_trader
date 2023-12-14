import webbrowser
import win32clipboard
import keyboard
import time

def open_browser(link):
    webbrowser.open_new_tab("https://buff.163.com/goods/" + link)



# Create dict from txt file
d = {}
with open(r"buffids.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
for line in lines:
    key, value = line.split(";")
    d[value] = key

all_found = []

while not keyboard.is_pressed("f12"):
    if keyboard.is_pressed("f9"):
        win32clipboard.OpenClipboard()
        search = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        all_found.clear()
        # Search for buff value fomr skin name
        for key, value in d.items():
            if search in key:
                all_found.append(value)
                time.sleep(0.1)
                webbrowser.open_new_tab("https://buff.163.com/goods/" + all_found[0])
                break
    # if keyboard.is_pressed("f10"):
    #     time.sleep(0.1)
    #     open_browser(all_found[0])
    

# webbrowser.open_new_tab("https://buff.163.com/goods/" + all_found[0])