# 1. Star pattern programs - Write a C program to print the given star patterns.

# 1. Square Star Pattern
# *****
# *****
# *****
# *****
# *****

# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()

# 2. Hollow Square Star Pattern with Diagonal
# *****
# *   *
# *   *
# *   *
# *****

# for i in range (5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 3. Hollow Square Star Pattern with Diagonal
# *****
# ** **
# * * *
# ** **
# *****

# for i in range (5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4 or i == j or i + j == 4:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 4. Rhombus Star Pattern
#     *****
#    *****
#   *****
#  *****
# *****

# for i in range (5):
#     for j in range( 5 - i - 1):
#         print(" ", end="")
#     for j in range(5):
#         print("*",end= "")
#     print()

# 5. Hollow Rhombus Star Pattern
#     *****
#    *   *
#   *   *
#  *   *
# *****

# for i in range(5):
#     for j in range(5 - i - 1):
#         print(" ", end="")
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 6. Mirrored Rhombus Star Pattern
# *****
#  *****
#   *****
#    *****
#     *****

# for i in range(5):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(5):
#         print("*", end="")
#     print()

# 7. Hollow Mirrored Rhombus Star Pattern
# *****
#  *   *
#   *   *
#    *   *
#     *****

# for i in range(5):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 8. Right Triangle Star Pattern
# *
# **
# ***
# ****
# *****

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()

# 9. Hollow Right Triangle Star Pattern
# *
# **
# * *
# *  *
# *****

# for i in range(1, 6):
#     for j in range(i):
#         if j == 0 or j == i - 1 or i == 5:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 10. Mirrored Right Triangle Star Pattern
#     *
#    **
#   ***
#  ****
# *****

# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()

# 10. Mirrored Right Triangle Star Pattern
#     *
#    **
#   * *
#  *  *
# *****

# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end="")
#     for j in range(i):
#         if j == 0 or j == i - 1 or i == 5:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 12. Inverted Right Triangle Star Pattern
# *****
# ****
# ***
# **
# *

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

# 13. Hollow Inverted Right Triangle Star Pattern
# *****
# *  *
# * *
# **
# *

# for i in range(5, 0, -1):
#     for j in range(i):
#         if j == 0 or j == i - 1 or i == 5:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 14. Inverted Right Triangle Star Pattern
# *****
#  ****
#   ***
#    **
#     *

# for i in range(5):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(5 - i):
#         print("*", end="")
#     print()

# 15. Hollow Inverted Right Triangle Star Pattern
# *****
#  ****
#   ***
#    **
#     *

# for i in range(5):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(5 - i):
#         if j == 0 or j == 5 - i - 1 or i == 0:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 16. Pyramid Star Pattern
#     *
#    ***
#   *****
#  *******
# *********

# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

# 17. Pyramid Star Pattern
#     *
#    * *
#   *   *
#  *     *
# *********

# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2 or i == 5:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 18. Inverted Pyramid Star Pattern
# *********
#  *******
#   *****
#    ***
#     *

# for i in range(5, 0, -1):
#     for j in range(5 - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

# 19.Hollowed Inverted Pyramid Star Pattern
# *********
#  *     *
#   *   *
#    * *
#     *

# for i in range(5, 0, -1):
#     for j in range(5 - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2 or i == 5:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 20. Half Diamond Star Pattern
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# n = 5

# for i in range(1, n + 1):
#     print("*" * i)

# for i in range(n - 1, 0, -1):
#     print("*" * i)

# 21. Mirrored Half Diamond Star Pattern
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * i)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * i)

# 22. Diamond Star Pattern
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# 23. Hollow Diamond Star Pattern
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

# n = 5

# for i in range(n, 0, -1):
#     if i == n:
#         print("*" * (2 * i))
#     else:
#         print("*" * i + " " * (2 * (n - i)) + "*" * i)

# for i in range(1, n + 1):
#     if i == n:
#         print("*" * (2 * i))
#     else:
#         print("*" * i + " " * (2 * (n - i)) + "*" * i)

# 24. Right Arrow Star Pattern
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****

# n = 5

# for i in range(n, 0, -1):
#     print("*" * i)

# for i in range(2, n + 1):
#     print("*" * i)

# 25. Left Arrow Star Pattern
# *****
#  ****
#   ***
#    **
#     *
#    **
#   ***
#  ****
# *****

# n = 5

# for i in range(n, 0, -1):
#     print(" " * (n - i) + "*" * i)

# for i in range(2, n + 1):
#     print(" " * (n - i) + "*" * i)

# 26. Plus Star Pattern
#     +
#     +
#     +
#     +
# +++++++++
#     +
#     +
#     +
#     +

# n = 10

# for i in range(n):
#     if i == n // 2:
#         print("+" * (2 * n - 1))
#     else:
#         print(" " * (n - 1) + "+")

# 27. X Star Pattern
# *       *
#  *     *
#   *   *
#    * *
#     *
#    * *
#   *   *
#  *     *
# *       *

# n = 11

# for i in range(n):
#     for j in range(n):
#         if j == i or j == n - 1 - i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
