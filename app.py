import os
from common import _app, _api, db
from app_factory import AppFactory
import test_data

if __name__ == '__main__':
     port = int(os.getenv('PORT', 8080))
     host = os.getenv('IP', '0.0.0.0')
     _app = AppFactory.create_app(_api, db, "sqrum.db")
     AppFactory.add_static_server(_app,'front', 'index.html')
     AppFactory.add_test_data(db, test_data.roles)
     AppFactory.add_test_data(db, test_data.stories)
     _app.run(port=port, host=host, debug=True)