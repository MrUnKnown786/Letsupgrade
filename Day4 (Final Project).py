'''
Hey you are a chemist from India and you work with degree celsius in your day to day life but due to a project your company had collaborated with a MNC company, where the chemists use degree frainite for their purposes, and to maintain collaboration consistent we want to have a easy degree conversion, 

Please develop a python based degree converter which takes °C value and give you output of °F 


Input - 

°C -> 50

Output - 

°F -> 122 


Formula for Conversion 



___°C × 9/5) + 32 = ___°F

'''

C = float(input("Enter Temperature in °C : "))
F = (C*9)/5 + 32
print("Temperature in °F :",F)
