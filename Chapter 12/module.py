def myFunc():
    print("Hello World")


# agar __name__ jis file mein likhe hai usi ko run kiye ---> then we'll get __main__
# agar koi file ke code ko import kar rahe hai ---> then we'll get the file name jisse import kiye hai

if __name__=="__main__":    # If this code is directly executed by running the file it is present in
    print("We are directly running this code")
    myFunc()
    print(__name__)
