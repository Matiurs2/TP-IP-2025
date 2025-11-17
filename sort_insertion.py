# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)
min_idx = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    global i, n, j, items

    a = j-1
    b = j

    if i >= n:
        return {"done": True}

    if j == None:
        j = i 
        
    if j > 0 and items[a] > items[b]:
        items[b], items[a] = items[a], items[b]
        return {"a": a, "b": b, "swap": True, "done": False} 
        j -= 1
        
    
    i += 1
    j = None

    return {"done": False}

    #NO FUNCIONA

    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    
