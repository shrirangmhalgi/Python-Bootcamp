import pyfiglet as pf
import termcolor as tc

def print_art(input_text, input_color):
    valid_colors = (
        "red",
        "blue",
        "green",
        "cyan",
        "magenta",
        "yellow",
        "white")

    if input_color not in valid_colors:
        input_color = "blue"

    print(tc.colored(pf.figlet_format(input_text), color=input_color))

if __name__ == "__main__":
    input_text = input("Enter the text you want to print... : ")
    input_color = input("Enter the color you want to print... : ")
    
    print_art(input_text, input_color)

# help(pf)
# autopep8 --in-place -a -a -a file_name.py