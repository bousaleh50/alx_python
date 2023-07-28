if __name__=="__main__":
    import sys
    
    if(len(sys.argv)==0):
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv)))
        for i in range(len(sys.argv)):
            print("{}: {}".format(i+1,sys.argv[i]))
        