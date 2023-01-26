wage = float(input('Digite o salário: R$'))
newWage = wage + (wage * 15 / 100)
print(f'Após o aumento de 15% no salário de R${wage:.2f}, o salário atual é de R${newWage:.2f}')