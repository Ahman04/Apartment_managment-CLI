# Apartment_managment-CLI

## Description

## Author

Abdirahman Mohamed


The Apartment Management CLI is a Python-based command-line application used to manage apartments, tenants, and payment records.
It demonstrates the use of SQLAlchemy ORM for database modeling and Click for interactive CLI commands.

The system supports full CRUD operations and includes one-to-many relationships:

One Apartment → Many Tenants

One Tenant → Many Payments


This project satisfies all Phase 3 requirements: ORM, CLI, environment setup, CRUD, and modular structure.




## Setup Instructions

1. Clone the Repository
git clone <https://github.com/Ahman04/Apartment_managment-CLI.git>
cd Apartment_managment-CLI

2. Activate Virtual Environment
pipenv shell

3. Install Dependencies
pipenv install

4. Seed the Database
python lib/seed.py

5. Run the CLI
python lib/cli.py


## BDD (Behavior Driven Development)
- User Input	System Output
- Create apartment	Saves apartment to database
- Create tenant with apartment ID	Assigns tenant to the correct apartment
- Create payment	Records payment under correct tenant
- Invalid ID input	Returns “Not found” message
- Update commands	Updates only the specified fields
- Relationship view command	Displays tenants in an apartment or payments for a tenant

## Technologies Used

Python
SQLAlchemy ORM
Click CLI Framework
SQLite
Pipenv

## Database Relationships

1. Apartment → Tenants (One-to-Many)

One apartment can have many tenants.

Implemented using ForeignKey("apartments.id").

2. Tenant → Payments (One-to-Many)

One tenant can have many payments.

Implemented using ForeignKey("tenants.id").

## CLI Commands

## Apartment Commands
python lib/cli.py apartment create
python lib/cli.py apartment list
python lib/cli.py apartment find <id>
python lib/cli.py apartment delete <id>
python lib/cli.py apartment tenants <id>
python lib/cli.py apartment update <id> --number=<new> --unit_type=<new> --rent_amount=<new>

## Tenant Commands
python lib/cli.py tenant create
python lib/cli.py tenant list
python lib/cli.py tenant find <id>
python lib/cli.py tenant delete <id>
python lib/cli.py tenant payments <id>
python lib/cli.py tenant update <id> --name=<new> --phone=<new> --apartment_id=<new>

## Payment Commands
python lib/cli.py payment create
python lib/cli.py payment list
python lib/cli.py payment find <id>
python lib/cli.py payment delete <id>
python lib/cli.py payment update <id> --amount=<new> --date_paid=<new>

## Contact Information

GitHub: Ahman04
Email: m.abdirahmanmohamed.adan@gmail.com



## License

## MIT License

Copyright (c) 2025 Abdirahman Mohamed

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.