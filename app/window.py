import pyforms;
from   pyforms          import BaseWidget;
from   pyforms.Controls import ControlText;
from   pyforms.Controls import ControlButton;

class DataScraperWindow(BaseWidget):
    def __init__(self):
        super(DataScraperWindow, self).__init__('Data finder');

        self._test = ControlText('Test', 'Default Value');

if __name__ == "__main__":
    pyforms.start_app(DataScraperWindow);
