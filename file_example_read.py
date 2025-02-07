fp = open("text1.txt","r")
print(fp.read())
fp.close()
with open("text1.txt","r") as fp:
    print(fp.read())
print("we are done, the context closed by the incident")

with open("text1.txt","r") as fp:
    for line in fp:
        print(line,end="")
        print(line.rstrip())
with open("text1.txt","r") as fp:
    line_number=1
    for line in fp:
        print(f"{line_number}:{line.rstrip()}")
        line_number+=1