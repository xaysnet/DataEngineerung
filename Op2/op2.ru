import os

class HomeworkResult:
    def __init__(self, author: Person, homework: Homework, solution: str) -> None:
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.now()


class Student(Person):
    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        if not homework.is_active():
            raise DeadlineError('You are late')
        return HomeworkResult(self, homework, solution)


class Teacher(Person):
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text: str, days: int) -> Homework:
        return Homework(text, days)

    @classmethod
    def check_homework(cls, result: HomeworkResult) -> bool:
        if len(result.solution) > 5:
            cls.homework_done[result.homework].add(result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Homework = None) -> None:
        if homework:
            cls.homework_done.pop(homework, None)
        else:
            cls.homework_done.clear()


def save_results_to_file(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)  # Создает папку, если её нет
    
    file_path = os.path.join(directory, 'homework_results.txt')
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for hw, results in Teacher.homework_done.items():
            file.write(f"{hw.text}:\n")
            for res in results:
                file.write(f"  {res.author.first_name} {res.author.last_name} -> {res.solution}\n")
    print(f'Результаты сохранены в {file_path}')


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read documentation', 5)

    results = []
    for student, hw, solution in [(good_student, oop_hw, 'I have done this hw'), 
                                   (good_student, docs_hw, 'I have done this hw too'), 
                                   (lazy_student, docs_hw, 'done')]:
        try:
            results.append(student.do_homework(hw, solution))
        except DeadlineError as e:
            print(e)

    try:
        HomeworkResult(good_student, 'not_homework_object', 'solution')
    except Exception as e:
        print(e)

    for result in results:
        opp_teacher.check_homework(result)

    print('\nСохранённые результаты:')
    for hw, results in Teacher.homework_done.items():
        print(f"{hw.text}:")
        for res in results:
            print(f"  {res.author.first_name} {res.author.last_name} -> {res.solution}")

    save_results_to_file("C:\\1")
    Teacher.reset_results()
    print('\nПосле сброса:')
    print(Teacher.homework_done)