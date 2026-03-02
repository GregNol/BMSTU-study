# Лабораторная 2

Автор: Титов Матвей ИУ7_22Б

## Оглавление

1. [Задание 1](#задание-1)
2. [Задание 2](#задание-2)
3. [Задание 3.1](#задание-31)
4. [Задание 3.2](#задание-32)
5. [Задание 3.3](#задание-33)

## Задание 1

### 1. Создали локальный репозиторий

### 2. Создали файл .gitignore

### 3. Скопировали файлы лабораторной

### 4. Создадим отдельную ветку fix

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git branch fix
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git switch fix
Switched to branch 'fix'
```

### 5. Добавим комментарии

Добавляем комментарии к функциям.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git status
On branch fix
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   iarray.py
        modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git add .
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git commit -m "Add comments for func"
[fix 6753b60] Add comments for func
 2 files changed, 16 insertions(+)
```

### 6. Добавим тест, демонстрирующий ошибку

Внесем изменения в файл **main.py**.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git diff
diff --git a/main.py b/main.py
index bf176a8..15df33a 100644
--- a/main.py
+++ b/main.py
@@ -13,16 +13,41 @@ def test_1():

   return arr, 4

+def test_2():^M
+  """^M
+  Тест 2^M
+  """^M
+  arr = list()^M
+  ^M
+  arr.append(9)^M
+  arr.append(8)^M
+  arr.append(7)^M
+  arr.append(6)^M
+  ^M
+  return arr, 4^M

 def main():
   """
   Прогонка тестов
   """
+  # Тест 1^M
+  print('Test 1')^M
+  ^M
   arr, n = test_1()

   print_array(arr, n)

   print("Max pos = " + str(get_max_pos(arr, n)))
+  print()^M
+  ^M
+  # Тест 2^M
+  print('Test 2')^M
+  ^M
+  arr, n = test_2()^M
+^M
+  print_array(arr, n)^M
+  ^M
+  print("Max pos = " + str(get_max_pos(arr, n)))^M
```

Подтвердим изменения.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git add main.py
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git commit -m "Add test_2"
[fix df6d2dc] Add test_2
 1 file changed, 25 insertions(+)
```

### 7. Создали issue

#### Негативный тест

Номер ревизии: **df6d2dc**

Входные данные: `[9, 8, 7, 6]` 

Ожидаемый результат: `9`

Фактический результат:

```bash
Traceback (most recent call last):
  File "main.py", line 54, in <module>
    main()
  File "main.py", line 50, in main
    print("Max pos = " + str(get_max_pos(arr, n)))
  File "/home/matvei/bmstu/labs_software_engineering/lab_2/src_2/iarray.py", line 19, in get_max_pos
    return j
UnboundLocalError: local variable 'j' referenced before assignment
```

### 8. Исправим ошибку

#### Анализ ошибки

При начальном выборе первого элемента как максимального мы не указываем **j=0**, из-за чего когда первый элемент является максимальным, переменная **j** не инициализируется => при её возврате появляется ошибка. 

#### Исправление ошибки

Добавим `j = 0`

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git diff
diff --git a/iarray.py b/iarray.py
index 090b7a1..06fd623 100644
--- a/iarray.py
+++ b/iarray.py
@@ -7,7 +7,8 @@ def get_max_pos(arr, n):
   return: индекс максиммального элемента
   """
   max = arr[0];
-
+  j = 0^M
+  ^M
   i = 1
   while (i < n):
     if (arr[i] > max):
```

Подтвердим изменения.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git add iarray.py
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git commit -m "Fix issue #2"
[fix 2e81309] Fix issue #2
 1 file changed, 2 insertions(+), 1 deletion(-)
```

Номер ревизии: **2e8130915c54441a50ab3506019a63ad5c9e2f61**

### 9. Добавим комментарий в issue с исправлением

### 10. Выполним объединение

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git switch master
Switched to branch 'master'
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git merge fix
Updating ecb6c08..2e81309
Fast-forward
 .gitignore |  2 +-
 iarray.py  | 13 ++++++++++++-
 main.py    | 31 +++++++++++++++++++++++++++++++
 3 files changed, 44 insertions(+), 2 deletions(-)
```

### 11. Закроем issue

### 12. Анализ истории

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/src_2$ git log --oneline --graph --all
* 2e81309 (HEAD -> master, fix) Fix issue #2
* df6d2dc Add test_2
* 6753b60 Add comments for func
* ecb6c08 Add .gitignore
* 8d3aca2 Project initialized
```

Конфликта не было, т.к. ветка **fix** содержит коммиты, напрямую продолжающие историю ветки, т.е. не было изменения главной ветки в процессе работы с веткой **fix**

## Задание 2

### Распаковка репозитория

Поместим в папку для выполнения лабораторной работы репозиторий small_fir.zip с помощью VS code.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2$ code .

# Переносим архив

#Проверяем его наличие
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2$ ls
small_fir.zip
```

Распакуем архив с помощью утилиты unzip

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2$ unzip small_fir.zip
Archive:  small_fir.zip
   creating: small_fir/.git/
   creating: small_fir/.git/branches/
 extracting: small_fir/.git/COMMIT_EDITMSG
  inflating: small_fir/.git/config
  inflating: small_fir/.git/description
 extracting: small_fir/.git/HEAD
   creating: small_fir/.git/hooks/
  inflating: small_fir/.git/hooks/applypatch-msg.sample
  inflating: small_fir/.git/hooks/commit-msg.sample
  inflating: small_fir/.git/hooks/post-update.sample
  inflating: small_fir/.git/hooks/pre-applypatch.sample
  inflating: small_fir/.git/hooks/pre-commit.sample
  inflating: small_fir/.git/hooks/prepare-commit-msg.sample
  inflating: small_fir/.git/hooks/pre-push.sample
  inflating: small_fir/.git/hooks/pre-rebase.sample
  inflating: small_fir/.git/hooks/pre-receive.sample
  inflating: small_fir/.git/hooks/update.sample
  inflating: small_fir/.git/index
   creating: small_fir/.git/info/
  inflating: small_fir/.git/info/exclude
   creating: small_fir/.git/logs/
  inflating: small_fir/.git/logs/HEAD
   creating: small_fir/.git/logs/refs/
   creating: small_fir/.git/logs/refs/heads/
  inflating: small_fir/.git/logs/refs/heads/develop
  inflating: small_fir/.git/logs/refs/heads/master
   creating: small_fir/.git/objects/
   creating: small_fir/.git/objects/12/
 extracting: small_fir/.git/objects/12/2ee3aeeea5f70e6a933bf0f4afbaa436e57b25
 extracting: small_fir/.git/objects/12/95f707870f0e1c13e9144b03cbef4bd10b52a7
   creating: small_fir/.git/objects/17/
 extracting: small_fir/.git/objects/17/4a840d4606e4c4da6f19cd2bbe43241800d3c6
   creating: small_fir/.git/objects/29/
 extracting: small_fir/.git/objects/29/dd977486586b4a4c8cbed83dfae05bcd5cbd84
   creating: small_fir/.git/objects/2c/
 extracting: small_fir/.git/objects/2c/605117c7fe0fc2452e787b44519f212ce48bcc
   creating: small_fir/.git/objects/4f/
 extracting: small_fir/.git/objects/4f/cbc684b3e8a22c172a218107bd669e0768b9f4
   creating: small_fir/.git/objects/77/
 extracting: small_fir/.git/objects/77/bf62b1125d36fd02ba686c1b5c563c0de10bf1
   creating: small_fir/.git/objects/7e/
 extracting: small_fir/.git/objects/7e/85de2c4933cf43354c7e121d455a105978de63
   creating: small_fir/.git/objects/85/
 extracting: small_fir/.git/objects/85/09e348f36bfd62cfb0fc59b87273bc1be55a87
   creating: small_fir/.git/objects/a5/
 extracting: small_fir/.git/objects/a5/16e3df14f364cfed07fd1c260246f0c1bfee54
 extracting: small_fir/.git/objects/a5/2c4ec45e14d5b48095e1bc9c569f06f4838362
 extracting: small_fir/.git/objects/a5/dc226e7e641a72ed9c8624948b557d813e2e6f
   creating: small_fir/.git/objects/aa/
 extracting: small_fir/.git/objects/aa/9041b1c18f3dbbc1fbe1fb22e9a8ea1bfc5480
   creating: small_fir/.git/objects/ab/
 extracting: small_fir/.git/objects/ab/49c101e38ef62b154180fa8ab2347b6c846ca0
   creating: small_fir/.git/objects/bb/
 extracting: small_fir/.git/objects/bb/b471f217bbf87ab9cb57bd4a86d93962e061f9
   creating: small_fir/.git/objects/e6/
 extracting: small_fir/.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391
   creating: small_fir/.git/objects/f7/
 extracting: small_fir/.git/objects/f7/39d2e40e87639a7fbb1d2a1333944164f879be
   creating: small_fir/.git/objects/f9/
 extracting: small_fir/.git/objects/f9/d8e65c356120d8ab13cd845ab0be8c6cdc332e
   creating: small_fir/.git/objects/info/
   creating: small_fir/.git/objects/pack/
   creating: small_fir/.git/refs/
   creating: small_fir/.git/refs/heads/
 extracting: small_fir/.git/refs/heads/develop
 extracting: small_fir/.git/refs/heads/master
   creating: small_fir/.git/refs/tags/
  inflating: small_fir/song.txt
```

Перейдем в папку репозитория.

```bash
# Проверим наличие папки
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2$ ls
small_fir  small_fir.zip

# Перейдем в папку
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2$ cd small_fir/

# Проверим, что есть .git
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ ls -a
.  ..  .git  song.txt
```

### Анализ истории изменений

#### Ветки

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git branch
  develop
* master
```

В этом репозитории 2 ветки **develop** и **master**. Мы находимся в ветке **master**

#### Пользователи

Посмотрим, кто редактировал репозиторий. Для этого вызовем команду `git log` с параметром `--all`, чтобы получить информацию о двух ветках сразу.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git log --all
commit a52c4ec45e14d5b48095e1bc9c569f06f4838362 (develop)
Author: Songster <songster@test>
Date:   Tue Mar 13 17:03:38 2018 +0300

    Couplets #5 and #6.

commit 1295f707870f0e1c13e9144b03cbef4bd10b52a7 (HEAD -> master)
Author: Minstrel <minstrel@test>
Date:   Tue Mar 13 17:01:15 2018 +0300

    Couplet #4.

commit 4fcbc684b3e8a22c172a218107bd669e0768b9f4
Author: Minstrel <minstrel@test>
Date:   Tue Mar 13 17:00:30 2018 +0300

    Couplet #3.

commit 2c605117c7fe0fc2452e787b44519f212ce48bcc
Author: Songster <songster@test>
Date:   Tue Mar 13 16:59:09 2018 +0300

    Couplet #2.

commit 122ee3aeeea5f70e6a933bf0f4afbaa436e57b25
Author: Minstrel <minstrel@test>
Date:   Tue Mar 13 16:57:10 2018 +0300

    Couplet #1.

commit f739d2e40e87639a7fbb1d2a1333944164f879be
Author: Minstrel <minstrel@test>
Date:   Tue Mar 13 16:50:47 2018 +0300

    Beginning.

[3]+  Stopped                 git log --all
```

Ветку **master** редактировал 1 пользователь **Minstrel** с почтой **minstrel@test**.
Ветку **develop** редактировали 2 пользователя **Songster** с почтой **songster@test** и **Minstrel** с почтой **minstrel@test**.

Итого, в репозитории 2 пользователя.

#### Файлы

Для получения списка файлов воспользуемся командой `git log --name-only --all --oneline`, где:

* `--name-only` - параметр для вывода имен измененных файлов;
* `--all` - выводит информацию по всем веткам;
* `--oneline` - убирает лишнюю информацию про коммиты.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git log --name-only --all --oneline
a52c4ec (develop) Couplets #5 and #6.
song.txt
1295f70 (HEAD -> master) Couplet #4.
song.txt
4fcbc68 Couplet #3.
song.txt
2c60511 Couplet #2.
song.txt
122ee3a Couplet #1.
song.txt
f739d2e Beginning.
song.txt
```

Видим, что во всех коммитах редактировали только один файл **song.txt**.

Для получения очередности вносимых изменений воспользуемся командой `git log --graph --all --name-only`, где `--graph` выводит логи в виде графа.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git log --graph --all --name-only
* commit a52c4ec45e14d5b48095e1bc9c569f06f4838362 (develop)
| Author: Songster <songster@test>
| Date:   Tue Mar 13 17:03:38 2018 +0300
|
|     Couplets #5 and #6.
|
| song.txt
|
* commit 2c605117c7fe0fc2452e787b44519f212ce48bcc
| Author: Songster <songster@test>
| Date:   Tue Mar 13 16:59:09 2018 +0300
|
|     Couplet #2.
|
| song.txt
|
| * commit 1295f707870f0e1c13e9144b03cbef4bd10b52a7 (HEAD -> master)
| | Author: Minstrel <minstrel@test>
| | Date:   Tue Mar 13 17:01:15 2018 +0300
| |
| |     Couplet #4.
| |
| | song.txt
| |
| * commit 4fcbc684b3e8a22c172a218107bd669e0768b9f4
| | Author: Minstrel <minstrel@test>
| | Date:   Tue Mar 13 17:00:30 2018 +0300
| |
| |     Couplet #3.
| |
| | song.txt
| |
| * commit 122ee3aeeea5f70e6a933bf0f4afbaa436e57b25
|/  Author: Minstrel <minstrel@test>
|   Date:   Tue Mar 13 16:57:10 2018 +0300
|
|       Couplet #1.
|
|   song.txt
|
* commit f739d2e40e87639a7fbb1d2a1333944164f879be
  Author: Minstrel <minstrel@test>
  Date:   Tue Mar 13 16:50:47 2018 +0300

      Beginning.

  song.txt
```

Видим, что изначально **Minstrel** инициализировал файл **song.txt** в ветке **develop**.
После чего **Minstrel** создал ветку **master**. и внес изменения в ней.
Потом **Songster** внес изменения в ветке **develop**.

#### Слияение ветвей

Для слияние ветки **develop** в **master**, необходимо перейти в ветку **master** и использовать команду `git merge develop`.

```bash
# Перейдем в ветку master
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git switch master
Already on 'master'

# Проверим ветку
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git status
On branch master
nothing to commit, working tree clean

# Попробуем провести слияние
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git merge develop
Auto-merging song.txt
CONFLICT (content): Merge conflict in song.txt
Automatic merge failed; fix conflicts and then commit the result.
# Ошибка слияния

# song.txt стал unmerged
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   song.txt
```

Откроем файл song.txt и посмотрим конфликт.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ cat song.txt
<<<<<<< HEAD
В лесу родилась ёлочка,
В лесу она росла.
Зимой и летом стройная,
Зелёная была.

Трусишка зайка серенький
Под ёлочкой скакал.
Порою волк, сердитый волк,
Рысцою пробегал.

Чу! Снег по лесу частому
Под полозом скрипит.
Лошадка мохноногая
Торопится, бежит.
=======
Метель ей пела песенку:
«Спи, ёлочка, бай-бай!»
Мороз снежком укутывал:
«Смотри, не замерзай!»

Везёт лошадка дровенки,
На дровнях - мужичок
Срубил он нашу ёлочку
Под самый корешок.

Теперь она, нарядная,
На праздник к нам пришла,
И много, много радости
Детишкам принесла.
>>>>>>> develop
```

Видим, что куплеты перемешались, чтобы восстановить правильную последовательность воспользуемся командой `git log -p --all --reverse`

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git log -p --all --reverse
commit f739d2e40e87639a7fbb1d2a1333944164f879be
Author: Minstrel <minstrel@test>
Date:   Tue Mar 13 16:50:47 2018 +0300

    Beginning.

diff --git a/song.txt b/song.txt
new file mode 100644
index 0000000..e69de29

commit 122ee3aeeea5f70e6a933bf0f4afbaa436e57b25
Author: Minstrel <minstrel@test>
Date:   Tue Mar 13 16:57:10 2018 +0300

    Couplet #1.

diff --git a/song.txt b/song.txt
index e69de29..a5dc226 100644
--- a/song.txt
+++ b/song.txt
@@ -0,0 +1,4 @@
+В лесу родилась ёлочка,^M
+В лесу она росла.^M
+Зимой и летом стройная,^M
+Зелёная была.^M

commit 2c605117c7fe0fc2452e787b44519f212ce48bcc
Author: Songster <songster@test>
Date:   Tue Mar 13 16:59:09 2018 +0300

    Couplet #2.

diff --git a/song.txt b/song.txt
index e69de29..174a840 100644
--- a/song.txt
+++ b/song.txt
@@ -0,0 +1,4 @@
+Метель ей пела песенку:^M
+«Спи, ёлочка, бай-бай!»^M
+Мороз снежком укутывал:^M
+«Смотри, не замерзай!»^M

commit 4fcbc684b3e8a22c172a218107bd669e0768b9f4
Author: Minstrel <minstrel@test>
Date:   Tue Mar 13 17:00:30 2018 +0300

    Couplet #3.

diff --git a/song.txt b/song.txt
index a5dc226..a516e3d 100644
--- a/song.txt
+++ b/song.txt
@@ -2,3 +2,8 @@
 В лесу она росла.
 Зимой и летом стройная,
 Зелёная была.
+^M
+Трусишка зайка серенький^M
+Под ёлочкой скакал.^M
+Порою волк, сердитый волк,^M
+Рысцою пробегал.^M

commit 1295f707870f0e1c13e9144b03cbef4bd10b52a7 (HEAD -> master)
Author: Minstrel <minstrel@test>
Date:   Tue Mar 13 17:01:15 2018 +0300

    Couplet #4.

diff --git a/song.txt b/song.txt
index a516e3d..ab49c10 100644
--- a/song.txt
+++ b/song.txt
@@ -7,3 +7,8 @@
 Под ёлочкой скакал.
 Порою волк, сердитый волк,
 Рысцою пробегал.
+^M
+Чу! Снег по лесу частому^M
+Под полозом скрипит.^M
+Лошадка мохноногая^M
+Торопится, бежит.^M

commit a52c4ec45e14d5b48095e1bc9c569f06f4838362 (develop)
Author: Songster <songster@test>
Date:   Tue Mar 13 17:03:38 2018 +0300

    Couplets #5 and #6.

diff --git a/song.txt b/song.txt
index 174a840..7e85de2 100644
--- a/song.txt
+++ b/song.txt
@@ -2,3 +2,13 @@
 «Спи, ёлочка, бай-бай!»
 Мороз снежком укутывал:
 «Смотри, не замерзай!»
+^M
+Везёт лошадка дровенки,^M
+На дровнях - мужичок^M
+Срубил он нашу ёлочку^M
+Под самый корешок.^M
+^M
+Теперь она, нарядная,^M
+На праздник к нам пришла,^M
+И много, много радости^M
+Детишкам принесла.^M
```

Изменим вручную файл **song.txt**, исходя из последовательности добавления куплетов.

Результат:

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ cat song.txt
В лесу родилась ёлочка,
В лесу она росла.
Зимой и летом стройная,
Зелёная была.

Метель ей пела песенку:
«Спи, ёлочка, бай-бай!»
Мороз снежком укутывал:
«Смотри, не замерзай!»

Трусишка зайка серенький
Под ёлочкой скакал.
Порою волк, сердитый волк,
Рысцою пробегал.

Чу! Снег по лесу частому
Под полозом скрипит.
Лошадка мохноногая
Торопится, бежит.

Везёт лошадка дровенки,
На дровнях - мужичок
Срубил он нашу ёлочку
Под самый корешок.

Теперь она, нарядная,
На праздник к нам пришла,
И много, много радости
Детишкам принесла.
```

Завершим слияние.

```bash
# Проверим статус
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   song.txt

no changes added to commit (use "git add" and/or "git commit -a")

# добавим файл для отслеживания
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git add song.txt

# Проверим
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git status
On branch master
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   song.txt

# Подтверждим изменения
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git commit -m "Merge with develop"
[master bf28ccd] Merge with develop

# Проверим
matvei@DESKTOP-FF9K6EV:~/bmstu/labs_software_engineering/lab_2/small_fir$ git status
On branch master
nothing to commit, working tree clean
```

## Заданиеи 3

### Задание 3.1

Merge request создан.
[Ссылка на MR](https://git.iu7.bmstu.ru/iu7-cprog/iu7-cprog-labs-2026/iu7-cprog-labs-2026-titovma3/-/merge_requests/1)

### Задание 3.2

#### 1. Копия удаленного репозитория была получена раннее, рабочая директория переименованна в software-engineering для удобства

#### 2. Перейдем в рабочую директорию

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu$ ls
cprog  labs_software_engineering  ptp  software-engineering

matvei@DESKTOP-FF9K6EV:~/bmstu$ cd software-engineering/

matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ pwd
/home/matvei/bmstu/software-engineering
```

#### 3. Создадим 2 дополнительные ветви

```bash
# Создадим ветки
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git branch lab_02_a
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git branch lab_02_b

# Проверим создались ли они
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git branch
  lab_02_a
  lab_02_b
* main
```

#### 4. Переключим ветку на lab_02_a

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git switch lab_02_a
Switched to branch 'lab_02_a'
```

#### 5. Добавим файлы lab_02_a и .gitignore

```bash
# Создадим файл
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ echo "lab_02_a" > lab_02_a.txt

# Добавим файл под версионный контроль
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git add lab_02_a.txt
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git commit -m "Add lab_02_a.txt"
[lab_02_a d63d9cb] Add lab_02_a.txt
 1 file changed, 1 insertion(+)
 create mode 100644 lab_02_a.txt

# Создадим файл
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ echo "*.exe" > .gitignore

# Добавим файл под версионный контроль
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git add .gitignore
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git commit -m "Add .gitignore"
[lab_02_a 18d0008] Add .gitignore
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore
```

#### 6. Отправим изменения

```bash
# Отправляем изменения
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git push --set-upstream origin lab_02_a
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 579 bytes | 193.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
remote:
remote: To create a merge request for lab_02_a, visit:
remote:   https://git.iu7.bmstu.ru/iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3/-/merge_requests/new?merge_request%5Bsource_branch%5D=lab_02_a
remote:
To git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3.git
 * [new branch]      lab_02_a -> lab_02_a
Branch 'lab_02_a' set up to track remote branch 'lab_02_a' from 'origin'.
```

Merge Request создается в GitLab.
[Ссылка на MR](https://git.iu7.bmstu.ru/iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3/-/merge_requests/2)

#### 7. Переключимся на ветку lab_02_b

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git switch lab_02_b
Switched to branch 'lab_02_b'
```

#### 8. Добавим файлы lab_02_b и .gitignore

```bash
# Создадим файл
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ echo "lab_02_b" > lab_02_b.txt

# Добавим файл под версионный контроль
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git commit -m "Add lab_02_b.txt"
[lab_02_b df4f2cb] Add lab_02_b.txt
 1 file changed, 1 insertion(+)
 create mode 100644 lab_02_b.txt

# Создадим файл
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ echo "*.o" > .gitignore

# Добавим файл под версионный контроль
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git add .gitignore
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git commit -m "Add .gitignore"
[lab_02_b c715354] Add .gitignore
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore
```

#### 9. Отправим изменения

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git push --set-upstream origin lab_02_b
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 579 bytes | 289.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
remote:
remote: To create a merge request for lab_02_b, visit:
remote:   https://git.iu7.bmstu.ru/iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3/-/merge_requests/new?merge_request%5Bsource_branch%5D=lab_02_b
remote:
To git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3.git
 * [new branch]      lab_02_b -> lab_02_b
Branch 'lab_02_b' set up to track remote branch 'lab_02_b' from 'origin'.
```

Merge Request создается в GitLab.
[Ссылка на MR](https://git.iu7.bmstu.ru/iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3/-/merge_requests/2)

#### 10. Просим преподавателя принять MR B

#### 11. Анализ MR A

Видим ошибку на файл **.gitignore**:

`Conflict: This file was added both in the source and target branches, but with different contents. Ask someone with write access to resolve it.`

Файл .gitignore был передан в ветку **main** при слиянии с веткой **lab_02_b**, из-за чего при попытке добавить его ветки **lab_02_a** возникает ошибка, т.к. файл иницилизирован в обеих ветках, но при этом имеет разное содержание.

#### 12. Исправляем конфликт

Переключимся на ветку **lab_02_a**.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git switch lab_02_a
Switched to branch 'lab_02_a'
Your branch is up to date with 'origin/lab_02_a'.
```

Загрузим все изменения из удаленного репозитория.

```bash
git fetch
```

Пересоберем нашу ветку относительно **main**.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git rebase origin/main
First, rewinding head to replay your work on top of it...
Applying: Add lab_02_a.txt
Applying: Add .gitignore
Using index info to reconstruct a base tree...
Falling back to patching base and 3-way merge...
CONFLICT (add/add): Merge conflict in .gitignore
Auto-merging .gitignore
error: Failed to merge in the changes.
Patch failed at 0002 Add .gitignore
hint: Use 'git am --show-current-patch' to see the failed patch
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
```

Видим ошибку о слиянии файла **.gitignore**.

Просмотрим содержимое файла.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ cat .gitignore
<<<<<<< HEAD
*.o
=======
*.exe
>>>>>>> Add .gitignore
```

Видим ошибку слияния, исправим её вручную, заменив содержимое файла на:

```txt
*.exe
*.o
```

Добавим изменения.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git add .gitignore
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git rebase --continue
Applying: Add .gitignore
```

Отправим изменения на удаленный репозиторий.

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git push
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (8/8), 936 bytes | 468.00 KiB/s, done.
Total 8 (delta 1), reused 0 (delta 0)
remote:
remote: View merge request for lab_02_a:
remote:   https://git.iu7.bmstu.ru/iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3/-/merge_requests/1
remote:
To git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3.git
   18d0008..2177c5d  lab_02_a -> lab_02_a
```

Конфликт MR исправлен.

#### 13. История изменения

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git log --graph --all
*   commit 2177c5d4b24070bb34eacd55c8aba4d625f62bad (HEAD -> lab_02_a, origin/lab_02_a)
|\  Merge: 580c194 18d0008
| | Author: titovma3 <titovma3@student.bmstu.ru>
| | Date:   Thu Feb 26 00:31:09 2026 +0300
| |
| |     Fix merge conflict
| |
| * commit 18d00088e4460c61f8f86bbb9b51879005c8a4f3
| | Author: titovma3 <titovma3@student.bmstu.ru>
| | Date:   Wed Feb 25 00:09:16 2026 +0300
| |
| |     Add .gitignore
| |
| * commit d63d9cb445b857473d7f12831cdb097007925baf
| | Author: titovma3 <titovma3@student.bmstu.ru>
| | Date:   Wed Feb 25 00:07:53 2026 +0300
| |
| |     Add lab_02_a.txt
| |
* | commit 580c19468d8730106b41202a993faf2beb39614a
| | Author: titovma3 <titovma3@student.bmstu.ru>
| | Date:   Wed Feb 25 00:09:16 2026 +0300
| |
| |     Add .gitignore
| |
* | commit aa7a5d46a864d6c449ee722f6f443e309da84309
| | Author: titovma3 <titovma3@student.bmstu.ru>
| | Date:   Wed Feb 25 00:07:53 2026 +0300
| |
| |     Add lab_02_a.txt
| |
* |   commit bbf2be977c5301ec56ad765d07b1be19e2c03ed5 (origin/main, origin/HEAD, main)
|\ \  Merge: f53d11e c715354
| |/  Author: Marina Baryshnikova <baryshnikovam@mail.ru>
|/|   Date:   Wed Feb 25 09:59:19 2026 +0000
| |
| |       Merge branch 'lab_02_b' into 'main'
| |
| |       Lab_02 B
| |
| |       See merge request iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3!2
| |
| * commit c715354955369d41cb0ef281e37da0f1ea733405 (origin/lab_02_b, lab_02_b)
| | Author: titovma3 <titovma3@student.bmstu.ru>
| | Date:   Wed Feb 25 00:35:13 2026 +0300
| |
| |     Add .gitignore
| |
| * commit df4f2cbdb4601e8e202b1268056ea3ab09be69d5
|/  Author: titovma3 <titovma3@student.bmstu.ru>
|   Date:   Wed Feb 25 00:34:10 2026 +0300
|
|       Add lab_02_b.txt
|
* commit f53d11e429c235ce142d061802f53a77a0c87346
  Author: Alexander Kostritsky <alexodnodvorcev@bmstu.ru>
  Date:   Thu Feb 12 21:26:01 2026 +0300

      Add README.md
```

Видим, что была создана ветка **lab_02_b**, добавлены файлы, после чего ветка была слита в **main**.
Также была создана ветка **lab_02_a**, добавлены файлы, исправлен конфликт слияние, отправлен MR на слияние.

### Задание 3.3

#### 1. Копия удаленного репозитория была получена раннее, локальный реп-ий был переименов для удобства

#### 2. Уже находимся в рабочей репозитории

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ pwd
/home/matvei/bmstu/software-engineering
```

#### 3. Создаем ветвь lab_02_c

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git branch lab_02_c

matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git switch lab_02_c
Switched to branch 'lab_02_c'

matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git status
On branch lab_02_c
nothing to commit, working tree clean
```

#### 4. Создадим текстовый файл с абзацем #1

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ touch song.txt

matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ nano song.txt
# Добавляем текст в файл

# Добавляем под версионный контроль
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git add song.txt
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git commit -m "Add song.txt"
[lab_02_c f9274a1] Add song.txt
 1 file changed, 9 insertions(+)
 create mode 100644 song.txt
```

#### 5. Отправим изменения

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git push --set-upstream origin lab_02_c
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 407 bytes | 407.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote:
remote: To create a merge request for lab_02_c, visit:
remote:   https://git.iu7.bmstu.ru/iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3/-/merge_requests/new?merge_request%5Bsource_branch%5D=lab_02_c
remote:
To git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3.git
 * [new branch]      lab_02_c -> lab_02_c
Branch 'lab_02_c' set up to track remote branch 'lab_02_c' from 'origin'.

#Посмотрим, как выглядит файл
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ cat song.txt
Вот оно какое, наше лето,
Лето яркой зеленью одето,
Лето жарким солнышком согрето,
Дышит лето ветерком.

Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля-ля-ля.
Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля!
```

#### 6. Добавими абзац #3

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ nano  song.txt
# Добавляем третий абзац

matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git status
On branch lab_02_c
Your branch is up to date with 'origin/lab_02_c'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   song.txt

no changes added to commit (use "git add" and/or "git commit -a")

# Добавим изменения под версионный контроль
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git add song.txt

# Подтвердим изменения
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git commit -m "Add part #3 of song to song.txt"
[lab_02_c d309d6f] Add part #3 of song to song.txt
 1 file changed, 10 insertions(+)

# Посмотрим как выглядит файл
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ cat song.txt
Вот оно какое, наше лето,
Лето яркой зеленью одето,
Лето жарким солнышком согрето,
Дышит лето ветерком.

Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля-ля-ля.
Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля!

Мы покрыты бронзовым загаром,
Ягоды в лесу горят пожаром.
Лето это жаркое недаром,
Лето — это хорошо!

Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля-ля-ля.
Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля!
```

#### 7. Создадим еще одну копию удаленного репозитория

```bash
# Скопируем удаленный репозиторий в другую папку
matvei@DESKTOP-FF9K6EV:~/bmstu$ git clone gitlab@git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3.git
Cloning into 'iu7-software-engineering-labs-2026-titovma3'...
remote: Enumerating objects: 27, done.
remote: Counting objects: 100% (24/24), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 27 (delta 3), reused 0 (delta 0), pack-reused 3 (from 1)
Receiving objects: 100% (27/27), done.
Resolving deltas: 100% (3/3), done.

# Проверим создалась ли копия
matvei@DESKTOP-FF9K6EV:~/bmstu$ ls -a
.  ..  cprog  iu7-software-engineering-labs-2026-titovma3  labs_software_engineering  ptp  software-engineering

# Переименуем её для удобства
matvei@DESKTOP-FF9K6EV:~/bmstu$ mv iu7-software-engineering-labs-2026-titovma3/ se_lab_02_c

# Проверим изменения
matvei@DESKTOP-FF9K6EV:~/bmstu$ ls
cprog  labs_software_engineering  ptp  se_lab_02_c  software-engineering

# Перейдем в директорию
matvei@DESKTOP-FF9K6EV:~/bmstu$ cd se_lab_02_c/

# Проверим содержимое
matvei@DESKTOP-FF9K6EV:~/bmstu/se_lab_02_c$ ls -a
.  ..  .git  .gitignore  README.md  lab_02_b.txt
```

#### 8. Переключимся на ветку lab_02_c

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/se_lab_02_c$ git switch lab_02_c
Branch 'lab_02_c' set up to track remote branch 'lab_02_c' from 'origin'.
Switched to a new branch 'lab_02_c'

# Проверим
matvei@DESKTOP-FF9K6EV:~/bmstu/se_lab_02_c$ git status
On branch lab_02_c
Your branch is up to date with 'origin/lab_02_c'.

nothing to commit, working tree clean
```

#### 9. Добавим абзац #2

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/se_lab_02_c$ nano song.txt
# Добавим абзац #2

# Проверим содержимое файла
matvei@DESKTOP-FF9K6EV:~/bmstu/se_lab_02_c$ cat song.txt
Вот оно какое, наше лето,
Лето яркой зеленью одето,
Лето жарким солнышком согрето,
Дышит лето ветерком.

Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля-ля-ля.
Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля!

На зеленой солнечной опушке
Прыгают зеленые лягушки,
И танцуют бабочки-подружки,
Расцветает все кругом.

Мы в дороге с песенкой о лете,
Самой лучшей песенкой на свете,
Мы в лесу ежа, быть может, встретим,
Хорошо, что дождь прошел.

Ля-ля-ля ля-ля-ля,
Ля-ля-ля ля-ля-ля-ля.

# Подтвердим изменения
matvei@DESKTOP-FF9K6EV:~/bmstu/se_lab_02_c$ git add song.txt
matvei@DESKTOP-FF9K6EV:~/bmstu/se_lab_02_c$ git commit -m "Add part #2 of song to song.txt"
[lab_02_c 7f89da6] Add part #2 of song to song.txt
 1 file changed, 13 insertions(+)

# Отправим изменения на удаленный репозиторий
matvei@DESKTOP-FF9K6EV:~/bmstu/se_lab_02_c$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 601 bytes | 601.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote:
remote: To create a merge request for lab_02_c, visit:
remote:   https://git.iu7.bmstu.ru/iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3/-/merge_requests/new?merge_request%5Bsource_branch%5D=lab_02_c
remote:
To git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3.git
   f9274a1..7f89da6  lab_02_c -> lab_02_c
```


#### 10. Перейдем в первую копию реп-ия

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/se_lab_02_c$ cd ../
matvei@DESKTOP-FF9K6EV:~/bmstu$ cd software-engineering/
```

#### 11. Попытаемся отправить изменения в удаленный репозиторий

```bash
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git push
To git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3.git
 ! [rejected]        lab_02_c -> lab_02_c (fetch first)
error: failed to push some refs to 'gitlab@git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

Видим ошибку, которая сообщает, что на удаленном репозитории есть изменения, которых нет у нас локально.

#### 12. Исправляем ошибку

Для исправления, подгрузим изменения с удаленного репозитория с помощью `git pull`. После чего исправим конфликт локально и отправим результат на удаленный реп-ий.

```bash
# Подгрузим изменения
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 576 bytes | 288.00 KiB/s, done.
From git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3
   f9274a1..7f89da6  lab_02_c   -> origin/lab_02_c
Auto-merging song.txt
CONFLICT (content): Merge conflict in song.txt
Automatic merge failed; fix conflicts and then commit the result.
# Видим ошибку слияние в song.txt

# Посмотрим содержимое файла song.txt
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ cat song.txt
Вот оно какое, наше лето,
Лето яркой зеленью одето,
Лето жарким солнышком согрето,
Дышит лето ветерком.

Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля-ля-ля.
Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля!

<<<<<<< HEAD
Мы покрыты бронзовым загаром,
Ягоды в лесу горят пожаром.
Лето это жаркое недаром,
Лето — это хорошо!

Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля-ля-ля.
Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля!
=======
На зеленой солнечной опушке
Прыгают зеленые лягушки,
И танцуют бабочки-подружки,
Расцветает все кругом.

Мы в дороге с песенкой о лете,
Самой лучшей песенкой на свете,
Мы в лесу ежа, быть может, встретим,
Хорошо, что дождь прошел.

Ля-ля-ля ля-ля-ля,
Ля-ля-ля ля-ля-ля-ля.
>>>>>>> 7f89da6dc1b68bdd2e99d00325fc2a64b5befd72
# Видим ошибку во втором абзаце

# Вручную объеденим абзацы
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ nano song.txt

# Проверим содержимое
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ cat song.txt
Вот оно какое, наше лето,
Лето яркой зеленью одето,
Лето жарким солнышком согрето,
Дышит лето ветерком.

Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля-ля-ля.
Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля!

На зеленой солнечной опушке
Прыгают зеленые лягушки,
И танцуют бабочки-подружки,
Расцветает все кругом.

Мы в дороге с песенкой о лете,
Самой лучшей песенкой на свете,
Мы в лесу ежа, быть может, встретим,
Хорошо, что дождь прошел.

Ля-ля-ля ля-ля-ля,
Ля-ля-ля ля-ля-ля-ля.

Мы покрыты бронзовым загаром,
Ягоды в лесу горят пожаром.
Лето это жаркое недаром,
Лето — это хорошо!

Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля-ля-ля.
Ля-ля-ля ля-ля-ля,
Ля-ля-ля-ля-ля ля-ля!

# Добавим файл под версионный контроль
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git add song.txt

# Проверим
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git status
On branch lab_02_c
Your branch and 'origin/lab_02_c' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   song.txt

# Подтвердим изменения
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git commit -m "Fix merge conflict"
[lab_02_c 8137a06] Fix merge conflict

# Проверим
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git status
On branch lab_02_c
Your branch is ahead of 'origin/lab_02_c' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

# Отправим изменения на удаленный репозиторий
matvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git push
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 689 bytes | 344.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0)
remote:
remote: To create a merge request for lab_02_c, visit:
remote:   https://git.iu7.bmstu.ru/iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3/-/merge_requests/new?merge_request%5Bsource_branch%5D=lab_02_c
remote:
To git.iu7.bmstu.ru:iu7-software-engineering/iu7-software-engineering-labs-2026/iu7-software-engineering-labs-2026-titovma3.git
   7f89da6..8137a06  lab_02_c -> lab_02_c
```

#### 13. Аналитика изменений

```bash
atvei@DESKTOP-FF9K6EV:~/bmstu/software-engineering$ git log
commit 8137a068f8bdf3b36574f42f1c234e66011852b4 (HEAD -> lab_02_c, origin/lab_02_c)
Merge: d309d6f 7f89da6
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Thu Feb 26 01:15:02 2026 +0300

    Fix merge conflict

commit 7f89da6dc1b68bdd2e99d00325fc2a64b5befd72
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Thu Feb 26 01:04:35 2026 +0300

    Add part #2 of song to song.txt

commit d309d6fafeccbf9821d5776f89670080111ff6b8
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Thu Feb 26 00:55:09 2026 +0300

    Add part #3 of song to song.txt

commit f9274a19868b0dce7bb4f2c033bb50d535295ef7
Author: titovma3 <titovma3@student.bmstu.ru>
Date:   Thu Feb 26 00:52:10 2026 +0300

    Add song.txt
```

После инициализации ветки, добавил в неё файл **song.txt** с абзацем #1.
Добавил абзац #3.
Добавил абзац #2.
Исправил конфликт слияния **song.txt** между двумя копиями удаленного репозитория.

#### 14. Последовательность действий по времени

* Т00 - создал ветку **lab_02_c**
* Т01 - добавил файл **song.txt** с абзацем #1 песни
* Т02 - зафиксировал изменения в локальном репозитории
* Т03 - отправил изменения в удаленный репозиторий
* Т04 - добавил в файл **song.txt** абзац #3 песни
* Т05 - зафиксировал изменения в локальном репозиторити
* Т06 - создал еще одну копию удаленного репозитория
* Т07 - перешел в директорию с новой копией реп-ия
* Т08 - в новой копии добавил абзац #2 песни в **song.txt**
* Т09 - зафиксировал изменения в локальном репозитории
* Т10 - отправил изменения в удаленнный репозиторий
* Т11 - вернулся в первончальную директорию
* Т12 - попытался отправить изменения с абзацем #3 в удаленный реп-ий
* Т13 - получил конфликт при отправке
* Т14 - обновил локальный репозиторий из удаленного
* Т15 - увидел конфликт в **song.txt**
* Т15 - вручную исправил конфликт в **song.txt**
* Т16 - зафиксировал изменения в локальном репозитории
* Т17 - отправил изменения в удаленный репозиторий