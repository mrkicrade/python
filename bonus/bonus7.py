filenames = ['1.doc', '1.report', '1.presentation']

res = ['1-doc.txt', '1-report.txt', '1-presentation.txt']

# result = []
#
# for filename in filenames:
#     filename = filename.replace('.', '-', 1)
#     filename = filename + '.txt'
#     result.append(filename)
#
# print(result)

filenames = [filename.replace('.', '-', 1) + '.txt' for filename in filenames]

print(filenames)
