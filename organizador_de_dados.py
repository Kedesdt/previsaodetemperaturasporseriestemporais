import csv, time

with open('dados_A701_H_2006-07-24_2023-03-22.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=";")

    nomes = []

    dia_anterior = None
    mes_anterior = None
    ano_anterior = None
    index = 0
    for row in spamreader:
        index += 1
        if index > 9:
            break
    for row in spamreader:
        nomes = row
        break

    horas = {}
    dias = {}
    meses = {}
    anos = {}

    somas_dia = {}
    somas_mes = {}
    somas_ano = {}

    medias_dia = {}
    medias_mes = {}
    medias_ano = {}

    for row in spamreader:
        if not len(row):
            continue
        for i in range(2, len(nomes)):
            if row[i] is not None:
                if not dia_anterior:
                    dia_anterior = row[0]
                if not mes_anterior:
                    mes_anterior = time.strftime('%Y-%m', time.strptime(row[0], '%Y-%m-%d'))
                if not ano_anterior:
                    ano_anterior = time.strftime('%Y', time.strptime(row[0], '%Y-%m-%d'))

                dia = row[0]
                mes = time.strftime('%Y-%m', time.strptime(row[0], '%Y-%m-%d'))
                ano = time.strftime('%Y', time.strptime(row[0], '%Y-%m-%d'))

                if dia == dia_anterior:

                    if not nomes[i] in horas:
                        horas[nomes[i]] = 1

                    if not dia in somas_dia:
                        somas_dia[dia] = {}

                    if not nomes[i] in somas_dia[dia]:
                        somas_dia[dia][nomes[i]] = 0

                    if not row[i] == "null" and not row[i] == '':
                        somas_dia[dia][nomes[i]] += float(row[i])
                        horas[nomes[i]] += 1

                else:
                    if not dia_anterior in medias_dia:
                        medias_dia[dia_anterior] = {"Dia": dia_anterior}
                    if horas[nomes[i]]:
                        medias_dia[dia_anterior][nomes[i]] = "%.2f" %(somas_dia[dia_anterior][nomes[i]] / horas[nomes[i]])
                    else:
                        medias_dia[dia_anterior][nomes[i]] = 0
                    horas[nomes[i]] = 1

                    if mes == mes_anterior:

                        if not mes in somas_mes:
                            somas_mes[mes] = {}

                        if not nomes[i] in somas_mes[mes]:
                            somas_mes[mes][nomes[i]] = 0
                            dias[nomes[i]] = 1

                        somas_mes[mes][nomes[i]] += float(medias_dia[dia_anterior][nomes[i]])
                        dias[nomes[i]] += 1

                    else:

                        if not mes_anterior in medias_mes:
                            medias_mes[mes_anterior] = {"Mes" : mes_anterior}
                        if dias[nomes[i]]:
                            medias_mes[mes_anterior][nomes[i]] = "%.2f" %(somas_mes[mes_anterior][nomes[i]] / dias[nomes[i]])
                        else:
                            medias_mes[mes_anterior][nomes[i]] = 0
                        dias[nomes[i]] = 1

                        if ano == ano_anterior:

                            if not ano in somas_ano:
                                somas_ano[ano] = {}

                            if not nomes[i] in somas_ano[ano]:
                                somas_ano[ano][nomes[i]] = 0
                                meses[nomes[i]] = 1

                            somas_ano[ano][nomes[i]] += float(medias_mes[mes_anterior][nomes[i]])
                            meses[nomes[i]] += 1

                        else:

                            if not ano_anterior in medias_ano:
                                medias_ano[ano_anterior] = {"Ano": ano_anterior}
                            if meses[nomes[i]]:
                                medias_ano[ano_anterior][nomes[i]] = "%.2f" %(somas_ano[ano_anterior][nomes[i]] / meses[nomes[i]])
                            else:
                                medias_ano[ano_anterior][nomes[i]] = 0
                            meses[nomes[i]] = 1

                            if i + 1 >= len(row):
                                ano_anterior = ano
                        if i + 1 >= len(row):
                            mes_anterior = mes
                    if i + 1 >= len(row):
                        dia_anterior = dia

    with open('medias_diarias.csv', 'w', newline='') as csvfile:

        fieldnames = [i[0] for i in medias_dia[list(medias_dia.items())[0][0]].items()]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for dia in medias_dia:
            try:
                writer.writerow(medias_dia[dia])
            except Exception as e:
                print(e)

    with open('medias_mensais.csv', 'w', newline='') as csvfile:

        fieldnames = [i[0] for i in medias_mes[list(medias_mes.items())[0][0]].items()]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for mes in medias_mes:
            try:
                writer.writerow(medias_mes[mes])
            except Exception as e:
                print(e)

    with open('medias_anuais.csv', 'w', newline='') as csvfile:

        fieldnames = [i[0] for i in medias_ano[list(medias_ano.items())[0][0]].items()]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for ano in medias_ano:
            try:
                writer.writerow(medias_ano[ano])
            except Exception as e:
                print(e)

    print(medias_dia)
    print(medias_mes)
    print(medias_ano)

