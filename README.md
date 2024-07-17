DJANGO ToDo App
![TODO1](https://github.com/user-attachments/assets/3d6c0262-b0ff-4a28-9fad-eccde71c8141)
![TODO2](https://github.com/user-attachments/assets/6aaa623e-9b7a-496f-9316-b1ca924e7b06)
![TODO3](https://github.com/user-attachments/assets/c15828df-139f-46b4-965e-1bb6921a40ee)
![TODO4](https://github.com/user-attachments/assets/d97038d5-a7a8-4fe5-abc7-4cae6df54e6e)

Clone the repository:

git clone <repository-url>
cd <repository-directory>



Build and run the Docker containers:

docker-compose up --build



Apply migrations:

docker-compose exec web python manage.py migrate



Create a superuser (optional):
docker-compose exec web python manage.py createsuperuser



API Endpoints
Authentication
Register: POST /api/register/
Login: POST /api/login/
Token Refresh: POST /api/token/refresh/
ToDo
List ToDos: GET /api/todos/
Create ToDo: POST /api/todos/create/
Retrieve ToDo: GET /api/todos/<id>/
Update ToDo: PUT /api/todos/update/<id>/
Delete ToDo: DELETE /api/todos/delete/<id>/
Photo
List Photos: GET /api/photos/
Create Photo: POST /api/photos/
Retrieve Photo: GET /api/photos/<id>/
Update Photo: PUT /api/photos/<id>/
Delete Photo: DELETE /api/photos/<id>/



![auth4](https://github.com/user-attachments/assets/fb0ca076-dc8f-49be-b1a3-64bd1206cf7e)
![auth3](https://github.com/user-attachments/assets/850d61b0-1907-47b8-9546-1a1563e387ee)
![auth2](https://github.com/user-attachments/assets/e2c7ae90-982c-4055-a011-ec63a38aa571)
![auth0](https://github.com/user-attachments/assets/393b8f3c-0fb8-4a28-8281-e19b97891c84)
![auth5](https://github.com/user-attachments/assets/ccebeeab-5a58-47bc-a420-3a80ff37d820)

