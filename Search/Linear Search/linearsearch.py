

def main():
    list_of_oddnumbers = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
    target = int(input("Enter your search target: "))
    linearsearch(target,list_of_oddnumbers)

def linearsearch(target,list_of_oddnumbers):
    for i in range(len(list_of_oddnumbers)):
        if list_of_oddnumbers[i] == target:
            print("The Target {}: It taked {} step/s to find that target".format(target,i))
            return
    print("Not Found")

if __name__ == "__main__":
    main()
