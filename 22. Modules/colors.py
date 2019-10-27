import termcolor as color

# print(dir(color)) # -> gives directory of functions
# help(color) # -> gives documentaion of functions

# color.cprint("hello python", color="blue", on_color="white", attrs=["blink"])
print(color.colored("Hello python", color="magenta", on_color="on_cyan", attrs=["blink"]))