## Cars Application
----

### Backend(DJANGO)
----

* Models
----

* [ ] cars
    * name: string
    * model: string
    * img url: string
    * company_name: string
    * car_logo: string
    * car_image_url: string
    * seller_id: integer
    * price: 
    * quantity: integer
    * created_at: date
    * updated_at: date
    * deleted_at: date

* [ ] User
    * username: string
    * email: string
    * password: string (hashed)
    * isAdmin: bool
    * isSeller: bool

* API's Routes:
----
* [ ] Cars
    * [ ] GET /cars
    * [ ] UPDATE /cars/id
    * [ ] PUT /cars/id
    * [ ] DELETE /cars/id

* [ ] Seller
----
    * [ ] GET /sellers
    * [ ] UPDATE /sellers/id
    * [ ] PUT /sellers/id
    * [ ] DELETE /sellers/id

* [ ] User (admin only!)
    * [ ] GET /users
    * [ ] UPDATE /users/id
    * [ ] PUT /users/id
    * [ ] DELETE /users/id

* [ ] Authentication
    * [ ] Register /auth/register
    * [ ] Login /auth/login
    * [ ] Logout /auth/logout
    * [ ] Email confirmation!
    * [ ] Oauth2.0 (Google)

* [ ] Authorization
    * Only admin can GET, DELETE, PUT, UPDATE users
    * Only admin && seller owner can GET, DELETE, PUT, UPDATE cars.
* [ ] Admin panel

### Frontend (REACTJS)
----