import openpyxl
import asyncio
from pydirectus import DirectusClient

FILE_PATH = "/home/d-cuzya/Рабочий стол/exel-script/schem.xlsx" 
DIRECTUS = DirectusClient(
    hostname="https://admin.dcuzya.ru",
    static_token="MjuNGAhDVXJTDHRF70u3q2iPbgH1ZanC",
)

async def upload_on_directus(row):
    new_item_data = {
        "name": row[0], 
        "age": int(row[1]),
        "city": row[2]
    }
    response = DIRECTUS.create_item("datamodelexample", data=new_item_data)
    print(response)
    
async def read_excel_file(file_path):
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        rows = list(sheet.iter_rows(values_only=True))
        
        for row in rows[1:]:
            if row[0]:
                await upload_on_directus(row)
        
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

async def main():
    await read_excel_file(FILE_PATH)

if __name__ == "__main__": 
    asyncio.run(main())