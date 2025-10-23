import pytest
import asyncio

from main import read_csv_files, average_rating_report, check_file_exists

csv_files = ['products1.csv', 'products2.csv']
report = "average-rating"

class TestReportGenerator:
    @pytest.mark.asyncio
    async def test_csv_read(self):
        for file in csv_files:
            file_check = await check_file_exists(file)

            if file_check:
                pass
            else:
                raise FileNotFoundError(f"Файл {file} не найден")
        csv_data = await read_csv_files(csv_files)
        
        assert len(csv_data) > 0
        print(csv_data)

    @pytest.mark.asyncio
    async def test_generate_report(self):
        for file in csv_files:
            file_check = await check_file_exists(file)

            if file_check:
                pass
            else:
                raise FileNotFoundError(f"Файл {file} не найден")

        csv_data = await read_csv_files(csv_files)
        tab = await average_rating_report(csv_data)

        assert 'brand' in tab
        assert 'rating' in tab
        print(tab)
