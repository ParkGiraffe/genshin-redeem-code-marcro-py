from firebase_admin import credentials, firestore, initialize_app
import json

cred = credentials.Certificate('serviceAccountKey.json')
initialize_app(cred)

class UploadJsonFileToFireStore:
    def __init__(self):
        self._json_file = 'data.json'
        self._firestore_collection = 'collection'
        self._firestore_document = 'document'
        self._firestore_field = 'field'
        self._firestore = firestore.Client()
        self._json_data = self._get_json_data()
        self._upload_json_data_to_firestore()

    def _get_json_data(self):
        with open(self._json_file, 'r') as f:
            return json.load(f)

    def _upload_json_data_to_firestore(self):
        self._firestore.collection(self._firestore_collection).document(self._firestore_document).set({
            self._firestore_field: self._json_data
        })