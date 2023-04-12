while True:
    with open("rezultati.txt", 'r') as file:
        rezultati = file.readlines()

    rezultat = input("Baci novčić i unesi rezultat: ? ") + "\n"

    # print(rezultat)
    print(len(rezultati))
    rezultati.append(rezultat)
    print(len(rezultati))

    with open("rezultati.txt", 'w') as file:
        file.writelines(rezultati)

    # print(rezultati)
    # print(len(rezultati))

    glava = rezultati.count("glava\n")
    procenat_glava = glava / len(rezultati) * 100

    pismo = rezultati.count('pismo\n')
    procenat_pismo = pismo / len(rezultati) * 100

    print(f"Glava: {procenat_glava}%")
    print(f"Pismo: {procenat_pismo}%")

