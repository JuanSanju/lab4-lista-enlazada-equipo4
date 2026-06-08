# src/linked_list.py
# Estructura base — cada equipo implementa su operación asignada.

class Node:
    """Nodo de la lista enlazada."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Lista enlazada simple."""

    def __init__(self):
        self.head = None

    # ------------------------------------------------------------------ #
    # Implementado por el docente — NO modificar                          #
    # ------------------------------------------------------------------ #
    def __str__(self):
        """Retorna una representación legible de la lista."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Lista vacía"

    def __len__(self):
        """Retorna el número de nodos."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # ------------------------------------------------------------------ #
    # TODO — Equipo B: rama feature/delete                                #
    # ------------------------------------------------------------------ #
    def delete(self, data):
        # lista vacía
        if self.head is None:
            return False

        # el dato está en la cabeza
        if self.head.data == data:
            self.head = self.head.next
            return True

        # buscar el nodo a eliminar
        actual = self.head

        while actual.next is not None:
            if actual.next.data == data:
                actual.next = actual.next.next
                return True

            actual = actual.next

        # no se encontró el dato
        return False
