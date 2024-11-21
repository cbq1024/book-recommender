CREATE SCHEMA IF NOT EXISTS db;

create table db.user
(
    id          bigint generated by default as identity
        constraint user_pk
            primary key,
    username    varchar                                not null
        constraint username_uniq
            unique,
    create_time timestamp with time zone default now() not null,
    password    varchar                                not null,
    enable      boolean                  default true  not null
);

comment
on table db.user is 'user information';


create table db.permission
(
    id   bigint generated by default as identity
        constraint permission_pk
            primary key,
    code varchar not null,
    name varchar not null
);

comment
on table db.permission is 'user permission';

create table db.role
(
    id   bigint generated by default as identity
        constraint role_pk
            primary key,
    code varchar not null,
    name varchar not null
);

comment
on table db.role is 'user role';

create table db.role_permission_map
(
    id            bigint generated by default as identity
        primary key,
    role_id       bigint not null,
    permission_id bigint not null
);

comment
on table db.role_permission_map is 'user role_permission_map';

create table db.user_role_map
(
    id      bigint generated by default as identity
        primary key,
    user_id bigint not null,
    role_id bigint not null
);

comment
on table db.user_role_map is 'user user_role_map';

CREATE TABLE db.book
(
    id            BIGINT GENERATED BY DEFAULT AS IDENTITY
        CONSTRAINT book_pk PRIMARY KEY,
    title              VARCHAR     NOT NULL,
    authors            VARCHAR     NOT NULL,
    average_rating     float,
    isbn               VARCHAR     NOT NULL,
    isbn13             VARCHAR     NOT NULL,
    language_code      VARCHAR(10) NOT NULL,
    num_pages          INT         NOT NULL,
    ratings_count      BIGINT      NOT NULL,
    text_reviews_count BIGINT      NOT NULL,
    publication_date   DATE        NOT NULL,
    publisher          VARCHAR     NOT NULL
);

COMMENT
ON TABLE db.book IS 'Book information including title, authors, rating, and other details.';

COMMENT
ON COLUMN db.book.id IS 'Unique identifier for each book.';
COMMENT
ON COLUMN db.book.title IS 'Title of the book.';
COMMENT
ON COLUMN db.book.authors IS 'Authors of the book.';
COMMENT
ON COLUMN db.book.average_rating IS 'Average user rating of the book.';
COMMENT
ON COLUMN db.book.isbn IS 'ISBN of the book.';
COMMENT
ON COLUMN db.book.isbn13 IS 'ISBN-13 of the book.';
COMMENT
ON COLUMN db.book.language_code IS 'Language code of the book.';
COMMENT
ON COLUMN db.book.num_pages IS 'Number of pages in the book.';
COMMENT
ON COLUMN db.book.ratings_count IS 'Number of ratings given to the book.';
COMMENT
ON COLUMN db.book.text_reviews_count IS 'Number of text reviews for the book.';
COMMENT
ON COLUMN db.book.publication_date IS 'Publication date of the book.';
COMMENT
ON COLUMN db.book.publisher IS 'Publisher of the book.';