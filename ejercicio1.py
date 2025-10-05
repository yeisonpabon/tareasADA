
#ejercico 1 
#divide y venceras 
class Tarea:
    def __init__(self, nombre, tiempo, prioridad):
        self.nombre = nombre
        self.tiempo = tiempo
        self.prioridad = prioridad
    
    def __repr__(self):
        return f"Tarea({self.nombre}, tiempo={self.tiempo}h, prioridad={self.prioridad})"


def merge_tareas(izq, der):

    resultado = []
    i = j = 0
    
    while i < len(izq) and j < len(der):
        # Comparar por prioridad primero (menor número es mayor prioridad)
        if izq[i].prioridad < der[j].prioridad:
            resultado.append(izq[i])
            i += 1
        elif izq[i].prioridad > der[j].prioridad:
            resultado.append(der[j])
            j += 1
        else:
            # Si tienen la misma prioridad, ordenar por tiempo (menor primero)
            if izq[i].tiempo <= der[j].tiempo:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1
    
    # Agregar elementos restantes
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado

def merge_sort_tareas(tareas):

    # Caso base: lista vacía o con un solo elemento
    if len(tareas) <= 1:
        return tareas
    
    # Dividir: encontrar el punto medio
    medio = len(tareas) // 2
    izquierda = tareas[:medio]
    derecha = tareas[medio:]
    
    # Conquistar: ordenar recursivamente cada mitad
    izq_ordenada = merge_sort_tareas(izquierda)
    der_ordenada = merge_sort_tareas(derecha)
    
    # Combinar: mezclar las dos mitades ordenadas
    return merge_tareas(izq_ordenada, der_ordenada)


def mostrar_tareas(tareas, titulo="Tareas"):
    print(f"\n{titulo}:")
    print("-" * 60)
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea.nombre:20}  Prioridad: {tarea.prioridad} Tiempo: {tarea.tiempo}h")
    print("-" * 60)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear lista de tareas de ejemplo
    tareas = [
        Tarea("Diseñar interfaz", 5, 3),
        Tarea("Corregir bug crítico", 2, 1),
        Tarea("Reunión equipo", 1, 2),
        Tarea("Documentar API", 8, 5),
        Tarea("Actualizar dependencias", 3, 1),
        Tarea("Revisar código", 4, 2),
        Tarea("Optimizar consultas", 6, 3),
        Tarea("Testing unitario", 7, 4),
        Tarea("Implementar feature", 10, 1),
        Tarea("Refactorizar módulo", 5, 4)
    ]
    
    
    # Ordenar tareas usando divide y vencerás
    tareas_ordenadas = merge_sort_tareas(tareas)
    
    # Mostrar tareas ordenadas
    mostrar_tareas(tareas_ordenadas, "Tareas Ordenadas")
    

    print(f"   - Tareas procesadas: {len(tareas)}")
