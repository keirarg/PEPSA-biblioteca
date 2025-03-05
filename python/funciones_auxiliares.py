import decimal
import json
import bleach

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)
        
def calculariva(importe):
    return importe*0.21       
        
def sanitize_input (user_input):
    return bleach.clean(user_input)