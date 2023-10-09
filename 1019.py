input_segs = int(input())
horas = int(input_segs / 3600)
mod_hora = input_segs % 3600
minutos = int(mod_hora / 60)
mod_minutos = mod_hora % 60
segundos = mod_minutos

print(f'{horas}:{minutos}:{segundos}')