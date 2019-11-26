from PySide2.QtWidgets import QApplication
from forms.main_form import MainForm
import sys
from config import Config
from util import *

if __name__ == "__main__":
    Config.load_config(config_path)

    app = QApplication(sys.argv)

    window = MainForm()
    window.show()

    sys.exit(app.exec_())
