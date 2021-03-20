def valida_password(var_password):
    lista_deny = [".","-"]
    var_respuesta = False if ((var_password[0] in lista_deny) or (var_password[-1] in lista_deny)) else True
    return var_respuesta

def compara_passwords(var_pass_1, var_pass_2):
    return True if var_pass_1 == var_pass_2 else False