# TextFile = open('./file.txt')
# print(TextFile.read())
# TextFile.seek(0)
# print(TextFile.read())
#
# TextFile.seek(0)
# textLines = TextFile.readlines()
# print(textLines)
# TextFile.close()

# with open('./file.txt') as File:
#     print(File.read())

# with open('./file.txt', mode='w') as File:
#     File.write('this is edited text')

with open('./file.txt', mode='a') as File:
    File.write('\nthis is end of line')
