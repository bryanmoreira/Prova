sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

total_1 = round(((sp/total)*100), 2)
print(f"Em SP a distribuidora teve o valor mensal de {total_1}%")
total_2 = round(((rj/total)*100),2)
print(f"Em RJ a distribuidora teve o valor mensal de {total_2}%")
total_3 = round(((mg/total)*100),2)
print(f"Em MG a distribuidora teve o valor mensal de {total_3}%")
total_4 = round(((es/total)*100),2)
print(f"Em ES a distribuidora teve o valor mensal de {total_4}%")
total_5 = round(((outros/total)*100),2)
print(f"Em Outros estados, a distribuidora teve o valor mensal de {total_5}%")
