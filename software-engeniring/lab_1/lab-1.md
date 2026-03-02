# Лабораторная 1

Автор: Титов Матвей ИУ7_22Б

## Оглавление

1. [Задачи](#1-задачи)
2. [Создание локального репозитория](#2-создание-локального-репозитория)
3. [Подготовка к работе](#3-подготовка-к-работе)
4. [Выполнение лабораторной работы](#4-выполнение-лабораторной-работы)
   1. [Назначение программы](#41-назначение-программы)
   2. [Поиск ошибки и её описание](#42-поиск-ошибки-и-её-описание)
   3. [Исправление ошибки](#43-исправление-ошибки)
   4. [Анализ истории](#44-анализ-истории)
   5. [Работа с wiki в gitlab](#45-работа-с-wiki-в-gitlab)

## 1. Задачи

Выполнение лабораторной работы включает следующие крупные шаги:

1. Чтение от начала и до конца методических указаний, проработка непонятных
моментов, подготовка плана выполнения лабораторной работы.
2. Создание локального репозитория; помещение исходной программы под версионный
контроль.
3. Разработка теста, для которого задача решается неверно; добавление теста к
программе; фиксация изменений.
4. Составление отчета (issue) об ошибке.
5. Исправление ошибки; фиксация изменений; закрытие отчета об ошибке.
6. Подготовка отчета о проделанной работе (с использованием wiki). Заполнение отчета
происходит в течение всего времени выполнения лабораторной работы

## 2. Создание локального репозитория

Проверяем, что находимся в "домашней папке".

```bash
matvei@DESKTOP-FF9K6EV:~$ pwd
/home/matvei
```

Создаем рабочую папку.

```bash
matvei@DESKTOP-FF9K6EV:~$ mkdir work

matvei@DESKTOP-FF9K6EV:~$ ls
bmstu  work
```

Переходим в рабочую папку.

```bash
matvei@DESKTOP-FF9K6EV:~$ cd work

matvei@DESKTOP-FF9K6EV:~/work$ pwd
/home/matvei/work
```

Создаем локальный репозиторий.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git init
Initialized empty Git repository in /home/matvei/work/.git/
```

Проверяем, что он создался.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ ls -a
.  ..  .git
```

## 3. Подготовка к работе

Проверим задано ли имя пользователя и e-mail.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git config --list
user.email=titovma3@student.bmstu.ru
user.name=titovma3
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
user.name=titovma3
```

Поместим в папку для выполнения лабораторной работы исходный код программы из
архива **src_1** с помощью **VS code**.

```bash
# Откроем WSL в VS Code.
matvei@DESKTOP-FF9K6EV:~/work$ code .
Updating VS Code Server to version c3a26841a84f20dfe0850d0a5a9bd01da4f003ea
Removing previous installation...
Installing VS Code Server for Linux x64 (c3a26841a84f20dfe0850d0a5a9bd01da4f003ea)
Downloading: 100%
Unpacking: 100%
Unpacked 3224 files and folders to /home/matvei/.vscode-server/bin/c3a26841a84f20dfe0850d0a5a9bd01da4f003ea.
Looking for compatibility check script at /home/matvei/.vscode-server/bin/c3a26841a84f20dfe0850d0a5a9bd01da4f003ea/bin/helpers/check-requirements.sh
Running compatibility check script
Compatibility check successful (0)
#  После этого перенесем файлы в WSL
```

Проверим, что файлы перенеслись.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ ls
iarray.py  main.py
```

Убедимся в том, что программа работает на тестовом примере.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ python3 main.py
Source
0 -1 3 -2 5
Result
0 3 5
```

Заметим, что создалась папка **\_\_pycache\_\_**, которая содержит байт-код Python.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ ls
__pycache__  iarray.py  main.py
```

Создадим .gitignore, чтобы не отслеживать __pycache__.

```bash
#  Создадим файл
matvei@DESKTOP-FF9K6EV:~/work$ touch .gitignore

matvei@DESKTOP-FF9K6EV:~/work$ ls -a
.  ..  .git  .gitignore  __pycache__  iarray.py  main.py
#  С помошью nano запишем **/__pycache__/** в .gitignore
matvei@DESKTOP-FF9K6EV:~/work$ nano .gitignore

#  Проверим результат записи
matvei@DESKTOP-FF9K6EV:~/work$ cat .gitignore
**/__pycache__/**
```

Добавим .gitignore для отслеживания, чтобы не отслеживался __pycache__.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        iarray.py
        main.py

nothing added to commit but untracked files present (use "git add" to track)

matvei@DESKTOP-FF9K6EV:~/work$ git add .gitignore

matvei@DESKTOP-FF9K6EV:~/work$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        iarray.py
        main.py

#  Зафиксируем изменения
matvei@DESKTOP-FF9K6EV:~/work$ git commit -m ".gitignore was added."
[master (root-commit) c6f28aa] .gitignore was added.
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore
 ```

Добавим под версионный контроль саму программу.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git add iarray.py main.py

#  Благодаря .gitignore папка __pycache__ проигнорирована
matvei@DESKTOP-FF9K6EV:~/work$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   iarray.py
        new file:   main.py

#  Зафиксируем изменения
matvei@DESKTOP-FF9K6EV:~/work$ git commit -m "Initial version of program was added."
[master 958a93b] Initial version of program was added.
 2 files changed, 49 insertions(+)
 create mode 100644 iarray.py
 create mode 100644 main.py
 ```

## 4. Выполнение лабораторной работы

### 4.1. Назначение программы

Программа предназначена для обработки и вывода числовых массивов.

#### Функции программы

Файл iarray.py содержит две функции:

* form_array - убирает из массива все отрицательные элементы;
* print_array - выводит все элементы массива.

Файл main.py содержит 2 функции:

* test_1 - создает тестовый массив;
* main - выводит тестовый массив с помощью print_array, обрабатывает его с помощью form_array и выводит потом новый массив с помощью print_array.

### 4.2. Поиск ошибки и её описание

Рассмотрим файл **iarray.py**.

```python
def form_array(arr, n):
  new_arr = arr

  i = 0
  while (i < n):
    if (new_arr[i] < 0):
      new_arr.pop(i)
      n -= 1
    
    i += 1
    
  return new_arr, n


def print_array(arr, n):
  i = 0
  while (i < n):
    print(arr[i], end = " ")
    i += 1
  
  print("")
```

#### Анализ ошибки

Используется метод **pop(i)**, который "выкидывает" элемент из списка, уменьшая индексы всех последующих элементов на 1. Пусть j-ый элемент \<0, тогда его "выкинет" и его место займет j+1-ый элемент. Мы проверили j-ый элемент, но j+1-ый элемент не проверим, т.к. мы увеличили индекс "проверяемого" элемента на 1 и убрали 1 элемент, т.е. будем проверять уже j+1 элемент.

#### Негативный тест

Можно отправить на обработку массив, где отрицательные элементы будут идти подряд.

Пример входных данных: `[-1, -2, -3, 0, 5, 6, -6, -7]`

Ожидаемый результат: `0 5 6`

Добавим новую тестовую функцию в файл **main.py**.

```python
def test_2():
  arr = list()
  
  arr.append(-1)
  arr.append(-2)
  arr.append(-3)
  arr.append(0)
  arr.append(5)
  arr.append(6)
  arr.append(-6)
  arr.append(-7)
  
  return arr, 8
```

Добавим тест в функцию **main()** в файле **main.py**.

```python
def main():
  
  print('Test 1')
  arr, n = test_1()

  print("Source")
  print_array(arr, n)
  
  new_arr, new_n = form_array(arr, n)

  print("Result")
  print_array(new_arr, new_n)
  print()

  print('Test 2')
  arr, n = test_2()

  print("Source")
  print_array(arr, n)
  
  new_arr, new_n = form_array(arr, n)

  print("Result")
  print_array(new_arr, new_n)
```

Проверим новый тест.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ python3 main.py
Test 1
Source
0 -1 3 -2 5
Result
0 3 5

Test 2
Source
-1 -2 -3 0 5 6 -6 -7
Result
-2 0 5 6 -7 #  !=0 5 6
```

Это подтверждает наличие ошибки в программе.

#### Анализ и фиксация изменений

Был изменен файл **main.py**.

```bash
matvei@DESKTOP-FF9K6EV:status ~/work$ git
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Изменения в файле **main.py**.

```bash
matvei@DESKTOP-FF9K6EV:diff ~/work$ git
diff --git a/main.py b/main.py
index 3a33132..e249dd9 100644
--- a/main.py
+++ b/main.py
@@ -11,7 +11,24 @@ def test_1():

   return arr, 5

+def test_2():^M
+  arr = list()^M
+  ^M
+  arr.append(-1)^M
+  arr.append(-2)^M
+  arr.append(-3)^M
+  arr.append(0)^M
+  arr.append(5)^M
+  arr.append(6)^M
+  arr.append(-6)^M
+  arr.append(-7)^M
+  ^M
+  return arr, 8^M
+^M
+^M
 def main():
+  ^M
+  ^M
+  ^M
+  ^M
+  print('Test 1')^M
   arr, n = test_1()

   print("Source")
@@ -21,7 +38,18 @@ def main():

   print("Result")
   print_array(new_arr, new_n)
+  print()^M
+  ^M
+  print('Test 2')^M
+  arr, n = test_2()^M

+  print("Source")^M
+  print_array(arr, n)^M
+  ^M
+  new_arr, new_n = form_array(arr, n)^M

+  print("Result")^M
+  print_array(new_arr, new_n)^M
+  ^M
 if __name__ == '__main__':
   main()
\ No newline at end of file
```

В первом блоке изменений, начиная с 11 строчки, было 7 строк, стало 24, добавилась функция **test_2()**. Во втором блоке изменений, начиная с 21 строчки, было 7 строк, стало, начиная с 38 строчки, 18, добавился Test 2.

Зафиксируем изменения.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")

matvei@DESKTOP-FF9K6EV:~/work$ git add main.py

matvei@DESKTOP-FF9K6EV:~/work$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   main.py

matvei@DESKTOP-FF9K6EV:~/work$ git commit -m "Test 2 was added."
[master e0a6ed7] Test 2 was added.
```

Номер ревизии **e0a6ed7**, комментарий **Test 2 was added.**.

### 4.3. Исправление ошибки

#### Исправление

Чтобы исправить ошибку, необходимо увеличивать "индекс проверяемого элемента" только в том случае, если только что проверенный элемент >=0. Для этого добавим **else** в функцию **form_array()**.

```python
def form_array(arr, n):
  new_arr = arr
  
  i = 0
  while (i < n):
    if (new_arr[i] < 0):
      new_arr.pop(i)
      n -= 1
    else:
      i += 1
    
  return new_arr, n
```

#### Тестирование

Запустим программу и проверим, решили ли мы ошибку.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ python3 main.py
Test 1
Source
0 -1 3 -2 5
Result
0 3 5

Test 2
Source
-1 -2 -3 0 5 6 -6 -7
Result
0 5 6 # the problem is solved
```

Ошибка исправлена.

#### Анализ и фиксирование изменений

Был изменен файл **main.py**.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   iarray.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Был добавлен **else** в функцию **form_array()**.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git diff
diff --git a/iarray.py b/iarray.py
index 63b016d..2a7308b 100644
--- a/iarray.py
+++ b/iarray.py
@@ -6,8 +6,8 @@ def form_array(arr, n):
     if (new_arr[i] < 0):
       new_arr.pop(i)
       n -= 1
-
-    i += 1
+    else:^M
+      i += 1^M

   return new_arr, n
```

Зафиксируем изменения.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git add iarray.py
matvei@DESKTOP-FF9K6EV:~/work$ git commit -m "fixed a bug"
[master 22530a4] fixed a bug
 1 file changed, 2 insertions(+), 2 deletions(-)
```

Номер ревизии **22530a4**.

### 4.4. Анализ истории

Команда **git log**.

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git log
commit 22530a4c877fb35ffb2c49d3ca788e0b2c08d4c7 (HEAD -> master)
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Wed Feb 18 22:15:57 2026 +0300

    fixed a bug

commit e0a6ed79dc9c9d474b0dec08127b9d3acdb2d24a
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Wed Feb 18 18:52:14 2026 +0300

    Test 2 was added.

commit 958a93bc97c33299900950702c61e2ceda8eb7c0
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Wed Feb 18 17:42:52 2026 +0300

    Initial version of program was added.

commit c6f28aaef9d7547a392635b78126e0dd25d9637f
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Wed Feb 18 17:37:51 2026 +0300

    .gitignore was added.
```

Выводится информация о "коммитах":

* Хэш коммита
* Автор
* Дата
* Описание изменений

Попробуем команду **git log** с параметром **--name-status**

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git log --name-status
commit 22530a4c877fb35ffb2c49d3ca788e0b2c08d4c7 (HEAD -> master)
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Wed Feb 18 22:15:57 2026 +0300

    fixed a bug

M       iarray.py

commit e0a6ed79dc9c9d474b0dec08127b9d3acdb2d24a
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Wed Feb 18 18:52:14 2026 +0300

    Test 2 was added.

M       main.py

commit 958a93bc97c33299900950702c61e2ceda8eb7c0
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Wed Feb 18 17:42:52 2026 +0300

    Initial version of program was added.

A       iarray.py
A       main.py

commit c6f28aaef9d7547a392635b78126e0dd25d9637f
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Wed Feb 18 17:37:51 2026 +0300

    .gitignore was added.

A       .gitignore
```

Добавилась информация о файлах, их изменении или создании.

Можно вывести историю не за весь период, а между двумя определенными ревизиями с помощью структуры `git log <commit1>..<commit2>`.

Пример:

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git log e0a6ed7..22530a4
commit 22530a4c877fb35ffb2c49d3ca788e0b2c08d4c7 (HEAD -> master)
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Wed Feb 18 22:15:57 2026 +0300

    fixed a bug
```

Сравнение одного и того же файла разных ревизий можно сделать с помощью структуры `git diff <commit1> <commit2> -- <файл>`

Пример:

```bash
matvei@DESKTOP-FF9K6EV:~/work$ git diff 958a93bc97c33299900950702c61e2ceda8eb7c0..22530a4 -- main.py
diff --git a/main.py b/main.py
index 3a33132..e249dd9 100644
--- a/main.py
+++ b/main.py
@@ -11,7 +11,24 @@ def test_1():

   return arr, 5

+def test_2():^M
+  arr = list()^M
+  ^M
+  arr.append(-1)^M
+  arr.append(-2)^M
+  arr.append(-3)^M
+  arr.append(0)^M
+  arr.append(5)^M
+  arr.append(6)^M
+  arr.append(-6)^M
+  arr.append(-7)^M
+  ^M
+  return arr, 8^M
+^M
+^M
 def main():
+  ^M
+  print('Test 1')^M
   arr, n = test_1()

   print("Source")
@@ -21,7 +38,18 @@ def main():

   print("Result")
   print_array(new_arr, new_n)
+  print()^M
+  ^M
+  print('Test 2')^M
+  arr, n = test_2()^M

+  print("Source")^M
+  print_array(arr, n)^M
+  ^M
+  new_arr, new_n = form_array(arr, n)^M

+  print("Result")^M
+  print_array(new_arr, new_n)^M
+  ^M
 if __name__ == '__main__':
   main()
\ No newline at end of file
```

### 4.5. Работа с wiki в GitLab

#### Как добавлять рисунки

Структура вставки: `![<Альтернативный текст>](<Ссылка на изображение>)`, где Альтернативный текст - текст, который появится вместо изображения, если оно не сможет загрузиться, Ссылка на изображение - путь до изображения на устройстве или URL-ссылка

Пример:
`![Бауманка](https://avatars.mds.yandex.net/get-altay/16113897/2a00000199b00e6fe320e20e17ab26cc46bf/L)`

![Бауманка](https://avatars.mds.yandex.net/get-altay/16113897/2a00000199b00e6fe320e20e17ab26cc46bf/L)

#### Как сделать оглавление

Для заголовка можно использовать список с ссылками на заголовки.

Пример:
```
## Оглавление

1. [Создание локального репозитория](#1-создание-локального-репозитория)
2. [Подготовка к работе](#2-подготовка-к-работе)
3. [Лабораторная работа](#4-выполнение-лабораторной-работы)
```

## Оглавление

1. [Создание локального репозитория](#1-создание-локального-репозитория)
2. [Подготовка к работе](#2-подготовка-к-работе)
3. [Лабораторная работа](#4-выполнение-лабораторной-работы)

#### Как добавить ссылки для перехода между страницами wiki

Ссылки на другие wiki страницы работают также, как ссылки на заголовки в оглавлении.

Пример относительной ссылки внутри одного репозитория: `[Главная страница](Home)`
Ссылки на другие страницы wiki: `[Часто задаваемые вопросы](FAQ)`


#### Как писать комментарии

Пример комментария в markdown: `<!-- Это комментарий -->`

Комментарии в блоках кода зависят от выбранного языка.

#### Стили оформления таблиц

`:---` — выравнивание по левому краю

`:---:` — выравнивание по центру

`---:` — выравнивание по правому краю

Пример:

```
| По левому краю | По центру  | По правому краю |
|:---------------|:----------:|----------------:|
| Текст слева    | Центр      | Текст справа    |
| Еще пример     | Пример     | 42              |
```

| По левому краю | По центру  | По правому краю |
|:---------------|:----------:|----------------:|
| Текст слева    | Центр      | Текст справа    |
| Еще пример     | Пример     | 42              |
