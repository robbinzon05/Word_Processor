import sys
from PyQt5.QtWidgets import QApplication
from ProcessorWindow import ProcessorWindow


def main():
    app = QApplication(sys.argv)
    wordProcessor = ProcessorWindow()
    wordProcessor.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
