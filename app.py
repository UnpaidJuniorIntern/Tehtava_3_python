from flask import Flask

from controllers import users_controller
from controllers import products_controller

app = Flask(__name__)

# user endpoints
app.add_url_rule('/api/users', 'get_all_users_handler', users_controller.get_all_users_handler, methods=['GET'])
app.add_url_rule('/api/users/<user_id>', 'get_user_by_id_handler', users_controller.get_user_by_id_handler, methods=['GET'])
app.add_url_rule('/api/users', 'add_user_handler', users_controller.add_user_handler, methods=['POST'])
app.add_url_rule('/api/users/<user_id>', 'update_user_handler', users_controller.update_user_handler, methods=['PUT', 'PATCH'])
app.add_url_rule('/api/users/<user_id>', 'remove_user_handler', users_controller.remove_user_handler, methods=['DELETE'])

# product endpoints 
app.add_url_rule('/api/products', 'get_all_products_handler', products_controller.get_all_products_handler, methods=['GET'])
app.add_url_rule('/api/products/<product_id>', 'get_product_by_id_handler', products_controller.get_product_by_id_handler, methods=['GET'])
app.add_url_rule('/api/products', 'add_product_handler', products_controller.add_product_handler, methods=['POST'])
app.add_url_rule('/api/products/<product_id>', 'update_product_handler', products_controller.update_product_handler, methods=['PUT', 'PATCH'])
app.add_url_rule('/api/products/<product_id>', 'remove_product_handler', products_controller.remove_product_handler, methods=['DELETE'])


if __name__ == '__main__':
    app.run(debug=True)