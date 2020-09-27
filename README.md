## Cars Application
----

### Backend(DJANGO)
----

* Models
----
* [ ] cars
    * id: string 
    * name: string (required)
    * model: string (required)
    * img_url: string (required)
    * company_name: string (optional or by default username)
    * car_logo: string (optional)
    * car_image_url: string (required)
    * seller_id: integer (required)
    * price: decimal (required in USD Currency)
    * quantity: integer (optional or by default 1)
    * color: string (required)
    * type: string (required) (electrical or gazual)
    * description: string (optional)
    * created_at: date
    * updated_at: date
    * deleted_at: date

* [ ] User
    * username: string (required)
    * email: string (required && unique)
    * password: string (required)(hashed)
    * isAdmin: bool (False)
    * isSeller: bool (False)
    * isActive: bool (True)
    * avatar_url: string (null)

* API's Routes:
----

* [ ] Cars Routes (Admin only!):
----
    * [ ] GET /cars
    * [ ] GET /cars __test__
    * [ ] UPDATE /cars/{id}
    * [ ] UPDATE /cars/{id} __test__
    * [ ] PUT /cars/{id}
    * [ ] PUT /cars/{id} __test__
    * [ ] DELETE /cars/{id}
    * [ ] DELETE /cars/{id} __test__
    * [ ] Sort by release date /cars?sort_by=release_date.desc or /cars?
    sort_by=release_date.asc
    * [ ] Sort by __test__
    * [ ] Search cars by name 
    * [ ] Search cars by name __test__
    * [ ] Pagination 
    * [ ] Pagination __test__

* [ ] Sellers Routes (Admin only!):
----
    * [ ] GET /sellers
    * [ ] GET /sellers __test__
    * [ ] UPDATE /sellers/{id}
    * [ ] UPDATE /sellers/{id} __test__
    * [ ] PUT /sellers/{id}
    * [ ] PUT /sellers/{id} __test__
    * [ ] DELETE /sellers/{id}
    * [ ] DELETE /sellers/{id} __test__

* [ ] SellerCars (admin + seller or owner user)
----
    * [ ] GET /seller/cars
    * [ ] GET /seller/cars __test__
    * [ ] UPDATE /seller/cars/{id}
    * [ ] UPDATE /seller/cars/{id} __test__
    * [ ] DELETE /seller/cars/{id}
    * [ ] DELETE /seller/cars/{id} __test__
    * [ ] PUT /seller/cars
    * [ ] PUT /seller/cars __test__
    * [ ] Sort by release date 
    * [ ] Sort by release date __test__
    * [ ] Search
    * [ ] Search __test__
    * [ ] Pagination
    * [ ] Pagination __test__

* [ ] User (admin only!)
----
    * [ ] GET /users
    * [ ] GET /users __test__
    * [ ] UPDATE /users/{id}
    * [ ] UPDATE /users/{id} __test__
    * [ ] PUT /users/{id}
    * [ ] PUT /users/{id} __test__
    * [ ] DELETE /users/{id}
    * [ ] DELETE /users/{id} __test__
    * [ ] Sort by release date
    * [ ] Sort by release date __test__
    * [ ] Search user by email 
    * [ ] Search user by email __test__
    * [ ] Pagination
    * [ ] Pagination __test__

* [ ] Authentication
----
    * [ ] Register /auth/register
    * [ ] Register /auth/register __test__
    * [ ] Login /auth/login
    * [ ] Login /auth/login __test__
    * [ ] Logout /auth/logout
    * [ ] Logout /auth/logout __test__
    * [ ] Email confirmation!
    * [ ] Email confirmation! __test__
    * [ ] Oauth2.0 (Google)
    * [ ] Oauth2.0 (Google) __test__

* [ ] Authorization
----
    * [ ] Only admin can GET, DELETE, PUT, UPDATE users
    * [ ] __test__
    * [ ] Only admin && seller owner can GET, DELETE, PUT, UPDATE cars.
    * [ ] __test__

* [ ] Admin panel (admin only)
----
    * [ ] __test__

* [ ] Integrate Stripe
----
    * [ ] __test__

* [ ] Integrate Paypal
----
    * [ ] __test__

### TODOS:
----
* [ ] Connect MongoDb Atlas with Django server
* [ ] Create cars model
* [ ] Create user model
    * [ ] /auth/register
    * [ ] /auth/login
    * [ ] /auth/logout
* [ ] Create database for __test__

### Frontend (REACTJS)
----

* [ ] Redux Hooks! 