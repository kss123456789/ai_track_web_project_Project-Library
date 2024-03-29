from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config) # config 에서 가져온 파일을 사용합니다.

    db.init_app(app) # SQLAlchemy 객체를 app 객체와 이어줍니다.
    Migrate().init_app(app, db)

    from views import main_view, book_detail_view, book_record_view
    app.register_blueprint(main_view.bp)
    app.register_blueprint(book_detail_view.bp)
    app.register_blueprint(book_record_view.bp)
    
    return app

if __name__ == "__main__":
    create_app().run(debug=True, port=3333)