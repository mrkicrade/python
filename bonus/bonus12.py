feet_inches = input('Enter feet and inches: ')


def convert(feet_inched):
    parts = feet_inched.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3408 + inches * 0.0254
    return meters


result = convert(feet_inches)

if result < 1:
    print('Kid is too small.')
else:
    print('Kid can use the slide.')



