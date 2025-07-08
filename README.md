# BooksCollector

Проект **BooksCollector** — это приложение для управления коллекцией книг. Оно позволяет:
- Добавлять новые книги
- Задавать жанры книгам
- Получать книги, подходящие для детей
- Добавлять книги в избранное и удалять их из избранного

## 📋 Зависимости и требования

Для запуска проекта необходимы:
- **Python** (версия 3.7 или выше)
- **pytest** (для запуска тестов)

Установите зависимости с помощью команды:
```bash
pip install pytest
🧪 Тесты
Проект включает следующие автоматические тесты:

1. Проверка добавления книг
test_add_new_book_add_two_books
Проверка добавления двух книг.

test_add_new_book_valid_number_added
Проверка добавления книги с допустимой длиной названия (1–40 символов).
Тест граничных значений: 1, 2, 30, 40, а также внутри КЭ: 21 символ.

test_add_new_book_invalid_number_not_added
Негативный тест на проверку длины названия книги (0, 41, 50 символов).

2. Работа с жанрами
test_set_book_genre_valid_genre_added
Проверка добавления жанра книге.

test_get_book_genre_valid_name_book_received
Проверка получения жанра книги по её названию.

test_get_books_with_specific_genre_returns_correct_list_when_books_added
Проверка вывода книг с определённым жанром.

3. Проверка книг для детей
test_get_books_for_children_valid_book_for_children_return
Проверка получения книг, доступных для детей.

test_get_books_for_children_invalid_book_for_children_not_return
Негативная проверка (книги с недетскими жанрами не возвращаются).

4. Работа с избранным
test_add_book_in_favorites_one_book_added
Проверка добавления книги в избранное.

test_delete_book_from_favorites_book_exists_book_removed
Проверка удаления книги из избранного.

test_get_list_of_favorites_books_one_book_exists_returns_list_with_one_book
Проверка получения списка избранных книг.
