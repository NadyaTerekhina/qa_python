from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

        # напиши свои тесты ниже
        # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_add_new_book_add_same_book_is_not_in_dic(self):
        #проверяем метод (аdd_new_book)
        #проверяем, что нельзя добавить книгу одну и ту же 2жды
        collector = BooksCollector()
        collector.add_new_book('Институт')
        collector.add_new_book('Институт')
        assert len(collector.get_books_rating()) == 1

    def test_add_new_book_default_raiting_is_one(self):
        # проверяем метод (аdd_new_book)
        # добавляем книгу и проверяем рейтинг по умолчанию - 1
        collector=BooksCollector()
        collector.add_new_book('Куджо')
        assert collector.get_book_rating('Куджо') == 1

    def test_set_book_rating_is_five(self):
        #проверяем метод (set_book_rating)
        #добавляем книгу и устанавливаем ей рейтинг 5, затем проверяем, что это 5
        # проверяем, что при вводе имени книги получаем рейтинг 5
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_rating('Оно',5)
        assert collector.get_book_rating('Оно') == 5

    def test_get_books_with_specific_rating_three_books_with_rating_three(self):
        # проверяем метод (get_books_with_specific_rating)
        #проверяем,  проверяем длину списка книг со спец.рейтингом 3 - 3 книги
        collector = BooksCollector()
        books = ['Кладбище домашних животных','Кристина','Сияние']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_rating(book,3)
            check = all(item in books for item in collector.get_books_with_specific_rating(3))
        assert check



    def test_add_book_in_favorites(self):
        # проверяем метод (add_book_in_favorites)
        # проверяем что книга в списке избранных
        collector = BooksCollector()
        collector.add_new_book('Под куполом')
        collector.add_book_in_favorites('Под куполом')
        assert 'Под куполом' in collector.get_list_of_favorites_books()



    def test_delete_book_from_favorites(self):
        # проверяем метод(delete_book_from_favorites)
        # проверяем, что удаленной книги нет в словаре
        collector = BooksCollector()
        collector.add_new_book('Долгая прогулка')
        collector.add_book_in_favorites('Долгая прогулка')
        collector.delete_book_from_favorites('Долгая прогулка')
        assert 'Долгая прогулка' not in collector.get_list_of_favorites_books()



    def test_get_books_rating(self):
        #проверяем, это словарь и что он не пустой
        collector = BooksCollector()
        collector.add_new_book('Чужак')
        assert type(collector.get_books_rating()) == dict
        assert collector.get_books_rating() != {}



    def test_get_list_of_favorites_books(self):
        # проверяем метод (get_list_of_favorites_books)
        # проверяем, что это список, что он не пустой
        collector = BooksCollector()
        collector.add_new_book('Керри')
        assert type(collector.get_list_of_favorites_books()) == list
        assert not collector.get_list_of_favorites_books()

































