

def total_salary(path):
    with open(path,"r") as file1:
        lines = [ l for l in file1.readlines()] 
        print(lines) 
        total = 0
        for i in lines:
            str= i.split(",")
            total = total + float(str[1])
            avg = total / len(lines)
        return(f"Total={total}  AVG = {avg}")

print(total_salary("s.txt"))

