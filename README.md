# Library Management System

## Introduction

The Library Management System is a user-friendly application designed to streamline library operations, providing dedicated interfaces for both administrators and users. Built using Tkinter for the graphical user interface and SQLite3 for the database backend, this system offers key features to enhance library management.

### Key Features

1. **Role Based Interfaces**
   - Customized interfaces for users and admins.
   - Easy-to-use features for users to explore the catalog, borrow, return books, and manage profiles.

2. **Admin Privileges**
   - Admins can efficiently oversee and manage the library system.
   - Features include adding new books, updating book details, and managing user accounts.

3. **Database Integration**
   - SQLite3 ensures data integrity and reliability.
   - Efficient information storage in a relational database.

4. **User and Book Properties**
   - Admins can edit user profiles and book properties to maintain accurate records.
   - Modification of user information and database update capabilities.

5. **Language Support**
   - Login page provides an option for users/admins to select a preferred language.
   - Multi-language support for a diverse user base.

## Member-Task Responsibilities

In the development of the Library Management System, team members had specific responsibilities contributing to the project's success.

- **Özlem Elif Tuncer** ([UpbeatJupiter](https://github.com/UpbeatJupiter))
  - User interface design and layout.
  - User functionalities (browsing catalog, borrowing, returning books, change password).
  - Admin privileges implementation.

- **Yusufhan Saçak** ([JosephDoUrden](https://github.com/JosephDoUrden))
  - Book interface design and layout.
  - Book functionalities (adding book, deleting book, updating book).
  - Admin privileges implementation.
  - Language support.

## Database Schema Diagram

![Alt text](./images/image.png)

## Functionalities

### Language Support

- Language selection before login (with button-3).

![Alt text](./images/image-1.png)

### Validation

- All entry widgets have validation.

![Alt text](./images/image-2.png)

### Admin Page

- Access option for admin to user or book data.

![Alt text](./images/image-3.png)

### Data Functionalities

- Five different options for user data management.

![Alt text](./images/image-4.png)

### Adding New User

- New users can be added by admin.
- Validations such as no more than one username can exist in the database.

![Alt text](./images/image-5.png)

### User List

- Only admin can access the user database.

![Alt text](./images/image-6.png)

### Update User

- User details can be changed by admin with a double click.

![Alt text](./images/image-7.png)

### Book List

- Admin has access to the book database after selecting Book Data.

![Alt text](./images/image-8.png)

### Adding New Book

- New books can be added with satisfied values based on validations.

![Alt text](./images/image-9.png)

### Deleting A Book

- Only admin can delete books by clicking the delete key.

![Alt text](./images/image-10.png)

### Editing Books

- Only admin can edit books based on given validations.

![Alt text](./images/image-11.png)

### User Page

- After user login, the library welcomes the user.

![Alt text](./images/image-12.png)

### Borrowing A Book

- Users can borrow selected books with a double click.

![Alt text](./images/image-13.png)

- Library is updated after borrowing.

![Alt text](./images/image-14.png)

### Books of User

- Users can see the books they borrowed on the My Books page.

![Alt text](./images/image-15.png)

### Returning A Book

- Users can return selected books on the My Books page with a double click.

![Alt text](./images/image-16.png)

- My Books page is updated after return.

![Alt text](./images/image-17.png)

### Change Password

- The Profile tab allows users to view their details and change their password.

![Alt text](./images/image-18.png)
![Alt text](./images/image-19.png)

## How to Use

1. Clone the repository.
2. Run the main application file.
3. Follow the on-screen instructions for logging in, browsing the catalog, managing users/books, and more.

Feel free to contribute, report issues, or suggest improvements!

*Include any additional instructions, dependencies, or setup information as needed.*

**Note:** Insert the actual database schema diagram and any missing details specific to your project.
