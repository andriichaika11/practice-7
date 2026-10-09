"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

count_of_students = 0
sum_of_math = 0
sum_of_python = 0
sum_of_english = 0
name_best_student = 0
avg_best_student = 0

with open(INPUT_FILE, "r", encoding = "utf-8") as f:
    next(f)
    for line in f:
        line = line.strip()
        parts = line.split(",")

        name = parts[0]
        math = int(parts[1])
        python = int(parts[2])
        english = int(parts[3])

        count_of_students += 1
        sum_of_math += math
        sum_of_python += python
        sum_of_english += english

        avg_student = round((math + python + english) / 3, 1)
        if avg_student > avg_best_student:
            avg_best_student = avg_student
            name_best_student = name

avg_of_math = round(sum_of_math / count_of_students, 1)
avg_of_python = round(sum_of_python / count_of_students, 1)
avg_of_english = round(sum_of_english / count_of_students, 1)

with open(OUTPUT_FILE, "w", encoding = "utf-8") as f:
    f.write(f"Середній бал по класу:\n math: {avg_of_math}\n python: {avg_of_python}\n english: {avg_of_english}\n Найкращий студент: {name_best_student} ({avg_best_student})")
print(f"Середній бал по класу:\n math: {avg_of_math}\n python: {avg_of_python}\n english: {avg_of_english}\n Найкращий студент: {name_best_student} ({avg_best_student})")
# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
