import csv
import requests
from requests.models import Response
with open('newb3.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader)
    line_count = 0
    teste = 0;
    for row in csv_reader:
            try:
                response = requests.post(
                    url = 'http://127.0.0.1:8000/api/cadastraarquivo', 
                    data={
                        "email": row[14].lower().strip(),
                        "cpfcnpj": row[1].lower().strip(),
                        "nome": row[2].lower().strip(),
                        "telefone": 'Arquivo B3',
                        "arquivo": f'Comprovante IRRF 202201-202212 {row[1].lower().strip()}.pdf' if len(row[1].lower().strip()) > 11 else f'Comprovante IRRF 2022 {row[1].lower().strip()}.pdf'
                    },
                    verify=False
                )
                print(f'Nome :{row[2].lower().strip()} CPF : {row[1].lower().strip()}')
                print(response.status_code)
            except:
                pass
            line_count += 1
    print('fim')