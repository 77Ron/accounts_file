# Write, update, and delete account info in a saved dictionary file.
# Display file by department and surname initial.
# Display account table with pandas.
# Display account graph with matplotlib.
# 
# ------- Not available at this time. ----------
# Create or update a MySQL database from the account dictionary file.
# Import accounts from a MySQL database.
# Import accounts from a text file.


from accounts_dictionary import *


def main():

    print("Company name: ",company_name)

    fl1 = ""
    while fl1 != 'E':
        fl1 = input("(U)pdate accounts, (P)rint, (T)able, (G)raph, (D)atabase update, (I)mport database, (txt) file import, (L)ogin print, (E)xit: ")
        
        if fl1 == 'U':
            uname = input("Enter username: ")
            with open("accts1", "a") as f:
                f.write(uname + " logged in " + str(datetime.now())+ " - ")
            UpdateDictFile()
            with open("accts1", "a") as f:
                f.write(uname + " saved changes " + str(datetime.now())+ " \n ")

        elif fl1 == 'P':
            PrintDictFile()

        elif fl1 == 'T':
            TableDictFile()
            
        elif fl1 == 'G':
            GraphDictFile()
      
        elif fl1 == 'D':
            print("Option not avaiable yet.")

        elif fl1 == 'I':
            print("Option not avaiable yet.")

        elif fl1 == 'txt':
            print("Option not avaiable yet.") 
        
        elif fl1 == 'L':
            LogFile()
   
        elif fl1 == 'Reformat':
            ReformatDictFile()
    
    exit()

if __name__ == '__main__':
    main()