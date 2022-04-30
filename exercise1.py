#

def main():
    for i in range(1, 101):
        text = ""
        if i % 3 == 0:
            text = "cyber"
        if i % 5 == 0:
            text += "click"

        msg = i if text == "" else text
        print(msg)


if __name__ == '__main__':
    main()
