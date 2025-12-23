import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_valid_name_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        assert 'Властелин колец' in collector.get_books_genre()


    @pytest.mark.parametrize('book_name', [
        '',
        'Очень длинное название книги, которое явно превышает лимит в 40 символов'
    ])
    def test_add_new_book_invalid_length_book_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()


    def test_add_new_book_duplicate_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 1


    def test_set_and_get_book_genre_valid_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.set_book_genre('Марсианин', 'Фантастика')
        assert collector.get_book_genre('Марсианин') == 'Фантастика'


    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Боевик')
        assert collector.get_book_genre('Шерлок Холмс') == ''


    @pytest.mark.parametrize(
        'genre, expected_count',
        [
            ('Ужасы', 2),
            ('Комедии', 1),
        ]
    )
    def test_get_books_with_specific_genre(self, genre, expected_count):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Ужасы')

        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2', 'Комедии')

        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 3', 'Ужасы')

        books = collector.get_books_with_specific_genre(genre)
        assert len(books) == expected_count


    def test_get_books_for_children_only_child_friendly(self):
        collector = BooksCollector()

        books = [
            ('Гарри Поттер', 'Фантастика'),
            ('Оно', 'Ужасы'),
            ('Трое в лодке', 'Комедии'),
            ('Десять негритят', 'Детективы')
        ]

        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        children_books = collector.get_books_for_children()
        assert children_books == ['Гарри Поттер', 'Трое в лодке']



    def test_add_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in collector.get_list_of_favorites_books()

    def test_add_book_to_favorites_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_book_in_favorites('Преступление и наказание')
        collector.delete_book_from_favorites('Преступление и наказание')
        assert 'Преступление и наказание' not in collector.get_list_of_favorites_books()


    def test_add_book_in_favorites_nonexistent_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Существующая книга')
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()
