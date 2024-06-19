from survey import AnonymousSurvey

question = "Que idioma aprendiste a hablar primero?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print(f"Pulse q en cualquier momento para terminar.")
while True:
    response = input("Idioma: ")
    if response == "q":
        break
    language_survey.store_response(response)

print("\nGracias por participar en la encuesta.")
language_survey.show_results()