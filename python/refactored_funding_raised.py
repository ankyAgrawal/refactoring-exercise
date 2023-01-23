from typing import Dict, List
import pandas as pd

class FundingEvent:

    def __init__(self, file_path):
        self.file_path = file_path

    def filter_funding_events(self, fields: Dict) -> List[Dict]:
        """
        :param fields: Dict where key represents the csv field column and value represents the str
        to filter against
        :return: List of Dict where each Dict represents a funding event row.
        """
        df = pd.read_csv(self.file_path)
        if 'company_name' in fields:
            df = self.funding_events_by_company(df, fields.get('company_name'))
        if 'city' in fields:
            df = self.funding_events_by_city(df, fields.get('city'))
        if 'state' in fields:
            df = self.funding_events_by_state(df, fields.get('state'))
        if 'round' in fields:
            df = self.funding_events_by_round(df, fields.get('round'))
        return df.to_dict('records')

    @staticmethod
    def funding_events_by_company(df: pd.DataFrame, company_name: str) -> pd.DataFrame:
        df = df[df['company_name'] == company_name]
        return df

    @staticmethod
    def funding_events_by_city(df: pd.DataFrame, city: str) -> pd.DataFrame:
        df = df[df['city'] == city]
        return df

    @staticmethod
    def funding_events_by_state(df: pd.DataFrame, state: str) -> pd.DataFrame:
        df = df[df['state'] == state]
        return df

    @staticmethod
    def funding_events_by_round(df: pd.DataFrame, state: str) -> pd.DataFrame:
        df = df[df['round'] == state]
        return df


#     @staticmethod
#     def find_by(options):
#         with open("../startup_funding.csv", "rt") as csvfile:
#             data = csv.reader(csvfile, delimiter=',', quotechar='"')
#             # skip header
#             next(data)
#             csv_data = []
#             for row in data:
#                 csv_data.append(row)
#
#         if 'company_name' in options:
#             for row in csv_data:
#                 if row[1] == options['company_name']:
#                     mapped = {}
#                     mapped['permalink'] = row[0]
#                     mapped['company_name'] = row[1]
#                     mapped['number_employees'] = row[2]
#                     mapped['category'] = row[3]
#                     mapped['city'] = row[4]
#                     mapped['state'] = row[5]
#                     mapped['funded_date'] = row[6]
#                     mapped['raised_amount'] = row[7]
#                     mapped['raised_currency'] = row[8]
#                     mapped['round'] = row[9]
#                     return mapped
#
#         if 'city' in options:
#             for row in csv_data:
#                 if row[4] == options['city']:
#                     mapped = {}
#                     mapped['permalink'] = row[0]
#                     mapped['company_name'] = row[1]
#                     mapped['number_employees'] = row[2]
#                     mapped['category'] = row[3]
#                     mapped['city'] = row[4]
#                     mapped['state'] = row[5]
#                     mapped['funded_date'] = row[6]
#                     mapped['raised_amount'] = row[7]
#                     mapped['raised_currency'] = row[8]
#                     mapped['round'] = row[9]
#                     return mapped
#
#         if 'state' in options:
#             for row in csv_data:
#                 if row[5] == options['state']:
#                     mapped = {}
#                     mapped['permalink'] = row[0]
#                     mapped['company_name'] = row[1]
#                     mapped['number_employees'] = row[2]
#                     mapped['category'] = row[3]
#                     mapped['city'] = row[4]
#                     mapped['state'] = row[5]
#                     mapped['funded_date'] = row[6]
#                     mapped['raised_amount'] = row[7]
#                     mapped['raised_currency'] = row[8]
#                     mapped['round'] = row[9]
#                     return mapped
#
#         if 'round' in options:
#             for row in csv_data:
#                 if row[9] == options['round']:
#                     mapped = {}
#                     mapped['permalink'] = row[0]
#                     mapped['company_name'] = row[1]
#                     mapped['number_employees'] = row[2]
#                     mapped['category'] = row[3]
#                     mapped['city'] = row[4]
#                     mapped['state'] = row[5]
#                     mapped['funded_date'] = row[6]
#                     mapped['raised_amount'] = row[7]
#                     mapped['raised_currency'] = row[8]
#                     mapped['round'] = row[9]
#                     return mapped
#
#         raise RecordNotFound
#
#
# class RecordNotFound(Exception):
#     pass
if __name__ == "__main__":
    fe = FundingEvent("../startup_funding.csv")
    print(fe.filter_funding_events({"company_name":"Facebook"}))
    print("___________________________________________________")
    
