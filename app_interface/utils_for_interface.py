from app_interface.form_processing import FormProcessing


def draw_form(win):
    """Заполнение формы исходными данными"""
    languages = ["Head Hunter", "Super Job"]
    FormProcessing(win, languages)
