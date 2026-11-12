import sqlite3

class Database:
    conn = None
    nome_bd="agenda.db"

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")
 
    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()

    @classmethod
    def criar_tabelas(cls):
        # --------------------- Tabela Cliente ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                senha TEXT NOT NULL
            );
        """)

        # --------------------- Tabela Profissional ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS profissional (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                especialidade TEXT NULL,
                senha TEXT NOT NULL
            );
        """)

        # --------------------- Tabela Servico ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL
            );
        """)

        # --------------------- Tabela Horario ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS horario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                confirmado INTEGER DEFAULT 0,
                id_cliente INTEGER,
                id_servico INTEGER,
                id_profissional INTEGER,

                FOREIGN KEY (id_cliente) REFERENCES cliente(id) ON DELETE CASCADE,
                FOREIGN KEY (id_servico) REFERENCES servico(id) ON DELETE CASCADE,
                FOREIGN KEY (id_profissional) REFERENCES profissional(id) ON DELETE CASCADE
            );
        """)

        # --------------------- Tabela Atendimento ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS atendimento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                queixa_principal TEXT NULL,
                historico_saude TEXT NULL,
                avaliacao TEXT NULL,
                prescricao TEXT NULL,
                id_horario INTEGER,

                FOREIGN KEY (id_horario) REFERENCES horario(id) ON DELETE CASCADE
            );
        """)

if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()