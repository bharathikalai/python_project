#     H
#    HHH
#   HHHHH
#  HHHHHHH
# HHHHHHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#   HHHHH               HHHHH
#                     HHHHHHHHH
#                      HHHHHHH
#                       HHHHH
#                        HHH
#                         H



#   HHHHH          HHHHH


def alobolo(n):
    for i in range(1, n + 1):
        print(("H" * (2 * i - 1)).center(2 * n - 1))

    for i in range(1, n + 2):
        print(("H" * n).center(n * 2) + ("H" * n).center(n * 6,"-"))

    for i in range(1, n - 1):
        print(("H" * (n * n)).rjust(10))
    
    # for i in range(1, n + 2):
    #     print(("H" * n).center(n * 2) + ("H" * n).center(n * 6))



a = int(input("Enter a number: "))
alobolo(a)


# z = "  HHHHH               HHHHH             "
# v = "  HHHHH   ------------HHHHH-------------"

bb = "HHHHHHHHHHHHHHHHHHHHHHHHH"

print(len(bb))

# print(len(z))