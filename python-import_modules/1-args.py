if __name__=="__main__":
    import sys
    
    if(len(sys.argv)==0):
        print("0 arguments.")
    else:
        if(len(sys.argv)==1):
            print("1 argument:")
        else:
            print(f"{len(sys.argv)} arguments:")
            for i in range(1,len(sys.argv)):
                print("{}: {}".format(i,sys.argv[i]))
        