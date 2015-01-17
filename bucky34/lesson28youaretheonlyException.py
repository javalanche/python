while True:
    try:
	number = int(input("What's your favorite number?:"))
	print(18/number)
	# print(number) must run if not break will not, e.g. print(tuna) will cause an infinite loop
	break
    except NameError, e:
        print("Make sure you enter a number.")
    except ZeroDivisionError, e:
        print("Don't pick zero")
    except :
        break
    finally: # not matter what this will run every loop	
	print("loop complete")


