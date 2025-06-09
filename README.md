# Client and Purchase Management CLI for PostgreSQL

A simple Python CLI application to manage clients and their purchases using PostgreSQL as the database backend. This project allows you to add, update, delete, and list clients, as well as generate CSV reports of purchases and spending per client. The application uses psycopg2 for database interaction, pandas for report generation, and python-dotenv for secure environment variable management.

## Features

    •	Add new clients to the database.
    •	Update client data (name or email) by client ID.
    •	Delete clients by ID, with confirmation prompt.
    •	List all registered clients with formatted output.
    •	Generate CSV reports:
    •	All purchases by all clients.
    •	Total spending per client.

## Requirements

    •	Python 3.8 or newer
    •	PostgreSQL database
    •	psycopg2
    •	pandas
    •	python-dotenv

Install dependencies with:

```python
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in your project root with your PostgreSQL credentials:

```python
DB_HOST=your_host
DB_PORT=5432
DB_USER=your_user
DB_PASS=your_password
DB_NAME=your_database
```

## Usage

Run the application from the command line:

```python
python main.py
```

You will see a menu with options to add, remove, update, list clients, or generate reports.

## Main Functions

• add_new_client(): Register a new client with name, email, and registration date.
• delete_client(): Remove a client by ID, with user confirmation.
• update_client(): Update a client’s name or email by ID, with user confirmation.
• make_search(): List all clients in a formatted table.
• make_total_report(): Generate a CSV file (`compras_clientes.csv`) with all purchases and related client data.
• make_client_report(): Generate a CSV file (`total_gastos_clientes.csv`) with the total spending per client.

## Best Practices Used

    •	Secure credential management with `python-dotenv`
    •	Parameterized SQL queries to prevent SQL injection
    •	Resource management: Always close cursors after use; close the database connection on exit
    •	Exception handling for robust error messages and rollback on failed updates
    •	Formatted output for user-friendly CLI experience
    •	CSV report generation using pandas for easy data analysis

### Notes

    •	Ensure your PostgreSQL database and tables (`clientes`, `compras`) exist and are properly structured.
    •	All CSV reports are generated in the same directory as the script.
    •	You can extend the application to include more features as needed.

### License

This project is provided for educational purposes. Adapt and use as needed.
