import urllib

def read_text():
    quotes = open("C:\Users\jf732h\Dropbox\udacity\programmingFoundationsWithPython\lesson1\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("BAD WORD(S)!")
    elif "false" in output:
            print("clean")
    else:
        print("something went wrong!*:~\\")
    
read_text()
