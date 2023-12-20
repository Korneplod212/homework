import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit


class DiceProbabilityApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор ввероятностей')
        self.resize(300, 200)

        self.layout = QVBoxLayout()

        self.dice_count_label = QLabel('Введите кол-во костей')
        self.dice_count_input = QLineEdit()

        self.roll_count_label = QLabel('Введите кол-во бросков')
        self.roll_count_input = QLineEdit()

        self.calculate_button = QPushButton('Рассчитать вероятности')
        self.calculate_button.clicked.connect(self.calculate_probability)

        self.layout.addWidget(self.dice_count_label)
        self.layout.addWidget(self.dice_count_input)
        self.layout.addWidget(self.roll_count_label)
        self.layout.addWidget(self.roll_count_input)
        self.layout.addWidget(self.calculate_button)

        self.setLayout(self.layout)

    def calculate_probability(self):
        dice_count = int(self.dice_count_input.text())
        roll_count = int(self.roll_count_input.text())
        probabilities = self.calculate_probabilities(dice_count, roll_count)

        probability_output = 'Вероятносити для каждой суммы {} бросок костей:\n'.format(roll_count)
        for total, probability in probabilities.items():
            probability_output += '{}: {:.3f}%\n'.format(total, probability * 100)

        self.result_window = ResultWindow(probability_output, self)
        self.result_window.show()

    def calculate_probabilities(self, dice_count, roll_count):
        results = {}

        def calculate_dice_sum(dice, current_sum):
            if dice == 0:
                if current_sum in results:
                    results[current_sum] += 1
                else:
                    results[current_sum] = 1
            else:
                for i in range(1, 7):
                    calculate_dice_sum(dice - 1, current_sum + i)

        for _ in range(roll_count):
            calculate_dice_sum(dice_count, 0)

        total_possibilities = 6 ** dice_count
        probabilities = {total: count / total_possibilities for total, count in results.items()}

        return probabilities


class ResultWindow(QWidget):
    def __init__(self, probability_output, main_window):
        super().__init__()
        self.setWindowTitle('Результаты вероятностей')
        self.resize(300, 400)

        self.layout = QVBoxLayout()

        self.probability_text = QTextEdit()
        self.probability_text.setPlainText(probability_output)
        self.probability_text.setReadOnly(True)

        self.close_button = QPushButton('Закрыть')
        self.close_button.clicked.connect(self.close_window)

        self.layout.addWidget(self.probability_text)
        self.layout.addWidget(self.close_button)

        self.setLayout(self.layout)

        self.main_window = main_window

    def close_window(self):
        self.close()
        self.main_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = DiceProbabilityApp()
    main_app.show()
    sys.exit(app.exec())
