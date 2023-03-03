def main():
    x= input()
    print(convert(x))

def convert(x):
    s= x.replace(":)",'\N{Slightly Smiling Face}').replace(":(",'\N{Slightly Frowning Face}')
    return s

main()
