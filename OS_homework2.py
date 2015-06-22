import random		#by 資網四B D1004342054 劉定岳
import os 

P0_Allocation 	=[random.randint(0,3),random.randint(0,3),random.randint(0,3)] #宣告狀態、最大、需求
P1_Allocation 	=[random.randint(0,3),random.randint(0,3),random.randint(0,3)]
P2_Allocation 	=[random.randint(0,3),random.randint(0,3),random.randint(0,3)]
P3_Allocation 	=[random.randint(0,3),random.randint(0,3),random.randint(0,3)]
P4_Allocation 	=[random.randint(0,3),random.randint(0,3),random.randint(0,3)]
P0_Max 			=[random.randint(P0_Allocation[0],7),random.randint(P0_Allocation[1],7),random.randint(P0_Allocation[2],7)]
P1_Max 			=[random.randint(P1_Allocation[0],7),random.randint(P1_Allocation[1],7),random.randint(P1_Allocation[2],7)]
P2_Max 			=[random.randint(P2_Allocation[0],7),random.randint(P2_Allocation[1],7),random.randint(P2_Allocation[2],7)]
P3_Max 			=[random.randint(P3_Allocation[0],7),random.randint(P3_Allocation[1],7),random.randint(P3_Allocation[2],7)]
P4_Max 			=[random.randint(P4_Allocation[0],7),random.randint(P4_Allocation[1],7),random.randint(P4_Allocation[2],7)]
P0_Need			=[P0_Max[0]-P0_Allocation[0],P0_Max[1]-P0_Allocation[1],P0_Max[2]-P0_Allocation[2],0,'P0']
P1_Need			=[P1_Max[0]-P1_Allocation[0],P1_Max[1]-P1_Allocation[1],P1_Max[2]-P1_Allocation[2],0,'P1']
P2_Need			=[P2_Max[0]-P2_Allocation[0],P2_Max[1]-P2_Allocation[1],P2_Max[2]-P2_Allocation[2],0,'P2']
P3_Need			=[P3_Max[0]-P3_Allocation[0],P3_Max[1]-P3_Allocation[1],P3_Max[2]-P3_Allocation[2],0,'P3']
P4_Need			=[P4_Max[0]-P4_Allocation[0],P4_Max[1]-P4_Allocation[1],P4_Max[2]-P4_Allocation[2],0,'P4']




print("行程\t","Allocation\t","Max")		#列出隨機產生之各行程與狀態
print("P0\t",P0_Allocation,"\t",P0_Max)
print("P1\t",P1_Allocation,"\t",P1_Max)
print("P2\t",P2_Allocation,"\t",P2_Max)
print("P3\t",P3_Allocation,"\t",P3_Max)
print("P4\t",P4_Allocation,"\t",P4_Max)


user = input("請輸入初始狀態(如a,b,c)：")
try:
	user = a, b, c = user.split(",")
	user = [int(user[0]),int(user[1]),int(user[2])]
except:										#格式檢查
	print("請輸入正確格式！")
	os.system("pause")
	quit()

print("初始狀態：",user)


program_Need=[P0_Need,P1_Need,P2_Need,P3_Need,P4_Need]

program_Allocation=[P0_Allocation,P1_Allocation,P2_Allocation,P3_Allocation,P4_Allocation]
i=1
text="可以配置，安全序列為"
while i<=5:
	j=0
	for P in program_Need:	#開始進行排序
		if(user[0]>=P[0] and user[1]>=P[1] and user[2]>=P[2] and P[3]==0):
			print("%s需要[%s, %s, %s] <= 現有資源%s" % (P[4],P[0],P[1],P[2],user))
			user[0] = user[0] + program_Allocation[j][0]
			user[1] = user[1] + program_Allocation[j][1]
			user[2] = user[2] + program_Allocation[j][2]
			P[3]=1
			text+=P[4]+" "
		j+=1

	i+=1
print("")
if(len(text)==25):
	print(text)
else:
	print("現有資源不足，無法配置！")

os.system("pause")