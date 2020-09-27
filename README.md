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
    * [ ] UPDATE /cars/{id}
    * [ ] PUT /cars/{id}
    * [ ] DELETE /cars/{id}
    * [ ] Sort by release date /cars?sort_by=release_date.desc or /cars?sort_by=release_date.asc
    * [ ] Search cars by name 
    * [ ] Pagination 

* [ ] Sellers Routes (Admin only!):
----
    * [ ] GET /sellers
    * [ ] UPDATE /sellers/{id}
    * [ ] PUT /sellers/{id}
    * [ ] DELETE /sellers/{id}

* [ ] SellerCars (admin + seller or owner user)
----
    * [ ] GET /seller/cars
    * [ ] UPDATE /seller/cars/{id}
    * [ ] DELETE /seller/cars/{id}
    * [ ] PUT /seller/cars
    * [ ] Sort by release date 
    * [ ] Search
    * [ ] Pagination

* [ ] User (admin only!)
    * [ ] GET /users
    * [ ] UPDATE /users/{id}
    * [ ] PUT /users/{id}
    * [ ] DELETE /users/{id}
    * [ ] Sort by release date
    * [ ] Search user by email 
    * [ ] Pagination

* [ ] Authentication
    * [ ] Register /auth/register
    * [ ] Login /auth/login
    * [ ] Logout /auth/logout
    * [ ] Email confirmation!
    * [ ] Oauth2.0 (Google)

* [ ] Authorization
    * Only admin can GET, DELETE, PUT, UPDATE users
    * Only admin && seller owner can GET, DELETE, PUT, UPDATE cars.

* [ ] Admin panel (admin only)

* [ ] Integrate Stripe

* [ ] Integrate Paypal

### TODOS:
----
* [ ] Connect MongoDb Atlas with Django server
* [ ] Create cars model
* [ ] Create user model
    * [ ] /auth/register
    * [ ] /auth/login
    * [ ] /auth/logout


### Frontend (REACTJS)
----