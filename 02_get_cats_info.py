
def get_cats_info(path):
    with open(path,"r") as file1:
        lines = [ l for l in file1.readlines()] 
        print(lines)
        for i in lines:
            str= i.split(",")
            print(str) 
    
print(get_cats_info("cats.txt"))