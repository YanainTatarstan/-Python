{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4dd9b018",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.5\n"
     ]
    }
   ],
   "source": [
    "print(3/2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "83bb0330",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print (8//2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9b359bbc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> 2+4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e21a70cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print (2 + 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edbf863a",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 12\n",
    "b = a + 8\n",
    "print (\"12+8 =\", b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cc62ead9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите свое имя: Yana\n",
      "Yana\n"
     ]
    }
   ],
   "source": [
    "a = input (\"Введите свое имя: \")\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "e39c5500",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name: Yana\n",
      "Hello, Yana!\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter your name: \")\n",
    "print(\"Hello, %s!\" % name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1437bd99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Укажите ваш возраст: 28\n"
     ]
    }
   ],
   "source": [
    ">>> a = int(input(\"Укажите ваш возраст: \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c338b1d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите свой номер телефона: 89656224696\n"
     ]
    }
   ],
   "source": [
    ">>> b = input (\"Введите свой номер телефона: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ef042c9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Yana and you?\n"
     ]
    }
   ],
   "source": [
    ">>> a = \"Yana\"\n",
    ">>> b = \"and you?>>> print (\"My name is\", a, b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dbe87186",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name: Yana\n",
      "Enter your age: 28\n",
      "Enter any number: 89656224696\n",
      "Yana 28 89656224696.0\n"
     ]
    }
   ],
   "source": [
    "a = input(\"Enter your name: \")\n",
    "b = int(input(\"Enter your age: \"))\n",
    "c = float(input(\"Enter any number: \"))\n",
    "\n",
    "print (a, b, c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "10736bcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your local time in sec: 8785\n",
      "Now is 2:26:25 \n"
     ]
    }
   ],
   "source": [
    "time_in_sec = int(input(\"Enter your local time in sec: \"))\n",
    "hours = time_in_sec // 3600\n",
    "residue = time_in_sec % 3600\n",
    "minutes = residue // 60\n",
    "sec = residue % 60\n",
    "print (f\"Now is {hours}:{minutes}:{sec} \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "44bb5735",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите время в секундах: 1457652\n",
      "Это: 404 ч; 54 мин; 12 сек \n"
     ]
    }
   ],
   "source": [
    "time_in_sec = int(input(\"Введите время в секундах: \"))\n",
    "hours = time_in_sec // 3600\n",
    "residue = time_in_sec % 3600\n",
    "minutes = residue // 60\n",
    "sec = residue % 60\n",
    "print (f\"Это: {hours} ч; {minutes} мин; {sec} сек \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "428a9a7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите число n (от 1 до 10): 10\n",
      "Число n равно = 10; Сумма чисел n + nn + nnn равна = 102030\n"
     ]
    }
   ],
   "source": [
    "number_n = input (\"Введите число n (от 1 до 10): \")\n",
    "a = int (number_n + number_n)\n",
    "b = int (number_n + number_n + number_n)\n",
    "sum = int(number_n) + a + b\n",
    "print (f\"Число n равно = {number_n}; Сумма чисел n + nn + nnn равна = {sum}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "638dc87a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите целое число: 4578123564\n",
      "Самая большая цифра в числе:  8\n"
     ]
    }
   ],
   "source": [
    "number = input(\"Введите целое число: \")\n",
    "x = 0\n",
    "for i in number:\n",
    "    while int(i) > x:\n",
    "        x = int(i)\n",
    "print(\"Самая большая цифра в числе: \", x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "6dac5420",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите целое число: 123\n",
      "Самая большая цифра в числе  3\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Введите целое число: \"))\n",
    "max = n % 10\n",
    "while n >= 1:\n",
    "    n = n // 10\n",
    "    if n % 10 > max:\n",
    "        max = n % 10\n",
    "    if n > 9:\n",
    "        continue\n",
    "    else:\n",
    "        print(\"Самая большая цифра в числе \", max)\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "402b479d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите прибыль за квартал, руб.: 150000\n",
      "Введите убытки за квартал, руб.: 108000\n",
      "Отличная работа! Ваша рентабельность: 42000 руб.\n",
      "Введите численность всех работников компании: 4\n",
      "10500.0 прибыль в расчете на одного работника\n"
     ]
    }
   ],
   "source": [
    "profit = int(input(\"Введите прибыль за квартал, руб.: \"))\n",
    "loss = int(input(\"Введите убытки за квартал, руб.: \"))\n",
    "if profit > loss:\n",
    "    profitability = profit - loss\n",
    "    rent = profitability / profit\n",
    "    print(f\"Отличная работа! Ваша рентабельность: {profitability} руб.\")\n",
    "    worker = int(input(\"Введите численность всех работников компании: \"))\n",
    "    print(f\"{profitability/worker} прибыль в расчете на одного работника\")\n",
    "elif profit == loss:\n",
    "    print(\"Ваши доходы равны расходам. Обратите внимание! \")\n",
    "else:\n",
    "    print(\"Расходы привышают доходы. Необходимо проверить введённые данные, либо бухгалтерскую отчетность!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "6dc96d49",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите результат первого дня пробежки, км: 2\n",
      "Введите желаемый конечный результат, км: 6\n",
      "На 13 день Вы достигните желаемых результатов - не менее 6 км\n"
     ]
    }
   ],
   "source": [
    "a = float(input(\"Введите результат первого дня пробежки, км: \"))\n",
    "b = int(input(\"Введите желаемый конечный результат, км: \"))\n",
    "day_1 = 1\n",
    "if a > b:\n",
    "    print(day_1)\n",
    "while a < b:\n",
    "    a = a + a/10\n",
    "    day_1 += 1\n",
    "print(f\"На {day_1} день Вы достигните желаемых результатов - не менее {b} км\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5b8ed1b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
