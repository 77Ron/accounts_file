# Write, update, and delete account info in a saved dictionary file.
# Display file by selected department and surname initial.
# Display account table with pandas.
# Display account graph with matplotlib. 
# Create a MySQL file from the account dictionary file.

#Changes to individual accounts requires delete and re-entry a this time.
#Database creation not available yet.

from datetime import datetime
from accounts_dictionary import *


def main():

    print("Company name: ",company_name)

    fl1 = ""
    while fl1 != 'E':
        fl1 = input("U'pdate accounts, P'rint accounts, T'able view, G'raph view, C'reate database, L'ogin view, E'xit: ")
        if fl1 == 'U':
            with open("accts1", "a") as f:
                uname = input("Enter username: ")
                f.write(uname + " logged in " + str(datetime.now())+ " - ")
            UpdateDictFile()
            with open("accts1", "a") as f:
                f.write(uname + " saved changes " + str(datetime.now())+ " | ")

        elif fl1 == 'P':
            PrintDictFile()

        elif fl1 == 'T':
            TableDictFile()
            
        elif fl1 == 'G':
            GraphDictFile()

        elif fl1 == 'L':
            try:
                with open("accts1", "r") as f:
                    for line1 in f:
                        print(line1)
            except Exception:
                print("Login file does not exist or cannot be opened.")

        elif fl1 == 'C':
            print("Option not avaiable yet.")

    exit()


if __name__ == '__main__':
    main()