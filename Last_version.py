import sys
import sqlite3 as sq
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QRadioButton
import time
base1 = [("Алексеев", "Илья", "Алексеевич", "23-Apr-1994", "директор по информатизации", "+79993456785",
          "aleksee45@mail.ru", "NULL", "NULL"),
         ("Аржанов", "Владислав", "Александрович", "27-Jan-1995", "начальние отдела кадров", "+79063194556",
          "arhjanov12@yandex.ru", "NULL", "NULL"),
         ("Белоцерковец ", "Дмитрий", "Александрович", "12-Sep-1983", "менеджер", "+79773332123",
          "belotserkovets@gmail.com", "NULL", "NULL"),
         ("Богушев", "Арсений", "Александрович", "09-Dec-1973", "директор", "+79264444334", "Bogushev@mail.ru", "NULL",
          "NULL"),
         ("Гундарова", "Софья", "Анатольевна", "30-Nov-1995", "менеджер", "+79256789012", "Gundarova@yandex.ru", "NULL",
          "NULL"),
         ("Долженков", "Борис", "Алексеевич", "23-Jun-2002", "курьер", "+79003196748", "Dolzhenkov@gmail.com", "NULL",
          "NULL"),
         ("Журавова", "Ангелина", "Сергеевна", "17-Aug-2002", "специалист по корреспонденции", "+79836571245",
          "Zhuravova@gmail.com", "NULL", "NULL"),
         ("Клевцова", "Варвара", "Андреевна", "15-Oct-2002", "секретарь", "+79023672156", "Klevtsova@gmail.com", "NULL",
          "NULL"),
         ("Коваленко", "Вероника", "Александровна", "17-Jul-1997", "менеджер", "+79271285522", "Kovalenko@gmail.com",
          "NULL", "NULL"),
         ("Королев", "Платон", "Валеорьевич", "13-Mar-1993", "главный бухгалтер", "+79773045689", "Korolev@gmail.com",
          "NULL", "NULL"),
         ("Кубышкин", "Роман", "Евгеньевич", "10-Oct-1985", "менеджер по технологии", "+79013219045",
          "Kubyshkin@gmail.com", "NULL", "NULL"),
         ("Макаренко", "Константин", "Викторович", "11-Nov-1984", "бизнес аналитик", "+79992341289",
          "Makarenko@gmail.com", "NULL", "NULL"),
         ("Мартиросов", "Артемий", "Артурович", "01-Feb-1974", "smm - менеджер", "+79027893459", "Martirosov@gmail.com",
          "NULL", "NULL"),
         (
         "Мелкумян", "Роберт", "Робертович", "16-May-1993", "маркетолог", "+79982341290", "Melkumyan@gmail.com", "NULL",
         "NULL"),
         ("Олейник", "Ольга", "Викторовна", "18-Jun-1993", "руководитель проекта", "+79762349987", "Oleinik@gmail.com",
          "NULL", "NULL"),
         ("Полюцкий", "Александр", "Сергеевич", "19-Jan-1981", "юрист-консультант", "+79673421894",
          "Polyutsky@gmail.com", "NULL", "NULL"),
         ("Рустамов", "Иброхим", "Рустамович", "29-Oct-1982", "зав.хозяйством", "+79231782392", "Rustamov@gmail.com",
          "NULL", "NULL"),
         (
         "Рябцева", "Алена", "Александровна", "14-Nov-1982", "бухгалтер", "+79321743981", "Ryabtseva@gmail.com", "NULL",
         "NULL"),
         ("Саберова", "Динара", "Равилевна", "28-Dec-1994", "главный юрист", "+79992341084", "Saberova@gmail.com",
          "NULL", "NULL"),
         ("Сафонова", "Ирина", "Ивановна", "15-Jul-1983", "делопроизводитель", "+79253419861", "Safonov@gmail.com",
          "NULL", "NULL"),
         ("Стронина", "София", "Евгеньевна", "31-Mar-2002", "секретарь", "+79162381629", "Stronina@gmail.com", "NULL",
          "NULL"),
         ("Тарасов", "Степан", "Павлович", "06-Jun-1996", "менеджер", "+79152371823", "Тарасов@gmail.com", "NULL",
          "NULL"),
         ("Чекменёв", "Кирилл", "Андреевич", "02-Aug-1998", "дизайнер", "+79172361959", "Chekmenev@gmail.com", "NULL",
          "NULL"),
         ("Чернов", "Максим", "Дмитриевич", "23-Dec-1999", "аналитик", "+79293652732", "Chernov@gmail.com", "NULL",
          "NULL"),
         (
         "Шарофидинова", "Ирода", "Отабек", "21-Mar-1991", "уборщица", "+79002893276", "Sharofidinov@gmail.com", "NULL",
         "NULL"),
         ("Шундрик", "Егор", "Максимович", "07-Apr-1992", "расчетчик", "+79281123119", "Shundrick@gmail.com", "NULL",
          "NULL"),
         ("Шушняев", "Никита", "Максимовна", "09-Sep-1991", "сметчик", "+79031732861", "Shushnyaev@gmail.com", "NULL",
          "NULL")]
