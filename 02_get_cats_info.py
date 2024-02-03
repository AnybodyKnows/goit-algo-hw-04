
def get_cats_info(path):
    try: 
        with open(path,"r") as file1:
            cat_inf = []
            for lines in file1:
                str = lines.strip()
                str = str.split(",")
                keys = ["id", "name", "age"]
                dict_tmp = dict(zip(keys,str))
                cat_inf.append(dict_tmp)
    except:
        return f"file {path} not found"  
    return  cat_inf       

print(get_cats_info("cats.txt"))


