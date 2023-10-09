input_dias = int(input())
anos = input_dias // 365
mod_anos = input_dias % 365
meses = mod_anos // 30
mod_meses = mod_anos % 30
dias = mod_meses

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')