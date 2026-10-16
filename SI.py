import sys
def simpleint(pr,intr,time):
    return (pr*intr*time)/100
if __name__=="__main__":
    pr=int(sys.argv[1])
    intr=int(sys.argv[2])
    time=int(sys.argv[3])
print("Simple interest:",simpleint(pr,intr,time))    