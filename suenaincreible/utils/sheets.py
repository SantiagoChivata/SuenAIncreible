import gspread

def get_dreams(sheet_name="Sueños"):
    """Obtiene sueños desde Google Sheets."""
    gc = gspread.service_account(filename="credentials.json")
    sheet = gc.open(sheet_name).sheet1
    return sheet.col_values(1)
