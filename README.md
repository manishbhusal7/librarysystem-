# librarysystem-

The program starts with a class LibraryManagement that has an initializer method __init__(self, master). This method sets the window size, background color, and initializes variables for books, lend list, and librarians. It creates a login screen with labels for username, password, and two buttons - one for login and the other for registration.
The login(self) method checks if the entered username and password match any of the librarians records in the librarians list. If the credentials match, the login screen is destroyed, and the library_management_screen() method is called.
The register(self) method appends the entered username and password to the librarians list.
The register(self) method appends the entered username and password to the librarians list.
The library_management_screen(self) method creates a screen with four labels and corresponding entry boxes and buttons for adding books, removing books, issuing books, and viewing books.
The add_book(self) method adds a book to the books list.
The remove_book(self) method removes a book from the books list.
The issue_book(self) method issues a book from the books list and adds it to the lend_list list.
Overall, this program can be used as a basic Library Management System with some additional features that can be extended.
