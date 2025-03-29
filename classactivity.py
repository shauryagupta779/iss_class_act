# def find_cube_pairs(target):
#     solutions = []
#     max_num = round(target ** (1/3))  

#     for a in range(1, max_num + 1):
#         for b in range(a, max_num + 1):
#             if a**3 + b**3 == target:
#                 solutions.append((a, b))
#     return solutions

# pairs = find_cube_pairs(1729)

# print("Valid cube pairs for 1729:")
# for a, b in pairs:
#     print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")


def find_cube_pairs(target):
    #missing colon
    solutions = []  #incorrect semicolon and variable name

    max_num = round(target ** (1/3))  #incorrect variable name (targ → target) and exponentiation (** instead of ***)

    for a in range(1, max_num + 1):  #"ranges" to "range"
        for b in range(a, max_num + 1):  #"ranges" to "range"
            if a**3 + b**3 == target:  #exponentiation (** instead of ***), and variable name (targ → target)
                solutions.append((a, b))  #variable name (sol → solutions) and removed semicolon

    return solutions  #return statement (sol → solutions)

# Removed extra comma after function call
pairs = find_cube_pairs(1729)

#"printf" to "print"
print("Valid cube pairs for 1729:")

#incorrect variable name (pair → pairs) in loop
for a, b in pairs:
    #incorrect exponentiation (a**2 → a**3, b**2 → b**3), and incorrect target value (1728 → 1729)
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")
