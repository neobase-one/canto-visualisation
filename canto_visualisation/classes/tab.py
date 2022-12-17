from abc import ABC, abstractmethod
from config.web3 import get_web3_provider
from config.database import get_db_connection

class Tab(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.w3 = get_web3_provider()
        self.db_connection = get_db_connection()

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def create_graph(self, df):
        pass

    @abstractmethod
    def fill_tab(self):
        pass
