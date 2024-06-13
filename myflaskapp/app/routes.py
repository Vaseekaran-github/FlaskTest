from flask import Blueprint, jsonify, request
from app import db
from app.models import TestWord

bp = Blueprint('main', __name__)

@bp.route('/api/test-word', methods=['GET'])
def get_test_word():
    test_word = TestWord.query.first()
    if test_word:
        return jsonify({"word": test_word.word})
    else:
        return jsonify({"message": "No test word found"}), 404


@bp.route('/admin/update-word', methods=['GET'])
def update_word():
    new_word = request.json.get('word')
    test_word = TestWord.query.first()
    test_word.word = new_word
    db.session.commit()
    return jsonify({"message": "Word updated successfully"})
