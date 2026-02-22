from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from services.time import Time

class Attendance():
    def __init__(self, creds_path, sheetid):
        # instantiate classes and sheet API

        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        self.credentials = Credentials.from_service_account_file(
                        creds_path,
                        scopes = SCOPES
                        )
        self.sheetid = sheetid    
        self.service = build("sheets", "v4", credentials = self.credentials)
        self.time = Time()
        self.subject = self.all_subjects()
        self.day = self.time.day()
        self.date = self.time.date()

    def all_subjects(self):
        # return list of all class days and classes

        return {"Tuesday": ["ICT", "Calculus"],
                "Wednesday": ["Physics"],
                "Thursday": ["Islamiat", "PF", "English"],
                "Friday": ["PF"]}

    def mark_present(self): 
        value = [["P"]]     # P for Present
        if self.day in self.all_subjects(): # check if today is a class day

            # loop over each subject in the day
            for subject in self.subject.get(self.day):

                # get all dates and row numbers in the sheet
                response = self.service.spreadsheets().values().get(
                    spreadsheetId = self.sheetid,
                    range = f"{subject}!A:A"
                ).execute()

                date_column = response.get("values", [])
                rows_with_values = [(i + 1, row[0]) for i, row in enumerate(date_column) if row]
                row = next((row for row, value in rows_with_values if value == self.date), None)

                # only update if the date exists in sheet
                if row:
                    self.service.spreadsheets().values().update(
                    spreadsheetId = self.sheetid,
                    range = f"{subject}!B{row}",
                    valueInputOption = "USER_ENTERED",
                    body = {"values": value}
                    ).execute()

        else:
            print("you do not have a class today dumbass")

    def mark_absent(self): 
        value = [["A"]]     # A for Absent
        if self.day in self.all_subjects(): # check if today is a class day

            # loop over each subject in the day
            for subject in self.subject.get(self.day):

                # get all dates and row numbers in the sheet
                response = self.service.spreadsheets().values().get(
                    spreadsheetId = self.sheetid,
                    range = f"{subject}!A:A"
                ).execute()

                date_column = response.get("values", [])
                rows_with_values = [(i + 1, row[0]) for i, row in enumerate(date_column) if row]
                row = next((row for row, value in rows_with_values if value == self.date), None)

                # only update if the date exists in sheet
                if row:
                    self.service.spreadsheets().values().update(
                    spreadsheetId = self.sheetid,
                    range = f"{subject}!B{row}",
                    valueInputOption = "USER_ENTERED",
                    body = {"values": value}
                    ).execute()

        else:
            print("you do not have a class today dumbass")