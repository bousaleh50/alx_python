if __name__=="__main__":
    import sys
    
    if(len(sys.argv)-1==0):
        print("0 arguments.")
    else:
        if(len(sys.argv)-1==1):
            print("1 argument:")
            print(f"1: {sys.argv[1]}")
        else:
            print(f"{len(sys.argv)-1} arguments:")
            for i in range(1,len(sys.argv)):
                print("{}: {}".format(i,sys.argv[i]))
        