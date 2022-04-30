# Code that prints a list of numbers from 1 to 100 changing multiples of three
# for "cyber", multiples of 5 for "click" and multiples of both for "cyberclick"

def main():
    for i in range(1, 101):
        text = ""
        if i % 3 == 0:
            text = "cyber"
        if i % 5 == 0:
            text += "click"

        # if none of the conditions are met, print the number
        msg = i if text == "" else text
        print(msg)


if __name__ == '__main__':
    main()
