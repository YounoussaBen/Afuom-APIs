# AG E-Commerce APIs

AG E-Commerce APIs is an e-commerce platform tailored for agricultural products. It provides a set of APIs for managing products, orders, carts, authentication, and more. This documentation will guide you through the installation process, API endpoints, authentication, and usage.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YounoussaBen/Ag-Ecom-APIs.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Ag-Ecom-APIs
   ```

3. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. Rename `.env.example` to `.env` and update the environment variables as needed:

   ```bash
   mv .env.example .env
   ```

   Ensure to replace the placeholder values with your actual settings.

5. Run migrations to create the database schema:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The server should now be running at `http://127.0.0.1:8000/`.

## API Documentation

### Swagger UI

You can explore the API endpoints and interact with them using Swagger UI.

- Base URL: `http://127.0.0.1:8000/api`
- [Swagger UI Link](http://127.0.0.1:8000/swagger/?format=openapi)

### Authentication

Authentication is required for certain endpoints. Use JWT tokens for authentication. Pass the Bearer token into the Authorization header to access protected APIs.

#### Endpoints:

- `/auth/google/`: Authenticate with Google.
- `/auth/token/`: Obtain an authentication token.
- `/auth/token/refresh/`: Refresh an authentication token.
- `/auth/user/register/`: Register a new user.

### Cart Management

Manage user shopping carts.

#### Endpoints:

- `GET /cart/cart/`: Retrieve user's cart.
- `POST /cart/cart/`: Create a new cart.
- `PUT /cart/cart/{id}/`: Update a cart.
- `PATCH /cart/cart/{id}/`: Partially update a cart.
- `DELETE /cart/cart/{id}/delete/`: Delete a cart.

### Order Management

Manage user orders and checkout process.

#### Endpoints:

- `POST /order/checkout/`: Checkout and create an order.
- `GET /order/orders/{id}/`: Retrieve an order.
- `PUT /order/orders/{id}/`: Update an order.
- `PATCH /order/orders/{id}/`: Partially update an order.
- `DELETE /order/orders/{id}/`: Delete an order.
- `GET /order/seller-order-history/`: Retrieve seller's order history.
- `GET /order/user-order-history/`: Retrieve user's order history.

### Shop Management

Manage product categories and products.

#### Endpoints:

- `GET /shop/categories/`: Retrieve all categories.
- `POST /shop/categories/`: Create a new category.
- `GET /shop/categories/{id}/`: Retrieve a category.
- `PUT /shop/categories/{id}/`: Update a category.
- `PATCH /shop/categories/{id}/`: Partially update a category.
- `DELETE /shop/categories/{id}/`: Delete a category.
- `GET /shop/products/`: Retrieve all products.
- `POST /shop/products/`: Create a new product.
- `GET /shop/products/{id}/`: Retrieve a product.
- `PUT /shop/products/{id}/`: Update a product.
- `PATCH /shop/products/{id}/`: Partially update a product.
- `DELETE /shop/products/{id}/`: Delete a product.

### Wishlist Management

Manage user's wishlist.

#### Endpoints:

- `GET /wishlist/add/`: Retrieve user's wishlist.
- `POST /wishlist/add/`: Add a product to wishlist.
- `DELETE /wishlist/remove/{id}/`: Remove a product from wishlist.
