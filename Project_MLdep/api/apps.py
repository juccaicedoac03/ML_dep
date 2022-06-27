from django.apps import AppConfig
import pickle


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

class RandomForestClassifier(AppConfig):
    mdl = pickle.load(open('../Models/RF_model.pkl', 'rb'))