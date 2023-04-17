texto = "Nunc non molestie nisl. Cras aliquet posuere felis at porta. Suspendisse viverra dui varius iaculis " \
        "venenatis. Suspendisse arcu elit, elementum a lorem vitae, bibendum commodo orci. Praesent eu erat ac mi " \
        "sollicitudin pulvinar non in nunc. Nunc volutpat dui elit, efficitur cursus dolor vulputate sollicitudin. "
texto = texto.lower()
texto = texto.split()
texto = [e.replace('.', '') if '.' in e else e for e in texto]
texto = [e.replace(',', '') if '.' in e else e for e in texto]
print(texto)
