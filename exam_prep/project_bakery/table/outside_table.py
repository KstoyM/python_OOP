from project_bakery.table.table import Table


class OutsideTable(Table):

    @property
    def table_type(self):
        return self.__class__.__name__

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not 51 <= value <= 100:
            raise ValueError("Inside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value