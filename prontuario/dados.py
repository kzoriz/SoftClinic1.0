import random


def raca_random():
    raca_list = [
        'PARDO',
        'BRANCO',
        'INDIGENA',
        'AMARELO'
    ]
    var = random.randint(0, 100)

    if var <= 10:
        return 'N.D.N'
    else:
        var2 = random.randint(0, len(raca_list) - 1)
        return raca_list[var2]


def estado_civil_random():
    estado_civil_list = [
        'SOLTEIRO(A)',
        'CASADO(A)',
        'VIÚVO(A)',
        'SEPARADO(A)',
        'DIVORCIADO(A)'
    ]
    var = random.randint(0, 100)

    if var <= 10:
        return 'N.D.N'
    else:
        var2 = random.randint(0, len(estado_civil_list) - 1)
        return estado_civil_list[var2]


def grau_instruncao_random():
    grau_instruncao_list = [
        'ANALFABETO',
        'FUNDAMENTAL INCOMPLETO',
        'FUNDAMENTAL COMPLETO',
        'MÉDIO INCOMPLETO',
        'MEDIO COMPLETO',
        'SUPERIOR INCOMPLETO',
        'SUPERIOR COMPLETO',
        'MESTRADO',
        'DOUTORADO'
    ]
    var = random.randint(0, 100)

    if var <= 10:
        return 'N.D.N'
    else:
        var2 = random.randint(0, len(grau_instruncao_list) - 1)
        return grau_instruncao_list[var2]


def anamnese_random():
    anamnese_list = [
        'Paciente procurou as clínicas da UERN alegando sentir dores nos dentes ao ter '
        'contato com qualquer substância gelada O paciente é operador de máquinas residente'
        ' da cidade de Cruzeta',

        'Paciente chegou as clinicas da UERN encaminhado da UBS com '
        'indicação de biopsia por lesão em lábio inferior. A paciente é '
        'trabalhadora rural no município de Jardim de Piranhas.',

        'Paciente dirigiu-se a clínica da UERN para uma consulta de rotina. A'
        ' paciente é comerciante na cidade de Caicó.',

        'Paciente foi a clínica da UERN após sentir ardência no vestibulo da '
        'boca. O paciente é estudante e reside na zona rural de Jardim do Seridó.',

        'Paciente deslocou-se para a clínica da UERN após fraturar ambos os '
        'dentes incisivos centrais superiores após ser vitima de agressão '
        'física. O paciente é mototaxista da cidade de Caicó.',

        'Paciente visitou a clínica da UERN para uma avaliação da saúde '
        'oral. O paciente é estudante da cidade de Caicó.',

        'A paciente foi encaminhado para a Clínica da UERN pelo médico que '
        'a acompanha. A paciente é autônoma da cidade de Ouro Branco.',

        'Paciente procurou a clínica de odontologia da UERN após notar o '
        'surgimento de uma lesão em seu lábio inferior. A paciente é do lar '
        'da cidade de São João do Sabugi.',

        'Paciente procurou a clínica de odontologia da UERN para uma '
        'consulta de rotina. O paciente é estudante da cidade de Caicó.',

        'Paciente procurou a clínica de odontologia da UERN após sentir um '
        'gosto metálico em sua boca. O paciente é gari da cidade de Caicó.'

    ]
    var = random.randint(0, 100)

    if var <= 20:
        return 'N.D.N'
    else:
        var2 = random.randint(0, 9)
        return anamnese_list[var2]


print('ANAMNESE: ', anamnese_random())


