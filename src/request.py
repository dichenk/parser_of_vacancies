import classes
import time

new_elem = vacancy_text = vacancy_salary = vacancy_place_of_work = vacancy_experience = None
while 1:
    vacancy_text = input('Что ищем?\nВведите ключевую фразу:')
    while 1:
        try:
            vacancy_salary = input('Сколько денег?\nВведите целое число от 0 до 1000000: ')
            vacancy_salary = int(vacancy_salary)
            if 0 < vacancy_salary < 1000000:
                break
        except:
            pass
    while 1:
        vacancy_place_of_work = input('удаленка?\nВведите да или нет: ')
        if vacancy_place_of_work in ['да', 'нет']:
            break
    while 1:
        vacancy_experience = input('опыт?\nВведите число от 0 до 99: ')
        try:
            vacancy_experience = int(vacancy_experience)
            if 0 < vacancy_experience < 100:
                break
        except:
            pass

    new_elem = classes.Vacancy(vacancy_text)
    if new_elem.amount_of_vacancies == 0:
        print('\t\t\tНичего не найдено\nПереформулируйте ваш запрос!\n')
        continue
    
    break

new_elem.find_the_offer()



