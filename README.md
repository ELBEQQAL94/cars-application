## Cars Application
----

### Run Back End
----

### Back End
----
* Live Url: 

### Run Backend Test
----

### Run Front End 
----

### Front End 
----
* Live Url: 

### Run Front End Test
----

### Back End(DJANGO)
----

### DATABASE: 
----
* MONGODB Atlas

* Schema
----
* [ ] cars
    * [x] id: string 
    * [x] name: string (required)
    * [x] model: string (required)
    * [x] company_name: string (optional or by default username)
    * [x] car_logo: string (optional)
    * [x] car_image_url: string (required)
    * [ ] seller_id: integer (required)
    * [x] price: decimal (required in USD Currency)
    * [x] quantity: integer (optional or by default 1)
    * [x] color: string (required)
    * [x] type: string (required) (electrical or gazual)
    * [x] description: string (optional)
    * [x] created_at: date
    * [x] updated_at: date
    * [ ] deleted_at: date

* [ ] User
    * [x] username: string (required)
    * [x] email: string (required && unique)
    * [x] password: string (required)(hashed)
    * [x] isAdmin: bool (False)
    * [x] isSeller: bool (False)
    * [x] isActive: bool (True)
    * [x] Groups: admin, seller (can only belong to one)

* [ ] Seller Profile
    * [x] email
    * [x] name
    * [x] phone
    * [x] avatar
    * [x] google id
    * [x] twitter profile
    * [x] facebook profile
    * [x] website
* API's Routes:
----

* [ ] Cars Routes (Admin only!):
----
    * [x] GET api/v1/cars
    * [ ] GET api/v1/cars __test__
    * [x] UPDATE api/v1/cars/update/{id}
        * [ ] update one field or more, or update the field you want
    * [ ] UPDATE api/v1/cars/{id} __test__
    * [x] PUT api/v1/cars/create/{id}
    * [ ] PUT api/v1/cars/{id} __test__
    * [x] DELETE api/v1/cars/delete/{id}
    * [ ] DELETE api/v1/cars/{id} __test__
    * [ ] Sort by release date /cars?sort_by=release_date.desc or /cars?
    sort_by=release_date.asc
    * [ ] Sort by __test__
    * [ ] Search cars by name 
    * [ ] Search cars by name __test__
    * [ ] Pagination 
    * [ ] Pagination __test__

* [ ] Sellers Routes (Admin only!):
----
    * [ ] GET api/v1/sellers
    * [ ] GET api/v1/sellers __test__
    * [ ] UPDATE api/v1/sellers/{id}
    * [ ] UPDATE api/v1/sellers/{id} __test__
    * [ ] PUT api/v1/sellers/{id}
    * [ ] PUT api/v1/sellers/{id} __test__
    * [ ] DELETE api/v1/sellers/{id}
    * [ ] DELETE api/v1/sellers/{id} __test__

* [ ] SellerCars (admin + seller or owner user)
----
    * [ ] GET api/v1/seller/cars
    * [ ] GET api/v1/seller/cars __test__
    * [ ] UPDATE api/v1/seller/cars/{id}
    * [ ] UPDATE api/v1/seller/cars/{id} __test__
    * [ ] DELETE api/v1/seller/cars/{id}
    * [ ] DELETE api/v1/seller/cars/{id} __test__
    * [ ] PUT api/v1/seller/cars
    * [ ] PUT api/v1/seller/cars __test__
    * [ ] Sort by release date 
    * [ ] Sort by release date __test__
    * [ ] Search
    * [ ] Search __test__
    * [ ] Pagination
    * [ ] Pagination __test__

* [ ] User (admin only!)
----
    * [ ] GET api/v1/users
    * [ ] GET api/v1/users __test__
    * [ ] UPDATE api/v1/users/{id}
    * [ ] UPDATE api/v1/users/{id} __test__
    * [ ] PUT api/v1/users/{id}
    * [ ] PUT api/v1/users/{id} __test__
    * [ ] DELETE api/v1/users/{id}
    * [ ] DELETE api/v1/users/{id} __test__
    * [ ] Sort by release date
    * [ ] Sort by release date __test__
    * [ ] Search user by email 
    * [ ] Search user by email __test__
    * [ ] Pagination
    * [ ] Pagination __test__

* [ ] Authentication
----
    * [ ] Register api/v1/auth/register
    * [ ] Register api/v1/auth/register __test__
    * [ ] Login api/v1/auth/login
    * [ ] Login api/v1/auth/login __test__
    * [ ] Logout api/v1/auth/logout
    * [ ] Logout api/v1/auth/logout __test__
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
* [x] Connect MongoDb Atlas with Django server
    * mongodb+srv://ELBEQQAL:<password>@cluster0.m7kbe.mongodb.net/<dbname>?retryWrites=true&w=majority
* [x] Add superuser
* [x] Generate .gitignore file gitignore.io
* [x] Change name main file to config 
* [x] Add apps folder as container for all django's 
applications
* [x] Install django rest framework
* [ ] Create cars model
* [ ] Create user model
    * [ ] api/v1/auth/register
    * [ ] api/v1/auth/login
    * [ ] api/v1/auth/logout
* [ ] Create database for __test__

### Front End (REACTJS Hooks!)
----

### TODOS:
----
* [ ] Redux Hooks! 