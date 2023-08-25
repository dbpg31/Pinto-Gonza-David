import os
os.system("cls")

bhorasAusencia = float (input("horas Ausencia : ")) <= 1.5
bTDefectuosos = int(input("Tornillos Defectuosos : ")) < 300
bTBuenos = int(input("Tornillos Buenos : ")) > 10000

if not bhorasAusencia and not bTDefectuosos and not bTBuenos : grado = 5
elif bhorasAusencia and not bTDefectuosos and not bTBuenos : grado = 7
elif not bhorasAusencia and bTDefectuosos and not bTBuenos : grado = 8
elif not bhorasAusencia and not bTDefectuosos and bTBuenos : grado = 9
elif bhorasAusencia and bTDefectuosos and not bTBuenos : grado = 12
elif bhorasAusencia and not bTDefectuosos and bTBuenos : grado = 13
elif not bhorasAusencia and bTDefectuosos and bTBuenos : grado = 15
elif bhorasAusencia and bTDefectuosos and bTBuenos : grado = 20

