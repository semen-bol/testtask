import argparse
import asyncio
import os
import csv

from tabulate import tabulate
from typing import List
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    brand: str
    price: int
    rating: float


async def average_rating_report(csv_data):
    products = []
    try:
        for item in csv_data:
            products.append(Product(**item))
    except Exception:
        raise Exception("Invalid data in csvs")

    products = sorted(products, key=lambda x: x.rating, reverse=True)

    table_data = []; i = 1
    for product in products:
        table_data.append([i, product.brand, product.rating])
        i += 1
    headers = [' ', 'brand', 'rating']

    table = tabulate(table_data, headers=headers, tablefmt="grid")
    return table

async def read_csv_files(file_paths: List[str]) -> List:
    products = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
    return products    

async def check_file_exists(filepath):
    return bool(os.path.exists(filepath))

async def get_args():
    parser = argparse.ArgumentParser(description="Тестовое задание")

    parser.add_argument("--files", help="Указать файлы через пробел", nargs="+", required=True)
    parser.add_argument("--report", help="Тип репорта", required=True)

    return parser.parse_args()

async def main():
    args = await get_args()

    files = args.files
    report = args.report

    if files:
        for file in files:
            file_check = await check_file_exists(file)

            if file_check:
                pass
            else:
                raise FileNotFoundError(f"Файл {file} не найден")
            
    csv_data = await read_csv_files(files)

    if report == "average-rating":
        report = await average_rating_report(csv_data)
        print(report)
        return report
    
    raise Exception("Не найден тип отчета")

if __name__ == "__main__":
    asyncio.run(main())