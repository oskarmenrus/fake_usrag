import os
import random


class FakeUserAgentBOR:
    """Основной класс, управляющий генерацией user-agent'ов"""

    def __init__(self):
        """Инициализация основных переменных"""
        # Путь к файлам с user-agent'ами
        self.path_to_files = os.path.join(os.path.normcase(os.path.dirname(__file__)), 'list_of_user_agents')
        # Случайный файл из директории
        self.random_file = random.choice(os.listdir(self.path_to_files))

    def random_user_agent(self, random_file: str = None) -> str:
        """Возвращает случайного user-agent'а, если именованный аргумент random_file не указан"""
        if random_file is None:
            random_file = self.random_file

        with open(self.path_to_files + os.sep + random_file) as file:
            random_user_agent = random.choice(file.read().split('\n'))

        return random_user_agent

    def random_android_user_agent(self) -> str:
        """Возвращает случайного Android user-agent'а"""
        return self.random_user_agent('AndroidWebkitBrowser.txt')

    def random_chrome_user_agent(self) -> str:
        """Возвращает случайного Google Chrome user-agent'а"""
        return self.random_user_agent('Chrome.txt')

    def random_edge_user_agent(self) -> str:
        """Возвращает случайного Edge user-agent'а"""
        return self.random_user_agent('Edge.txt')

    def random_firefox_user_agent(self) -> str:
        """Возвращает случайного Mozilla Firefox user-agent'а"""
        return self.random_user_agent('Firefox.txt')

    def random_ie_user_agent(self) -> str:
        """Возвращает случайного Internet Explorer user-agent'а"""
        return self.random_user_agent('InternetExplorer.txt')

    def random_opera_user_agent(self) -> str:
        """Возвращает случайного Opera user-agent'а"""
        return self.random_user_agent('Opera.txt')

    def random_safari_user_agent(self) -> str:
        """Возвращает случайного Safari user-agent'а"""
        return self.random_user_agent('Safari.txt')

    def simple_header(self, func: object = None) -> dict:
        """Возвращает словарь с простейшим header'ом, включающим в себя случайный user-agent.

        В качесте именованного аргумента принимает объект функции, для получения определенного user-agent'а.

        Пример header'а со случайным user-agent'ом:
            import user_agent_bor
            fake_u_a = user_agent_bor.FakeUserAgentBOR()
            fake_u_a.simple_header()
            >> {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20040913 Firefox/0.10'}

        Пример header'а с определенным user-agent'ом (в данном случае - Opera):
            import user_agent_bor
            fake_u_a = user_agent_bor.FakeUserAgentBOR()
            fake_u_a.simple_header(fake_u_a.random_opera_user_agent)
            >> {'User-Agent': 'Opera/7.10 (Windows NT 5.1; U)  [en]'}

        """
        if func is None:
            func = self.random_user_agent

        return {'User-Agent': f'{func()}'}
