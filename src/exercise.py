def main():
    #write your code below this line'
    name = ""
    greatest = 0
    while True:
        details = input()
        if (details != ""):
            details_split = details.split(",")
            if (int(details_split[1]) > greatest):
                name = details_split[0]
                greatest = int(details_split[1])
        else:
            break
    print("Name of the oldest: " + name)

if __name__ == '__main__':
    main()
