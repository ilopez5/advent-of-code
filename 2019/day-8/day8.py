def verify_image(file):
    with open(file, 'r') as fd:
        image = fd.read()
    
    min_zeros = width = 25*6
    image = [image[i: i+width] for i in range(0, len(image), width)][:-1]

    for layer, pixel in enumerate(image):
        count = pixel.count('0')
        if count < min_zeros:
            min_zeros = count
            target = layer
    return image[target].count('1') * image[target].count('2')


def draw(file):
    with open(file, 'r') as fd:
        image = fd.read()

    width, height = 25, 6
    image = [image[i: i+width] for i in range(0, len(image), width)][:-1]
    
    output = []
    for row in range(6):
        result = []
        for col in range(width):
            pixel = 2
            for layer in range(0, len(image), 6):
                current = int(image[row+layer][col])
                if current != pixel:
                    pixel = current
                    break
            result.append(str(pixel))
        output.append("".join(result))

    for row in output:
        print(row)
    return

if __name__ == "__main__":
    solution = verify_image('day8input.txt')
    print("Solution is:", solution)
    draw('day8input.txt')