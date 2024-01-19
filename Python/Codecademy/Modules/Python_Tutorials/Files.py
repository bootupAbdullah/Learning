## HOW TO READ WHOLE FILE:


# with open('how_many_lines.txt') as howmany:
#   content = howmany.read()
# print(content)

## HOW TO READ LINES OF FILE:

# with open('how_many_lines.txt') as lines_doc:
#   for line in lines_doc.readlines():
#     print(line)



with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")


