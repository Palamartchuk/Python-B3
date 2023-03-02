import asyncio
import csv
import concurrent.futures
import requests


async def make_request(row):
    try:
        """ response = requests.post(
            url='http://127.0.0.1:8000/api/cadastraarquivo',
            data={
                "email": row[14].lower().strip(),
                "cpfcnpj": row[1].lower().strip(),
                "nome": row[2].lower().strip(),
                "telefone": 'Arquivo B3',
                "arquivo": f'Comprovante IRRF 202201-202212 {row[1].lower().strip()}.pdf' if len(row[1].lower().strip()) > 11 else f'Comprovante IRRF 2022 {row[1].lower().strip()}.pdf'
            },
            verify=False
        ) """
        print(f'Nome :{row[2].lower().strip()} CPF : {row[1].lower().strip()}')
        """ print(response.status_code) """
        """ print(f'Comprovante IRRF 202201-202212 {row[1].lower().strip()}.pdf') if len(row[1].lower().strip()) > 11 else print(f'Comprovante IRRF 2022 {row[1].lower().strip()}.pdf') """
    except:
        pass


async def main():
    with open('newb3.txt', encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        line_count = 0
        tasks = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for row in csv_reader:
                task = asyncio.ensure_future(
                    make_request(row)
                )
                tasks.append(task)
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                pass
            line_count += 1
    print('fim')


if __name__ == '__main__':
    asyncio.run(main())
