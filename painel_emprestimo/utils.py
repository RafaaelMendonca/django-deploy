import joblib
import os
from django.conf import settings

def carregar_modelo():
    modelo_path = os.path.join(settings.BASE_DIR, "painel_emprestimo", "ml_models", "modelo_ml.pkl")
    return joblib.load(modelo_path)
