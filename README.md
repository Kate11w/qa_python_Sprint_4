# Тестирование приложения `BooksCollector`

**Список тестов**

* `test_add_new_book_adds_two_books` - Проверяет добавление двух новых уникальных книг.
* `test_add_new_book_ignores_duplicates` - Проверяет, что одну и ту же книгу можно добавить только один раз.
* `test_set_book_genre_sets_genre` - Проверяет добавление жанра для книги.
* `test_get_book_genre_returns_correct_genre` - Проверяет вывод корректного жанра.
* `test_get_book_genre_returns_empty_for_new_book` - Проверяет, что у новой книги по умолчанию нет жанра.
* `test_get_books_with_specific_genre_returns_books_with_specified_genre` - Возвращаются только книги определенного жанра.
* `test_get_books_genre_returns_all_books_with_genres` - Проверка, что словарь books_genre содержит все добавленные книги и их жанры.
* `test_get_books_for_children_returns_only_allowed_books` - Проверяет, что книги с возрастным ограничением не попадают в список книг для детей.
* `test_add_book_in_favorites_adds_book` - Книга корректно добавляется в список избранного.
* `test_delete_book_from_favorites_removes_book` - Удаление книги из избранного работает корректно.
* `test_get_list_of_favorites_books_returns_added_books` - Возвращается точный список избранных книг.