personal = 20
ghosti = 5
local = time.ctime(time.time())
with sq.connect("base.db") as base:
    m_data = base.cursor()
    m_data.execute('DROP TABLE IF EXISTS rabotniki')
    m_data.execute("""CREATE TABLE IF NOT EXISTS rabotniki(
                        famil TEXT,
                        name TEXT,
                        otch TEXT,
                        date TEXT,
                        dol TEXT,
                        nomer TEXT,
                        pochta TEXT,
                        time_ek TEXT ,
                        time_ex TEXT 
                        );
                        """)
    m_data.executemany("INSERT INTO rabotniki VALUES(?, ? , ?, ?, ? , ?, ? , ?,?)", base1)
    base.commit()
with sq.connect("gosti.db") as base2:
    s_data = base2.cursor()
    s_data.execute('DROP TABLE IF EXISTS gosti')
    s_data.execute("""CREATE TABLE IF NOT EXISTS gosti(
                        famil TEXT,
                        name TEXT,
                        otch TEXT,
                        date TEXT,
                        nomer TEXT,
                        pochta TEXT,
                        time_ek INT ,
                        time_ex INT 
                        );
                        """)
    base2.commit()
class PassControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,500)
        global m_data
        global base
        global personal
        global ghosti
        self.m_data = 0
        self.car = 0
        self.RadioButton = QRadioButton("Есть машина?")
        self.issue_pass_button3 = QPushButton('Вышел')
        self.issue_pass_button = QPushButton('Зашёл')
        self.issue_pass_button2 = QPushButton('Гостевой пропуск')
        self.issue_pass_button.clicked.connect(self.eks)
        self.issue_pass_button3.clicked.connect(self.ex)
        self.issue_pass_button2.clicked.connect(self.time_c)
        self.RadioButton.toggled.connect(self.parking)
        self.name = QLineEdit(self, placeholderText="почта сотрудника...")
        self.passv = QLineEdit(self, placeholderText="имя...")
        layout = QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.passv)
        layout.addWidget(self.RadioButton)
        layout.addWidget(self.issue_pass_button2)
        layout.addWidget(self.issue_pass_button)
        layout.addWidget(self.issue_pass_button3)
        self.setLayout(layout)
        self.setWindowTitle('Терминал Охранника')
    def time_c(self):
        pass1.show()
    def eks(self):
        global ghosti
        global personal
        self.dog = self.name.text().find("@")
        self.poch = self.name.text()
        self.local_time = time.ctime(time.time())
        if self.car == 1:
            if personal != 0:
                if personal < 5 and ghosti > 0:
                    personal -= 1
                    ghosti -= 1
                else:
                    personal -= 1
                m_data.execute(f"""UPDATE rabotniki SET time_ek = ? where pochta=?""", [self.local_time, self.poch])
                m_data.execute('SELECT pochta FROM rabotniki')
                self.rows = m_data.fetchall()
                if self.rows.count((self.name.text(),)):
                    print("Сотрудник", self.poch, "Вошёл")
                else:
                    print("Такой почты в базе данных нет")
                base.commit()
            else:
                print("Мест нет")
        elif self.car == 0:
            m_data.execute(f"""UPDATE rabotniki SET time_ek = ? where pochta=?""", [self.local_time, self.poch])
            base.commit()
            m_data.execute('SELECT pochta FROM rabotniki')
            self.rows = m_data.fetchall()
            if self.rows.count((self.name.text(),)):
                print("сотрудник", self.poch, "Вошёл !")
            else:
                print("в базе данных нет этой почты")
    def ex(self):
        global ghosti
        global personal
        self.poch = self.name.text()
        if self.car == 1:
            if personal < 5 and ghosti < 5:
                personal += 1
                ghosti += 1
            personal += 1
        self.local_time = time.ctime(time.time())
        m_data.execute(f"""UPDATE rabotniki SET time_ex = ? where pochta=? AND time_ek!='NULL' """,
                    [self.local_time, self.poch])
        m_data.execute('SELECT pochta FROM rabotniki')
        self.rows = m_data.fetchall()
        if self.rows.count((self.name.text(),)):
            print("Сотрудник", self.poch, "Вышел")
        else:
            print("Такой почты нет в базе данных")
        base.commit()
        base.commit()
    def parking(self):
        if self.car == 0:
            self.car = 1
        else:
            self.car = 0
        print(self.car)
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,400)
        self.car = 0
        global s_data
        global base2
        global personal
        global ghosti
        self.issue_pass_button2 = QPushButton('Выдать пропуск на выход')
        self.issue_pass_button = QPushButton('Выдать пропуск')
        self.RadioButton = QRadioButton("Есть ли машина?")
        self.issue_pass_button.clicked.connect(self.Goshti)
        self.issue_pass_button2.clicked.connect(self.time_c)
        self.RadioButton.toggled.connect(self.parking)
        self.ex = QLineEdit(self, placeholderText="Ведите контактную почту для выхода...")
        self.famil = QLineEdit(self, placeholderText="Ведите фамилию ...")
        self.name = QLineEdit(self, placeholderText="Ведите имя...")
        self.otch = QLineEdit(self, placeholderText="Ведите отчество...")
        self.date = QLineEdit(self, placeholderText="Ведите дату рождения...")
        self.nomer = QLineEdit(self, placeholderText="Ведите номер телефона...")
        self.pochta = QLineEdit(self, placeholderText="Ведите контактную почту...")
        layout = QVBoxLayout()
        layout.addWidget(self.famil)
        layout.addWidget(self.name)
        layout.addWidget(self.otch)
        layout.addWidget(self.date)
        layout.addWidget(self.nomer)
        layout.addWidget(self.pochta)
        layout.addWidget(self.RadioButton)
        layout.addWidget(self.issue_pass_button)
        layout.addWidget(self.ex)
        layout.addWidget(self.issue_pass_button2)
        self.setLayout(layout)
        self.setWindowTitle('Пропускной пункт для гостей')
    def parking(self):
        if self.car == 0:
            self.car = 1
        else:
            self.car = 0
        if ghosti == 0:
            print("Порковочных мест нет")
    def Goshti(self):
        global ghosti
        global personal
        if self.car == 1:
            if ghosti == 0:
                print("Парковочных мест нет приходите позже!!!")
            else:
                personal -= 1
                ghosti -= 1
                self.time = time.time()
                self.familt = self.famil.text()
                self.namet = self.name.text()
                self.otcht = self.otch.text()
                self.datet = self.date.text()
                self.nomert = self.nomer.text()
                self.pochtat = self.pochta.text()
                self.CORT = [(self.familt, self.namet, self.otcht, self.datet,self.nomert, self.pochtat,
                              self.time, 0)]
                s_data.execute('SELECT pochta FROM gosti')
                self.rows = s_data.fetchall()
                if self.rows.count((self.pochta.text(),)):
                    print("Такая почта уже есть")
                else:
                    print("Гость", self.pochtat, "Вошёл")
                    s_data.executemany("INSERT INTO gosti VALUES(?, ? , ?, ?, ? , ?, ? , ?,?)", self.CORT)
                    base2.commit()
        else:
            self.time = time.time()
            self.familt = self.famil.text()
            self.namet = self.name.text()
            self.otcht = self.otch.text()
            self.datet = self.date.text()
            self.nomert = self.nomer.text()
            self.pochtat = self.pochta.text()
            self.CORT = [
                (self.familt, self.namet, self.otcht, self.datet, self.nomert, self.pochtat, self.time, 0)]
            s_data.execute('SELECT pochta FROM gosti')
            self.rows = s_data.fetchall()
            if self.rows.count((self.pochta.text(),)):
                print("Такая почта уже есть")
            else:
                print("Гость", self.pochtat, "Вошёл")
                s_data.executemany("INSERT INTO gosti VALUES(?, ? , ?, ?, ? , ?, ? , ?,?)", self.CORT)
                base2.commit()
            s_data.execute('SELECT time_ek,time_ex FROM gosti WHERE pochta=?', (self.pochtat,))
            self.rows2 = s_data.fetchall()
            self.tkk = self.rows2[0]
            self.tk = self.tkk
    def time_c(self):
        global ghosti
        global personal
        if self.car == 1:
            personal += 1
            ghosti += 1
        self.exi = self.ex.text()
        self.time = time.time()
        self.local_time = time.ctime(time.time())
        s_data.execute(f"""UPDATE gosti SET time_ex = ? where pochta=? """, [self.time, self.exi])
        s_data.execute('SELECT pochta FROM gosti')
        self.rows = s_data.fetchall()
        if self.rows.count((self.ex.text(),)):
            print("Гость", self.exi, "Вышел")
            s_data.execute('SELECT time_ek,time_ex FROM gosti WHERE pochta=?', (self.pochtat,))
            self.rows2 = s_data.fetchall()
            self.tkk = self.rows2[0]
            self.tk, self.tx = self.tkk
            if self.tx - self.tk > 10:
                print(
                    f"Гость {self.exi} - привысил время посещения на {(self.tx) - (self.tk) - 10} сек, 'ОБРАТИТЕСЬ К НАЧАЛЬНИКУ ОХРАНЫ'")
            if self.tx - self.tk < 10:
                print(f"Гость {self.exi} пробыл внутри {(self.tx) - (self.tk)} сек")
        else:
            print("Такой почты нет в базе данных")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pass_control = PassControlApp()
    pass1 = App()
    pass_control.show()
    sys.exit(app.exec())
