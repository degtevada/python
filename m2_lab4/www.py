class Publication:
    """
    Базовый класс для всех публикаций в литературном издательстве.
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Инициализирует объект публикации.

        :param title: Название публикации.
        :param author: Автор публикации.
        :param year: Год выпуска.
        """
        self._title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"{self._title} ({self.year}), автор: {self.author}"

    def __repr__(self) -> str:
        return f"Publication(title={self._title}, author={self.author}, year={self.year})"

    def publish(self) -> str:
        """
        Публикует произведение.

        :return: Сообщение о публикации.
        """
        return "Произведение опубликовано."


class Book(Publication):
    """
    Дочерний класс для книг.
    """

    def __init__(self, title: str, author: str, year: int, pages: int) -> None:
        """
        Инициализирует объект книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания.
        :param pages: Количество страниц в книге.
        """
        super().__init__(title, author, year)
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга: {self._title}, автор: {self.author}, {self.year}, {self.pages} страниц."

    def __repr__(self) -> str:
        return f"Book(title={self._title}, author={self.author}, year={self.year}, pages={self.pages})"

    def publish(self) -> str:
        """
        Переопределенный метод публикации.

        Причина: Книги могут издаваться в разных форматах (твердый переплет, электронный вариант и т. д.).

        :return: Сообщение о публикации книги.
        """
        return "Книга издана в печатном и электронном вариантах."


class Magazine(Publication):
    """
    Дочерний класс для журналов.
    """

    def __init__(self, title: str, author: str, year: int, issue: int) -> None:
        """
        Инициализирует объект журнала.

        :param title: Название журнала.
        :param author: Автор или редакция журнала.
        :param year: Год издания.
        :param issue: Номер выпуска журнала.
        """
        super().__init__(title, author, year)
        self.issue = issue

    def __str__(self) -> str:
        return f"Журнал: {self._title}, автор: {self.author}, {self.year}, выпуск №{self.issue}."

    def __repr__(self) -> str:
        return f"Magazine(title={self._title}, author={self.author}, year={self.year}, issue={self.issue})"

    def distribute(self) -> str:
        """
        Распространяет журнал среди подписчиков.

        :return: Сообщение о распространении журнала.
        """
        return "Журнал разослан подписчикам."


if __name__ == "__main__":
    book = Book("Война и мир", "Лев Толстой", 1869, 1225)
    magazine = Magazine("Наука и жизнь", "Редакция", 2024, 5)
    print(book)
    print(magazine)
    print(book.publish())
    print(magazine.distribute())
