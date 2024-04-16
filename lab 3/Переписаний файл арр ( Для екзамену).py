import webbrowser

class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    
    def __init__(self, type, length, color) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length
        self.color = color

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length

    @property
    def get_color(self):
        return self.color

    @staticmethod
    def visit_website(website_url):
        webbrowser.open_new_tab(website_url)

# Поза блоком класу Figure
figure = Figure("квадрат", 5, "червоний")
figure.visit_website("https://itcollege.lviv.ua/")
