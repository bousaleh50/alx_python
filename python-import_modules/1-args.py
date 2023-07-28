if __name__=="__main__":
    import sys
    
    if(len(sys.argv)==0):
        print("0 arguments.")
    else:
        print(f"{len(sys.argv)-1} arguments:" if len(sys.argv)==1 else f"{len(sys.argv)-1} argument")
        for i in range(1,len(sys.argv)):
            print("{}: {}".format(i,sys.argv[i]))
        