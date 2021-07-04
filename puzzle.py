from logic import *
#Knight prolect solution
#Ing. Brayan Andru Montenegro Embus

people = ["A", "B"]
rol = ["knight", "knave"]

A_kni = Symbol("A_knight")
B_kni = Symbol("B_knight")
C_kni = Symbol("C_knight")

A_kna = Symbol("A_knave")
B_kna = Symbol("B_knave")
C_kna = Symbol("C_knave")
knowledge = And()
knowledge.add(And(
    Or(A_kni, A_kna), Or(B_kni, B_kna), Or(C_kni, C_kna)
))

knowledge.add(And(Not(And(A_kni, A_kna)), Not(And(B_kni, B_kna)) ))

knowledge.add(And(Not(And(A_kni, B_kni)), Not(And(A_kna, B_kna)) ))

#Implication(Symbol(f"{person}{h1}"), Not(

# Puzzle 0
'''
knowledge.add(A_kna)
print(knowledge.formula())
print(" A says “I am both a knight and a knave.” ")
print(" can A is Knave? ", model_check(knowledge, A_kna))
print("and can A is Knight at the same time? ",model_check(knowledge, A_kni))

'''
# Puzzle 1
'''
knowledge.add(A_kna)
print(knowledge.formula())
print(" A says “We are both knaves.” ")
print(" can A is Knave? ", model_check(knowledge, A_kna))
print("and can B is Knave at the same time? ",model_check(knowledge, B_kna))'''

# Puzzle 2
'''
knowledge.add(A_kna)
print(knowledge.formula())
print("A says “We are the same kind.”")
print(" can A is Knave? ", model_check(knowledge, A_kna))
print("and can B is Knave at the same time? ",model_check(knowledge, B_kna))
print(" can A is Knight? ", model_check(knowledge, A_kni))
print("and can B is Knight at the same time? ",model_check(knowledge, B_kni))'''


# Puzzle 3
knowledge.add(And(Not(And(A_kni, A_kna)), Not(And(B_kni, B_kna)), Not(And(C_kni, C_kna)) ))
knowledge.add(And(Not(And(A_kni, B_kni, C_kni)), Not(And(A_kna, B_kna, C_kna)) ))
knowledge.add(B_kna)
knowledge.add(C_kna)
print(knowledge.formula())
print("A says either “I am a knight.” or “I am a knave.”, but you don’t know which")
print("B says “A said ‘I am a knave.’”", model_check(knowledge, B_kna))
print("B then says “C is a knave.” ",model_check(knowledge, C_kna))
print("C says “A is a knight.” ",model_check(knowledge, A_kni))













