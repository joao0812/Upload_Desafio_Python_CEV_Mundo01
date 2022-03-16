import math

compri_reta01 = float(input('Digite o valor da reta: '))
compri_reta02 = float(input('Digite o valor da proxima reta: '))
compri_reta03 = float(input('Digite o valor da última reta: '))

if compri_reta01 < (compri_reta02 + compri_reta03) and compri_reta01 > math.fabs(compri_reta02 - compri_reta03):
    if compri_reta02 < (compri_reta01 + compri_reta03) and compri_reta02 > math.fabs(compri_reta01 - compri_reta03):
        if compri_reta03 < (compri_reta02 + compri_reta01) and compri_reta03 > math.fabs(compri_reta02 - compri_reta01):
            print('-' * 47)
            print('| APROVADO! Triângulo possíve de ser feito |')
            print('-' * 47)
else:
    print('_' * 48)
    print('| REJEITADO! Triângulo impossível de ser feito |')
    print('-' * 48)