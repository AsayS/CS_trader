import webbrowser


# Create dict from txt file
d = {}
with open("item_search/buffids.txt", "r") as fp:
    lines = fp.readlines()
for line in lines:
    key, value = line.split(";")
    d[value] = key


search_for = "AK-47 | Bloodsport (Factory New)"
usp = "USP-S | Overgrowth"
val = 34444


all_found = []
# Search for buff value fomr skin name
for key, value in d.items():
    if usp in key:
        all_found.append(value)


print(all_found[0])
print(type(all_found))

webbrowser.open_new_tab("https://buff.163.com/goods/" + str(all_found[0]))
webbrowser.get('chrome %s').open_new_tab(
    "https://buff.163.com/goods/" + str(all_found[0]))
