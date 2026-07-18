"""2999"""
def main():
    """main"""
    text = str(input())
    row_1 = len(text)
    row_2 = str('*' + text + '*')
    roe_3 = len(row_2)
    for i in range(len(row_2)):
        print('*', end = '')
    print()
    print('*'+(text)+'*')
    for i in range(len(row_2)):
        print('*', end = '')
main()
