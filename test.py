import pytest
import asyncio

from main import read_csv_files, average_rating_report

csv_files = ['products1.csv', 'products2.csv']
report = "average-rating"

class TestReportGenerator:
    @pytest.mark.asyncio
    async def test_csv_read(self):
        csv_data = await read_csv_files(csv_files)
        
        assert len(csv_data) > 0
        print(csv_data)

    @pytest.mark.asyncio
    async def test_generate_report(self):
        csv_data = await read_csv_files(csv_files)
        tab = await average_rating_report(csv_data)

        assert 'brand' in tab
        assert 'rating' in tab
        print(tab)
