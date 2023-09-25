import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", [
        ("Д"),
        ("Дю"),
        ("книга состоящая из 30 символов"),
        ("Д" * 40),
        ("Д" * 21)
    ])
    def test_add_new_book_valid_number_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name", [
        (""),
        ("Д" * 41),
        ("Д" * 50)
    ])
    def test_add_new_book_invalid_number_not_added(self, book_name):
        collector = BooksCollector()
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid_genre_added(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_book_genre_valid_name_book_received(self):
        collector = BooksCollector()
        collector.add_new_book('Тайна Коко')
        collector.set_book_genre('Тайна Коко', 'Мультфильмы')
        assert collector.get_book_genre('Тайна Коко') == 'Мультфильмы'

    def test_get_books_genre_two_valid_name_book_received(self):
        collector = BooksCollector()
        collector.add_new_book('Тайна Коко')
        collector.add_new_book('Планета сокровищ')
        collector.set_book_genre('Тайна Коко', 'Мультфильмы')
        collector.set_book_genre('Планета сокровищ', 'Мультфильмы')
        books_genre = collector.get_books_genre()
        assert len(books_genre) == 2

    def test_get_books_with_specific_genre_returns_correct_list_when_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Планета сокровищ')
        collector.set_book_genre('Планета сокровищ', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Мультфильмы')

    @pytest.mark.parametrize("book_name, genre", [
        ("Тайна Коко", "Мультфильмы"),
        ("Дюна", "Фантастика"),
        ("Молодой человек", "Комедии")
    ])
    def test_get_books_for_children_valid_book_for_children_return(self, book_name, genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        expected_result = [book_name]
        assert books_collector.get_books_for_children() == expected_result

    @pytest.mark.parametrize("book_name, genre", [
        ("Ужасающий", "Ужасы"),
        ("Восточный экспресс", "Детективы")
    ])
    def test_get_books_for_children_invalid_book_for_children_not_return(self, book_name, genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        expected_result = []
        assert books_collector.get_books_for_children() == expected_result

    def test_add_book_in_favorites_one_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Тайна Коко')
        collector.add_book_in_favorites('Тайна Коко')
        assert 'Тайна Коко' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_exists_book_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Тайна Коко')
        collector.set_book_genre('Тайна Коко', 'Мультфильмы')
        collector.add_book_in_favorites('Тайна Коко')
        collector.delete_book_from_favorites('Тайна Коко')
        assert 'Тайна Коко' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_one_book_exists_returns_list_with_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тайна Коко')
        collector.set_book_genre('Тайна Коко', 'Мультфильмы')
        collector.add_book_in_favorites('Тайна Коко')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == "Тайна Коко"
