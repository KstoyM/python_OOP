from project_bakery.table.table import Table


class InsideTable(Table):

    @property
    def table_type(self):
        return self.__class__.__name__

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not 1 <= value <= 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value



