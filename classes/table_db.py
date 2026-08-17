import sqlite3 as sql

class TabelaDB():
    def __init__(self, id: int, name: str, data_name: str):
        self.id: int = id
        self.name: str = name
        self.data_name: str = data_name

class tabelaFrequênciaDB():
    def __init__(self, tabela_id: int, data: float, frequency: int):
        self.tabela_id: int = tabela_id
        self.data: float = data
        self.frequency: int = frequency

class AllTableDataDB():
    def __init__(self):
        self.table_rows: list[TabelaDB] = []

    def define_rows(self, rows: list[tuple]):
        for r in rows:
            self.table_rows.append(TabelaDB(r[0], r[1], r[2]))
            
class TableDataDB():
    def __init__(self):
        self.table: TabelaDB = None
        self.table_datas: list[tabelaFrequênciaDB] = []

    def define_table_row(self, row: tuple):
        self.table = TabelaDB(row[0], row[1], row[2])

    def define_table_data_rows(self, rows: list[tuple]):
        for r in rows:
            self.table_datas.append(tabelaFrequênciaDB(r[0], r[1], r[2]))

class TableDB():
    def __init__(self):
        self.connection: sql.Connection = sql.connect("table.db")
        self.cursor: sql.Cursor = self.connection.cursor()
        self._create_tables()

    def get_table_id(self, table_name: str) -> int | None:
        id: int = None
        self.cursor.execute(f"SELECT id FROM Tabela WHERE name = ?", (table_name,))
        result: tuple = self.cursor.fetchone()
        if result != None and len(result) != 0:
            id = result[0]
        return id

    def get_all_tables(self) -> AllTableDataDB:
        self.cursor.execute("SELECT * FROM Tabela")
        tables: AllTableDataDB = AllTableDataDB()
        tables.define_rows(self.cursor.fetchall())
        return tables

    def get_table(self, table_id: int) -> TableDataDB:
        table: TableDataDB = TableDataDB()
        self.cursor.execute("SELECT * FROM Tabela WHERE id = ?", (table_id,))
        table.define_table_row(self.cursor.fetchone())
        self.cursor.execute("SELECT * FROM tabelaFrequência WHERE tabela_id = ?", (table_id,))
        table.define_table_data_rows(self.cursor.fetchall())
        return table
        
    def has_table(self, table_name: str) -> bool:
        return True if self.get_table_id(table_name) != None else False

    def add_table(self, table_name: str, data_name: str, datas: list[tuple]) -> int:
        if not self.has_table(table_name):
            self.cursor.execute("INSERT INTO Tabela(name, data_name) VALUES (?, ?)", (table_name, data_name,))
        table_id: int = self.get_table_id(table_name)
        self.modify_table_datas(table_id, datas)
        return table_id

    def modify_table_names(self, table_id: int, new_name: str = "", new_data_name: str = "") -> None:
        if new_name != "" and not self.has_table(new_name):
            self.cursor.execute("UPDATE Tabela SET name = ? WHERE id = ?", (new_name, table_id,))
        if new_data_name != "":
            self.cursor.execute("UPDATE Tabela SET data_name = ? WHERE id = ?", (new_data_name, table_id,))
        self.connection.commit()

    def modify_table_datas(self, table_id: int, datas: list[tuple]) -> None:
        self.delete_datas(table_id)
        params: list[tuple] = [((table_id, d[0], d[1],)) for d in datas]
        self.cursor.executemany("INSERT INTO tabelaFrequência(tabela_id, data, frequency) VALUES (?, ?, ?)", params)
        self.connection.commit()

    def delete_datas(self, table_id: int) -> None:
        self.cursor.execute("DELETE FROM tabelaFrequência WHERE tabela_id = ?", (table_id,))
        self.connection.commit()

    def delete_table(self, table_id: int) -> None:
        self.delete_datas(table_id)
        self.cursor.execute("DELETE FROM Tabela WHERE id = ?", (table_id,))
        self.connection.commit()

    def _create_tables(self) -> None:
        try:
            self.cursor.execute("""
            CREATE TABLE Tabela(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(50) UNIQUE NOT NULL,
                data_name VARCHAR(20)
            )
            """)
        except sql.OperationalError:
            None
        try:
            self.cursor.execute("""
            CREATE TABLE tabelaFrequência(
                tabela_id INTEGER REFERENCES Tabela(id) NOT NULL, 
                data INTEGER NOT NULL, 
                frequency INTEGER NOT NULL
            )
        """)
        except sql.OperationalError:
            None