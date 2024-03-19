create table students (
	student_id serial primary key,
	first_name text not null,
	last_name text not null,
	email text not null unique,
	enrollment_date date
);