import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2


    def test_add_new_book_ignores_duplicates(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_new_book(book)

        assert len(collector.get_books_genre()) == 1


    def test_set_book_genre_sets_genre(self, book):
        collector = BooksCollector()
        collector.books_genre[book] = ''
        collector.set_book_genre(book, 'Фантастика')

        assert collector.books_genre[book] == 'Фантастика'


    @pytest.mark.parametrize('book_name, genre', [
        ('Двенадцать стульев', 'Комедии'),
        ('Зов Ктулху', 'Ужасы'),
        ('Маленький принц', 'Мультфильмы'),
    ])
    def test_get_book_genre_returns_correct_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.books_genre[book_name] = genre

        assert collector.get_book_genre(book_name) == genre


    def test_get_book_genre_returns_empty_for_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')

        assert collector.get_book_genre('Маленький принц') == ''


    def test_get_books_with_specific_genre_returns_books_with_specified_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Зов Ктулху')
        collector.set_book_genre('Зов Ктулху', 'Ужасы')
        result = collector.get_books_with_specific_genre('Фантастика')

        assert result == ['Дюна']


    @pytest.mark.parametrize('book_name, genre', [
        ('Двенадцать стульев', 'Комедии'),
        ('Дюна', 'Фантастика'),
        ('Маленький принц', 'Мультфильмы'),
        ('Зов Ктулху', 'Ужасы'),
        ('451 градус по Фаренгейту', 'Фантастика'),
    ])

    def test_get_books_genre_returns_all_books_with_genres(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books_genre = collector.get_books_genre()

        assert book_name in books_genre
        assert books_genre[book_name] == genre


    @pytest.mark.parametrize('book_name, genre', [
        ('Маленький принц', 'Мультфильмы'),
        ('Трое в лодке, не считая собаки', 'Комедии'),
        ('Дюна', 'Фантастика'),
    ])

    def test_get_books_for_children_returns_only_allowed_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        children_books = collector.get_books_for_children()

        assert book_name in children_books
        assert collector.get_book_genre(book_name) not in collector.genre_age_rating


    def test_add_book_in_favorites_adds_book(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert book in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites_removes_book(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert book not in collector.get_list_of_favorites_books()


    def test_get_list_of_favorites_books_returns_added_books(self):
        collector = BooksCollector()
        books = [
            'Дюна',
            'Маленький принц',
            'Трое в лодке, не считая собаки'
        ]

        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        favorites = collector.get_list_of_favorites_books()

        assert favorites == books
