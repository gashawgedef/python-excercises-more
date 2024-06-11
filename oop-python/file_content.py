
fh = open("C:\\Users\\ggashaw\\Documents\\files\\example.txt","a")

# fh.write("Dear Gashaw Gedef welcome to Addis Ababa this year.\n")
# fh.write("Dear Gashaw Gedef welcome to Addis Ababa this year.\n")
try:
 for i in range(1,11):
        fh.write("Line: %d \n" %i)
        
finally:
    fh.close()
