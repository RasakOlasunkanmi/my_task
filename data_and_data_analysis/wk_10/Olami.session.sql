CREATE TABLE authors (
    authorId SERIAL PRIMARY KEY,
    authorName VARCHAR(255),
    countryOfOrigin VARCHAR(255),
    numberOfBooksWritten INT
);


CREATE TABLE books (
    bookId SERIAL PRIMARY KEY,
    title VARCHAR(150),
    authorId INT,
    genre VARCHAR(100),
    dateOfPublication DATE,
    publisher VARCHAR(150),
    ISBN VARCHAR(20),
    language VARCHAR(50),
    availableCopies INT,
    ageRating VARCHAR(10),
    FOREIGN KEY (authorId) REFERENCES authors(authorId)
);



CREATE TYPE fulfillment AS ENUM ('Fulfilled', 'Pending', 'Processing');

CREATE TABLE bookOrders (
    orderId SERIAL PRIMARY KEY,
    orderDate DATE,
    bookId INT,
    cost DECIMAL(10, 2),
    quantity INT,
    supplyDate DATE,
    fulfillmentStatus fulfillment,
    supplierName VARCHAR(150),
    FOREIGN KEY (bookId) REFERENCES books(bookId)
);


CREATE TYPE gender AS ENUM ('Male', 'Female');
CREATE TYPE status AS ENUM ('Active', 'Suspended');

CREATE TABLE members (
    memberId SERIAL PRIMARY KEY,
    name VARCHAR(150),
    gender gender,
    emailAddress VARCHAR(100),
    phoneNumber VARCHAR(15),
    address VARCHAR(150),
    age INT,
    typeOfMembership VARCHAR(50),
    dateOfMembership DATE,
    status status
);



CREATE TABLE borrowHistory (
    borrowId SERIAL PRIMARY KEY,
    bookId INT,
    memberId INT,
    borrowDate DATE,
    returnDate DATE,
    FOREIGN KEY (memberId) REFERENCES members(memberId),
    FOREIGN KEY (bookId) REFERENCES books(bookId)
);


CREATE TABLE departments (
    deptId SERIAL PRIMARY KEY,
    departmentName VARCHAR(150),
    managerName VARCHAR(150)
);



CREATE TABLE libraryStaff (
    staffId SERIAL PRIMARY KEY,
    name VARCHAR(150),
    jobTitle VARCHAR(100),
    departmentId INT,
    gender gender,
    address VARCHAR(150),
    phoneNumber VARCHAR(15),
    hireDate DATE,
    managerId INT,
    FOREIGN KEY (departmentId) REFERENCES departments(deptId)
);



