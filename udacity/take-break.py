import webbrowser
import time

totalBreak = 3
breakCount = 0

print("THis program started on "+time.ctime())
while(breakCount < totalBreak):
    time.sleep(10)
    webbrowser.open("https://play.google.com/music/listen#/now")
    breakCount = breakCount + 1
