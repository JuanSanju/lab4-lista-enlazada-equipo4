# tests/test_linked_list.py
# Pruebas base escritas por el docente.
# CADA EQUIPO agregará sus propias pruebas en este archivo
# desde su rama — esto generará merge conflicts intencionales.

import pytest
from src.linked_list import LinkedList, Node


# ------------------------------------------------------------------ #
# Pruebas del docente — __str__ y __len__                             #
# ------------------------------------------------------------------ #

def test_lista_vacia_str():
    ll = LinkedList()
    assert str(ll) == "Lista vacía"


def test_lista_vacia_len():
    ll = LinkedList()
    assert len(ll) == 0


def test_node_repr():
    n = Node(42)
    assert repr(n) == "Node(42)"

#-----------------------
#PRUEBAS PARA LA FUNCIONALIDAD search()
#--------------------------
def test_search_elemento_existente():
    ll = LinkedList()
    ll.head = Node(10)
    ll.head.next = Node(20)
    nodo = ll.search(10)
    assert nodo is not None
    assert nodo.data == 10


def test_search_elemento_inexistente():
    ll = LinkedList()
    ll.head = Node(5)
    assert ll.search(99) is None


def test_search_lista_vacia():
    ll = LinkedList()
    assert ll.search(1) is None


def test_search_ultimo_elemento():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
  
    nodo = ll.search(3)
    assert nodo is not None
    assert nodo.data == 3