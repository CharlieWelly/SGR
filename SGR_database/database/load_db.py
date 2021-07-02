from openpyxl import load_workbook
from django.core.exceptions import ObjectDoesNotExist


class IndustryToDB(object):
    def __init__(self, excel_file):
        self.excel_file = excel_file
        (
            self.industry_group_1,
            self.industry_group_2,
            self.industry,
        ) = self.get_industries()

    def get_industries(self):
        wb = load_workbook(self.excel_file)
        try:
            ws = wb["Bản đồ ngành"]
        except IndexError:
            raise IndexError("There is no such sheet")
        else:
            industry_group_1 = set()
            industry_group_2 = set()
            industry = dict()
            # to skip the heading
            g = ws.iter_rows(values_only=True)
            next(g)
            # -------------------
            for couple in g:
                industry_2, industry_1 = couple
                industry_group_1.add(industry_1)
                industry_group_2.add(industry_2)
                industry[industry_2] = industry_1
            return industry_group_1, industry_group_2, industry

    def industry_level1_to_db(self, IndustryLevel1):
        """ """
        industries = list(self.industry_group_1)
        for industry in industries:
            IndustryLevel1.objects.create(industry_level_1=industry)

    def industry_to_db(self, IndustryLevel1, Industry):
        for key, value in self.industry.items():
            level_1 = IndustryLevel1.objects.get(industry_level_1=value)
            Industry.objects.create(industry_level_1=level_1, industry_level_2=key)


class CompanyToDB(object):
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.stock_exchange_dict = self.get_companies()

    def get_companies(self):
        wb = load_workbook(filename=self.excel_file)
        ws = wb["Danh sách tất cả công ty"]
        stock_exchange_dict = dict()

        # to skip the heading
        g = ws.iter_rows(values_only=True)
        next(g)
        # -------------------
        for row in g:
            try:
                (
                    _,
                    code_vs,
                    company_name,
                    industry_level_1,
                    industry_level_2,
                    exchange,
                    issue_amount,
                ) = row
            except ValueError:
                print(row)
                raise ValueError("this is the bad one")
            if exchange not in stock_exchange_dict:
                stock_exchange_dict[exchange] = {}
            if industry_level_2 not in stock_exchange_dict[exchange]:
                stock_exchange_dict[exchange][industry_level_2] = []
            stock_exchange_dict[exchange][industry_level_2].append(
                (
                    company_name,
                    code_vs,
                )
            )
        return stock_exchange_dict

    def company_to_db(self, Company, StockExchange, Industry):
        for stock_exchange, value_1 in self.stock_exchange_dict.items():
            exchange = StockExchange.objects.get(stock_exchange=stock_exchange)
            for industry_level_2, value_2 in value_1.items():
                try:
                    industry = Industry.objects.get(industry_level_2=industry_level_2)
                    for value_3 in value_2:
                        name, code_vs = value_3
                        Company.objects.create(
                            code_vs=code_vs,
                            name=name,
                            industry=industry,
                            exchange=exchange,
                        )
                except ObjectDoesNotExist as e:
                    print(industry_level_2, value_2)
                    raise e
