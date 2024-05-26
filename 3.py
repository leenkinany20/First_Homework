import json
def read_quiz_from_json(file_path):
    with open(file_path, 'r') as file:
        quiz_data = json.load(file)
    return quiz_data['questions']
def ask_questions(questions):
    score = 0
    for question_data in questions:
        question = question_data['question']
        correct_answer = question_data['answer']
        user_answer = input(question + " ")
        if user_answer.lower() == correct_answer.lower():
            score += 1
    return score
def get_user_name():
    return input("Enter your name: ")
def store_user_result(name, score, file_path, mode='a'):
    with open(file_path, mode) as file:
        file.write(f"name score \n{name },{score}\n")
def main():
    quiz_file = 'quiz.json'
    user_result_file = 'user_results.csv'
    print("enter the answer True or False :")
    questions = read_quiz_from_json(quiz_file)
    score = ask_questions(questions)
    name = get_user_name()
    print("name:",name,"score:",score)
    store_user_result(name, score, user_result_file)
if __name__ == "__main__":
    main()


