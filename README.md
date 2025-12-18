В данном проекте реализованы автоматизированные тесты для класса `BooksCollector`

Тест 1: test_add_new_book_valid_name_book_added Проверка добавления новой книги с корректным названием
Тест 2: test_add_new_book_invalid_length_book_not_added Проверка, что книга с некорректной длиной названия не добавляется
Тест 3: test_add_new_book_duplicate_book_not_added Проверка, что дублирование книги не происходит
Тест 4: test_set_and_get_book_genre_valid_genre_set Проверка установки и получения жанра для книги
Тест 5: test_set_book_genre_invalid_genre_not_set Тест 5 Проверка, что нельзя установить недопустимый жанр
Тест 6: test_get_books_with_specific_genre_multiple_books Параметризованный тест получения книг по жанру
Тест 7: test_get_books_for_children_only_child_friendly Проверка получения книг для детей
Тест 8: test_favorites_operations_add_remove_get Проверка работы с избранными книгами
Тест 9: test_add_book_in_favorites_nonexistent_book_not_added Проверка, что нельзя добавить в избранное несуществующую книгу
