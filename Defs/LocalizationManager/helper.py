import Defs.ThemeManager.theme as theme
default_palette = theme.default_palette

def print_sorted_as_menu(sorting_list):
    col_width = max(len(word) for row in sorting_list for word in row) + 2
    for row in sorting_list:
        print("".join(word.ljust(col_width) for word in row).format(default_palette[0], default_palette[2]))