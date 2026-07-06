"""3011"""
def main():
    """main"""
    color_1 = str(input())
    color_2 = str(input())
    if color_1 == 'Red' and color_2 == 'Yellow':
        print("Orange")
    elif color_1 == 'Yellow' and color_2 == 'Red':
        print("Orange")
    elif color_1 == 'Red' and color_2 == 'Blue':
        print("Violet")
    elif color_1 == 'Blue' and color_2 == 'Red':
        print("Violet")
    elif color_1 == 'Yellow' and color_2 == 'Blue':
        print("Green")
    elif color_1 == 'Blue' and color_2 == 'Yellow':
        print("Green")
    elif color_1 == 'Blue' and color_2 == 'Blue':
        print("Blue")
    elif color_1 == 'Red' and color_2 == 'Red':
        print("Red")
    elif color_1 == 'Yellow' and color_2 == 'Yellow':
        print("Yellow")
    else :
        print("Error")
main()
