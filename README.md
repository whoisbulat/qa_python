1  test_add_new_book_add_two_books - проверка добавления двух книг
2 test_add_new_book_valid_number_added - проверка добавления книги с названием более 0 символов и не более 40 символов. Тест граничных значений: 1, 2, 30 и 40, а также внутри КЭ: 21 символ
3 test_add_new_book_invalid_number_not_added - негативный тест на проверку длины названия книги. 0, 41, 50 символов
4 test_set_book_genre_valid_genre_added - проверка на добавление жанра книге
5 test_get_book_genre_valid_name_book_received - проверка получения жанра книги по имени книги
6 test_get_books_genre_two_valid_name_book_received - проверка получение словаря books_genre
7 test_get_books_with_specific_genre_returns_correct_list_when_books_added - проверка вывода книги с определённым жанром
8 test_get_books_for_children_valid_book_for_children_return - проверка на получение книг доступных для детей
9 test_get_books_for_children_invalid_book_for_children_not_return - негативная проверка теста 8
10 test_add_book_in_favorites_one_book_added - проверка добавления книги в избранное
11 test_delete_book_from_favorites_book_exists_book_removed - проверка удаления книги из избранного
12 test_get_list_of_favorites_books_one_book_exists_returns_list_with_one_book - проверка получения списка избранного