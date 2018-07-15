# 모두의 파이썬 Chapter03 실습 문제 1번
# 급여 계산기

sh = input("Enter Hours: ")  # 근무시간
sr = input("Enter Rate: ")   # 근무시급
fh = float(sh)
fr = float(sr)

if fh > 40:
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    # print(reg,otp)
    xp = reg + otp
else:
    # print("regular")
    xp = fh * fr
print("Pay:",xp)