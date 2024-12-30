
try:

    with (
        open("file2.txt","r") as f2,
        open("file1.txt","r") as f1,
        open("file3.txt","r") as f3
    ):
        print(f1.readlines(),f2.readlines(),f3.readlines())

except Exception as e:
    print(e)


print("End of the program")