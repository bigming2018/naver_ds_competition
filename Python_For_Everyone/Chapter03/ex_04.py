# 모두의 파이썬 Chapter03 실습 문제 2번
# 급여 계산기

sh = input("Enter Hours: ")  # 근무 시간
sr = input("Enter Rate: ")   # 근무 시급
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit() # 뒷 부분 코드를 실행하지 않음

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    # print(reg,otp)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:",xp)