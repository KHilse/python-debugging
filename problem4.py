wealth = 1000000000

print('{:,}'.format(wealth))

# str_output = ""
# while wealth > 0:
#     if wealth >= 1000:
#         str_output += ",{:03d}".format(wealth % 1000)
#         wealth = wealth // 1000
#     else:
#         str_output = str(wealth) + str_output
#         wealth = 0
# print(str_output)