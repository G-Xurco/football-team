import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from newfootballdesign import Ui_MainWindow
from PyQt5.QtCore import QStringListModel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the button
        self.ui.pushButton.clicked.connect(self.display_team)

    def display_team(self):
        # Extract player names and their positions
        positions_and_players = [
            (self.ui.lineEdit_3.text(), self.ui.comboBox.currentText()),  # Goalkeeper
            (self.ui.lineEdit_4.text(), self.ui.comboBox_2.currentText()),  # Central Defender 1
            (self.ui.lineEdit_5.text(), self.ui.comboBox_5.currentText()),  # Central Defender 2
            (self.ui.lineEdit_2.text(), self.ui.comboBox_11.currentText()),  # Right Back
            (self.ui.lineEdit_13.text(), self.ui.comboBox_12.currentText()),  # Left Back
            (self.ui.lineEdit_6.text(), self.ui.comboBox_6.currentText()),  # Midfielder 1
            (self.ui.lineEdit_7.text(), self.ui.comboBox_3.currentText()),  # Midfielder 2
            (self.ui.lineEdit_8.text(), self.ui.comboBox_7.currentText()),  # Midfielder 3
            (self.ui.lineEdit_9.text(), self.ui.comboBox_8.currentText()),  # Attacker 1
            (self.ui.lineEdit_10.text(), self.ui.comboBox_9.currentText()),  # Attacker 2
            (self.ui.lineEdit_11.text(), self.ui.comboBox_4.currentText()),  # Attacker 3
        ]

        captain_name = self.ui.comboBox_10.currentText().strip()
        if any(player.strip() == "" for _, player in positions_and_players):
                QMessageBox.warning(self, "შეცდომა", "გთხოვთ, შეავსოთ ყველა მოთამაშის პოზიცია.")
                return


        team_list = [f"{pos}: {player}" for pos, player in positions_and_players]
        team_list.append(f"კაპიტანი: {captain_name}")


        model = QStringListModel()
        model.setStringList(team_list)
        self.ui.listView.setModel(model)


    def update_label(self):
        user_text = self.lineEdit.text()
        self.label.setText(user_text)

        self.ui.pushButton.clicked.connect(self.update_label)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())