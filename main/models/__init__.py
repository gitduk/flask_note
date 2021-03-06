from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    from main.models.note import index_model
    from main.models.note import login_model
    from main.models.wchat import msg_model
    from main.models.lsqlalchemy import test
    with app.app_context():
        db.create_all()
