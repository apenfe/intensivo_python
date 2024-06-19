import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    question = "Que idioma aprendiste a hablar primero?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    responses = ["ingles","español","chino"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses