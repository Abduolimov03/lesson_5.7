### Multiplication table for number
# def multi_table(number):
#     result = ''
#     for i in range(1, 11):
#         result += f"{i} * {number} = {i * number}"
#         if i != 10:
#             result += '\n'
#     return result

### Who is going to pay for the wall?
# def who_is_paying(name):
#     if len(name) <= 2:
#         return [name]
#     else:
#         return [name, name[:2]]

### Name Shuffler
# def name_shuffler(str_):
#     parts = str_.split()
#     swapped = [parts[1], parts[0]]
#     return ' '.join(swapped)

### Contamination
# def contamination(text, char):
#     if not text or not char:
#         return ""
#     return char * len(text)

### Remove String Spaces
# def no_space(x):
#     return x.replace(" ", "")

### Dollars and Cents
# def format_money(amount):
#     return f"${amount:.2f}"

### Name on billboard
# def billboard(name, price=30):
#     total = 0
#     for _ in name:
#         total += price
#     return total

### Is the string uppercase?
# def is_uppercase(inp):
#     return inp == inp.upper()

### UEFA EURO 2016
# def uefa_euro_2016(teams, scores):
#     if scores[0] > scores[1]:
#         return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
#     elif scores[1] > scores[0]:
#         return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
#     else:
#         return f"At match {teams[0]} - {teams[1]}, teams played draw."

###A Strange Trip to the Market
def is_loch_ness_monster(string):
    triggers = ["tree fiddy", "three fifty", "3.50"]
    for phrase in triggers:
        if phrase in string.lower():
            return True
    return False