def antecedentes_familiares_random():
    lista = []
    dados = ''
    antecedentes_familiares_list = [
        'Glaucoma (avô paterno)',
        'Parada cardíaca (Pai)',
        'AVC (avó materna)',
        'Diabetes (avó paterna e materna)',
        'hipertensão (pai)',
        'Infarto (avô paterno)',
        'diabetes (mãe)',
        'diabetes (pai e avós paternos)',
        'Câncer de boca (avô paterno)',
        'Doença de Huntington (avó materna)'
    ]
    var = random.randint(0, 100)
    if var <= 50:
        return 'N.D.N'
    else:
        var2 = random.randint(1, 3)
        for i in range(var2):
            lista.append(antecedentes_familiares_list[random.randint(0, len(antecedentes_familiares_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('ANTECEDENTES FAMILIARES: ', antecedentes_familiares_random())


def medicamentos_random():
    lista = []
    dados = ''
    medicamentos_em_uso_list = [
        'Insulina Detemir',
        'Prednisona',
        'Crizanlizumabe',
        'ciclosporina',
        'azatriopina',
        'metotrexato',
        'Butalab',
        'losartana',
        'Fluoxetina',
        'Benzetacil',
        'hidroxiureia',
        'clofibrato',
        'Alprazolam',
        'Sofosbuvir',
        'Acetaminofeno',
        'Bactrim',
        'Tacrolimus',
        'Nistatina'
    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 3)
        for i in range(var2):
            lista.append(medicamentos_em_uso_list[random.randint(0, len(medicamentos_em_uso_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('MEDICAMENTOS EM USO: ', medicamentos_random())


def cirurgia_random():
    lista = []
    dados = ''
    cirurgias_anteriores_list = [

        'Septoplastia (há 3 anos)',
        'Cesaria',
        'histerectomia',
        'Curetagem',
        'Remoção das amígdalas',
        'Apendicite (Há 4 anos)',
        'colecistectomia (há 9 meses)',
        'fimose (há 2 anos)',
        'Transplante do fígado (há 2 anos)'

    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 3)
        for i in range(var2):
            lista.append(cirurgias_anteriores_list[random.randint(0, len(cirurgias_anteriores_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('CIRURGIAS ANTERIORES: ', cirurgia_random())


def cardiaco_random():
    lista = []
    dados = ''
    problemas_cardiacos_list = [
        'Insuficiência mitral',
        'Doença coronariana',
        'Doença cerebrovascular',
        'Doença arterial periférica',
        'Cardiopatia congênita',
        'Doença cardíaca reumática'

    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 2)
        for i in range(var2):
            lista.append(problemas_cardiacos_list[random.randint(0, len(problemas_cardiacos_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('PROBLEMAS CARDIACOS: ', cardiaco_random())


def gastrointestinais_random():
    lista = []
    dados = ''
    problemas_gastroinstestinais_list = [
        'Refluxo',
        'Gastrite',
        'Doença de Crohn',
        'Refluxo gastroesofágico'
    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 3)
        for i in range(var2):
            lista.append(
                problemas_gastroinstestinais_list[random.randint(0, len(problemas_gastroinstestinais_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('PROBLEMAS GASTROINTESTINAIS: ', gastrointestinais_random())


def alteracoes_sangineas():
    lista = []
    dados = ''
    alteracoes_sanguineas_list = [
        'Anemia falciforme',
        'Leucemia'
    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 2)
        for i in range(var2):
            lista.append(alteracoes_sanguineas_list[random.randint(0, len(alteracoes_sanguineas_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('ALTERAÇÕES SANGUINEAS: ', alteracoes_sangineas())


def enfermidades_osseas_random():
    lista = []
    dados = ''
    enfermidades_osseas_list = [
        'Doença de Paget',
        'Reumatismo',
        'Febre reumática',
        'Osteoporose',
    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 2)
        for i in range(var2):
            lista.append(enfermidades_osseas_list[random.randint(0, len(enfermidades_osseas_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('ENFERMIDADES ÓSSEAS: ', enfermidades_osseas_random())


def problemas_pulmonares_random():
    lista = []
    dados = ''
    problemas_pulmonares_list = [
        'Sinusite',
        'Rinite crônica',
        'Asma',
        'Enfisema pulmonar',
        'Rinite',
        'Tuberculose'
    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 3)
        for i in range(var2):
            lista.append(problemas_pulmonares_list[random.randint(0, len(problemas_pulmonares_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('PROBLEMAS PULMONARES: ', problemas_pulmonares_random())


def alegias_random():
    lista = []
    dados = ''
    alergias_list = [
        'Amoxicilina',
        'Abacaxi',
        'Metal',
        'Látex',
        'Lidocaína',
        'Paracetamol',
        'Algodão',
        'Pelo de gato',
        'proteína do leite',
        'AAS',
        'Amido',
        'Camarão',
        'cafeína'

    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 4)
        for i in range(var2):
            lista.append(alergias_list[random.randint(0, len(alergias_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('ALERGIAS: ', alegias_random())


def habitos_random():
    lista = []
    dados = ''
    habitos_list = [
        'Apertamento',
        'Bruxismo',
        'Respirador bucal',
        'Onicofagia'

    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 4)
        for i in range(var2):
            lista.append(habitos_list[random.randint(0, len(habitos_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('HÁBITOS: ', habitos_random())


def diabetes_random():
    diabetes_list = [
        'Mellitus Tipo 1',
        'Mellitus Tipo 2',
        'Insipidus Nefrogênico',
        'Insipidus Gestacional',
        'Insipidus Neurogênico'
    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(diabetes_list) - 1)
        dados = diabetes_list[var2]
        return dados


print('DIABETES: ', diabetes_random())


def hipertencao_random():
    hipertensao_list = [
        'Normal',
        'Normal limítrofe',
        'Hipertensão leve(estágio 1)',
        'Hipertensão moderada(estágio 2)',
        'Hipertensão grave(estágio 3)',
    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(hipertensao_list) - 1)
        dados = hipertensao_list[var2]
        return dados


print('HIPERTENSÃO: ', hipertencao_random())


def epilepsia_random():
    epilepsia_list = [
        'Crise focal Simples',
        'Crise focal Complexa',
        'Crise generalizada de Ausência',
        'Crise generalizada  Atônica',
        'Crise generalizada Tônica',
        'Crise generalizada Clônica',
        'Crise generalizada Tônico-Clônica',
    ]

    var = random.randint(0, 100)
    if var <= 80:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(epilepsia_list) - 1)
        dados = epilepsia_list[var2]
        return dados


print('EPILEPSIA: ', epilepsia_random())


def doenca_mental_random():
    lista = []
    dados = ''
    doenca_mental_list = [
        'Ansiedade',
        'Autismo',
        'Depressão',
        'Síndrome do pânico',
        'Transtorno obsessivo-compulsivo'
    ]
    var = random.randint(0, 100)
    if var <= 70:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 4)
        for i in range(var2):
            lista.append(doenca_mental_list[random.randint(0, len(doenca_mental_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('DOENÇA MENTAL: ', doenca_mental_random())


def hepatite_random():
    hepatite_list = [
        'A',
        'B',
        'C',
        'D',
        'E'
    ]
    var = random.randint(0, 100)
    if var <= 80:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(hepatite_list) - 1)
        dados = hepatite_list[var2]
        return dados


print('HEPATITE: ', hepatite_random())


def hiv_random():
    hiv_list = [
        'Sim'
    ]
    var = random.randint(0, 100)
    if var <= 90:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(hiv_list) - 1)
        dados = hiv_list[var2]
        return dados


print('HIV: ', hiv_random())


def herpes_random():
    herpes_list = [
        'Tipo 1',
        'Tipo 2',
        'Tipo 3',
    ]
    var = random.randint(0, 100)
    if var <= 80:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(herpes_list) - 1)
        dados = herpes_list[var2]
        return dados


print('HERPES: ', herpes_random())


def sangra_excesso_random():
    sangra_list = [
        'Sim'
    ]
    var = random.randint(0, 100)
    if var <= 80:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(sangra_list) - 1)
        dados = sangra_list[var2]
        return dados


print('SANGRA EM EXCESSO: ', sangra_excesso_random())


def gravida_random():
    gravida_list = [
        'Sim',
    ]
    var = random.randint(0, 100)
    if var <= 80:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(gravida_list) - 1)
        dados = gravida_list[var2]
        return dados


print('GRAVIDA: ', gravida_random())


def problemas_renais_random():
    lista = []
    dados = ''

    problemas_renais_list = [

        'Cálculos renais',
        'Nefrite crônica',
        'insuficiência renal',

    ]
    var = random.randint(0, 100)
    if var <= 80:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 3)
        for i in range(var2):
            lista.append(problemas_renais_list[random.randint(0, len(problemas_renais_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('PROBLEMAS RENAIS: ', problemas_renais_random())


def radioterapia_random():
    radioterapia_list = [
        'Sim'
    ]
    var = random.randint(0, 100)
    if var <= 90:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(radioterapia_list) - 1)
        dados = radioterapia_list[var2]
        return dados


print('RADIOTERAPIA: ', radioterapia_random())


def quimioterapia_random():
    quimioterapia_list = [
        'Sim'
    ]
    var = random.randint(0, 100)
    if var <= 90:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(quimioterapia_list) - 1)
        dados = quimioterapia_list[var2]
        return dados


print('QUIMIOTERAPIA: ', quimioterapia_random())


def protese_random():
    lista = []
    dados = ''
    proteses_list = [
        'Prótese dentária inferior',
        'Prótese dentária superior'
    ]
    var = random.randint(0, 100)
    if var <= 80:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(1, 2)
        for i in range(var2):
            lista.append(proteses_list[random.randint(0, len(proteses_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('ARTICULAÇÕES OU PROTÉSE: ', protese_random())


def fuma_random():
    fuma_list = [
        'Diariamente',
        'Socialmente',
        'Semanalmente'
    ]
    var = random.randint(0, 100)
    if var <= 80:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(fuma_list) - 1)
        dados = fuma_list[var2]
        return dados


print('FUMA / MASTIGA TABACO OU RAPÉ: ', fuma_random())


def bebida_random():
    bebida_list = [
        'Diariamente',
        'Socialmente',
        'Semanalmente'
    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Não'
    else:
        var2 = random.randint(0, len(bebida_list) - 1)
        dados = bebida_list[var2]
        return dados


print('BEBIDA: ', bebida_random())


def nodulos_linfaticos_random():
    nodulos_linfaticos_list = [
        'Não Palpavéis',
        'Inchados',

    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Normal'
    else:
        var2 = random.randint(0, len(nodulos_linfaticos_list) - 1)
        dados = nodulos_linfaticos_list[var2]
        return dados


print('NODULOS LINFATICOS: ', nodulos_linfaticos_random())


def amigdalas_random():
    lista = []
    dados = ''
    amigdalas_list = [
        'Hipertrofica',
    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 2)
        if var2 == 0:
            return 'N.D.N'
        elif var2 == 1:
            return 'Normal'
        else:
            return 'Ausente'
    else:
        var2 = random.randint(1, 2)
        for i in range(var2):
            lista.append(amigdalas_list[random.randint(0, len(amigdalas_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('AMIGDALAS: ', amigdalas_random())


def trigono_retromolar_random():
    lista = []
    dados = ''

    trigono_retromolar_list = [
        'Ulcerações',
        'Presença de eritroplasias',
        'Presença de úlceras',

    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'N.D.N'
        else:
            return 'Normal'
    else:
        var2 = random.randint(1, 2)
        for i in range(var2):
            lista.append(trigono_retromolar_list[random.randint(0, len(trigono_retromolar_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('TRIGONO RETROMOLAR: ', trigono_retromolar_random())


def palato_duro_random():
    lista = []
    dados = ''

    palato_duro_list = [
        'Tórus',
        'Tórus na rafe',
        'Candidíase',
        'Presença de áreas nodulares',
        'Presença de pústulas',
    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'Normal'
        else:
            return 'N.D.N'
    else:
        var2 = random.randint(1, 3)
        for i in range(var2):
            lista.append(palato_duro_list[random.randint(0, len(palato_duro_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('PALATO DURO: ', palato_duro_random())


def palato_mole_random():
    lista = []
    dados = ''
    palato_mole_list = [
        'Úvula bífida',
        'Presença de pigmentos amarelados',
        'candidíase',
        'herpangina',
        'Presença de petéquias',
        'Presença de abcesso',
        'abscesso peritonsilar',
    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'Normal'
        else:
            return 'N.D.N'
    else:
        var2 = random.randint(1, 3)
        for i in range(var2):
            lista.append(palato_mole_list[random.randint(0, len(palato_mole_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('PALATO MOLE: ', palato_mole_random())


def labios_random():
    lista = []
    dados = ''
    labios_list = [
        'Ressecados',
        'Lesão arredondada',
        'Mucocele',
        'Mucosite',
        'Bolhas no lábio superior',
        'Bolhas no lábio inferior',
        'Mácula no lábio inferior',
        'Mácula no lábio superior',
        'Queilite actínica no lábio inferior',
        'Queilite actínica no lábio superior',

    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'Normal'
        else:
            return 'N.D.N'
    else:
        var2 = random.randint(1, 3)
        for i in range(var2):
            lista.append(labios_list[random.randint(0, len(labios_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print("LABIOS: ", labios_random())


def pele_random():
    lista = []
    dados = ''
    pele_list = [
        'Brozeada',
        'Presença de pápula vermelha',
    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'Normal'
        else:
            return 'N.D.N'
    else:
        var2 = random.randint(1, 2)
        for i in range(var2):
            lista.append(pele_list[random.randint(0, len(pele_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('PELE: ', pele_random())


def atm_random():
    lista = []
    dados = ''
    atm_list = [
        'Estalido (direito)',
        'Estalidos',
        'Dor',
        'Apertamento',
        'Dor ao acordar'
    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'Normal'
        else:
            return 'N.D.N'
    else:
        var2 = random.randint(1, 2)
        for i in range(var2):
            lista.append(atm_list[random.randint(0, len(atm_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('ATM: ', atm_random())


def vestibulo_random():
    lista = []
    dados = ''
    vestibulo_list = [
        'Morsicatio',
        'Hiperplasia fibrosa inflamatoria',
        'Presença de placas esbranquiçadas difusas',
        'Presença de petéquias e úlceras',
        'Nevo',
        'aftas'
    ]
    var = random.randint(0, 100)
    if var <= 50:
        var2 = random.randint(0, 1)
        if var2 == 0:
            return 'Normal'
        else:
            return 'N.D.N'
    else:
        var2 = random.randint(1, 4)
        for i in range(var2):
            lista.append(vestibulo_list[random.randint(0, len(vestibulo_list) - 1)])
        lista_set = list(set(lista))
        for i in range(len(lista_set)):
            if i == len(lista_set) - 1:
                dados += f'{lista_set[i]}.'
            else:
                dados += f'{lista_set[i]}, '

        return dados


print('VESTIBULO: ', vestibulo_random())


def higiene_bucal_random():
    higiene_bucal_list = [
        'Razoável',
        'Ruim',
        'Boa',
        'Excelente',

    ]
    var = random.randint(0, 100)
    if var <= 40:
        return 'N.D.N'

    else:
        var2 = random.randint(0, len(higiene_bucal_list) - 1)
        dados = higiene_bucal_list[var2]
        return dados


print('HIGIENE BUCAL: ', higiene_bucal_random())

# for i in range(1, 10001):
#     print('PACIENTE: ', i)
#     print('-----------------------------------------------------------------------------------------------------------')
#     print()
#     print('ANAMNESE: ', anamnese_random())
#     print('ANTECEDENTES FAMILIARES: ', antecedentes_familiares_random())
#     print('MEDICAMENTOS EM USO: ', medicamentos_random())
#     print('CIRURGIAS ANTERIORES: ', cirurgia_random())
#     print('PROBLEMAS CARDIACOS: ', cardiaco_random())
#     print('PROBLEMAS GASTROINTESTINAIS: ', gastrointestinais_random())
#     print('ARTICULAÇÕES OU PROTÉSE: ', protese_random())
#     print()
#     print('-----------------------------------------------------------------------------------------------------------')
