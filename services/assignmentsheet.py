from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

class Assignments():
    def __init__(self, creds_path, sheetid):
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        self.credentials = Credentials.from_service_account_file(
                        creds_path,
                        scopes = SCOPES
                        )
        self.sheetid = sheetid    
        self.service = build("sheets", "v4", credentials = self.credentials)

    def add(self):    
        values = [["Hello from REGULUS", "Test entry"]]

        body = {
            "values": values
        }

        # Append to Sheet1
        self.service.spreadsheets().values().append(
            spreadsheetId = self.sheetid,
            range = "Sheet1!B1",
            valueInputOption = "USER_ENTERED",
            body = body
        ).execute()