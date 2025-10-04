def squares_of_evens(numbers):
    result = []
    for num in numbers:
        if num % 2 == 1:  # ОШИБКА: проверка на нечётность!
            result.append(num ** 2)
    return result

print(squares_of_evens([1, 2, 3, 4, 5, 6]))  # Ожидаем [4, 16, 36], но получим [1, 9, 25]