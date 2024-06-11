class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author._all_authors.append(self)

    @classmethod
    def all_authors(cls):
        return cls._all_authors

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book object expected.")
        if not isinstance(date, str):
            raise Exception("Date should be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties should be an integer.")
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book._all_books.append(self)

    @classmethod
    def all_books(cls):
        return cls._all_books


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract._all_contracts.append(self)

    @classmethod
    def all_contracts(cls):
        return cls._all_contracts

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls._all_contracts if contract.date == date]
