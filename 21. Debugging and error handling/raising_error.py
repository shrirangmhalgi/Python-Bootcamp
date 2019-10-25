def colorize(text, color):
    if type(text) is not str or type(color) is not str :
        raise TypeError("text and color both should be a string...")
    elif color not in ('red', 'blue', 'green'):
        raise ValueError("color shoud be either Red or Green or Blue")
    print(f"printed {text} in {color} color")

colorize("hey", "red")