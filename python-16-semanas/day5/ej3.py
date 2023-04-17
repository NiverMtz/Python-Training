# def ceros_repetidos(*args):
#     for i, e in enumerate(args):
#         if i < len(args) - 1 and (e, args[i+1]) == (0, 0):
#             return True
#     return False

def ceros_repetidos(*args):
    return True in [True if i < len(args) - 1 and (e, args[i+1]) == (0, 0) else False for i, e in enumerate(args)]


resultado = ceros_repetidos(2, 3, 1, 0, 0, 0, 1)
print(resultado)
