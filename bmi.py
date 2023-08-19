#小程式:BMI值計算程式

height = input('請輸入身高(公分)')
weight = input('請輸入體重(公斤)')

#型別轉換
height = float(height)
weight = float(weight)

#計算bmi值
bmi = weight / (height / 100)**2
print('你的BMI值為：',bmi)

#if架構
if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('體重標準')
else:
	print('體重過重')