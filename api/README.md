# API

This Python script retrieves and processes data from a REST API to display information about an employee's TODO list progress. The script can also export this data to CSV and JSON formats.

## Task 0: Gather data from an API

To use this script, run the following command:

```bash
python3 0-gather_data_from_an_API.py <employee_id>
```

Replace `<employee_id>` with the ID of the employee you want to query.

### Example usage:

```bash
python3 0-gather_data_from_an_API.py 2
```

### Output example:

```plaintext
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
```

## Task 1: Export to CSV

This script can also export the employee's task data to a CSV file with the following command:

```bash
python3 1-export_to_CSV.py <employee_id>
```

Replace `<employee_id>` with the ID of the employee you want to export data for.

### Example usage:

```bash
python3 1-export_to_CSV.py 2
```

### Output example (CSV file content, e.g., 2.csv):

```plaintext
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
"2","Antonette","False","et itaque necessitatibus maxime molestiae qui quas velit"
"2","Antonette","False","adipisci non ad dicta qui amet quaerat doloribus ea"
"2","Antonette","True","voluptas quo tenetur perspiciatis explicabo natus"
"2","Antonette","True","aliquam aut quasi"
"2","Antonette","True","veritatis pariatur delectus"
"2","Antonette","False","nesciunt totam sit blanditiis sit"
"2","Antonette","False","laborum aut in quam"
"2","Antonette","True","nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"
"2","Antonette","False","repudiandae totam in est sint facere fuga"
"2","Antonette","False","earum doloribus ea doloremque quis"
"2","Antonette","False","sint sit aut vero"
"2","Antonette","False","porro aut necessitatibus eaque distinctio"
"2","Antonette","True","repellendus veritatis molestias dicta incidunt"
"2","Antonette","True","excepturi deleniti adipisci voluptatem et neque optio illum ad"
"2","Antonette","False","sunt cum tempora"
"2","Antonette","False","totam quia non"
"2","Antonette","False","doloremque quibusdam asperiores libero corrupti illum qui omnis"
"2","Antonette","True","totam atque quo nesciunt"
```

## Task 2: Export to JSON

To export the employee's task data to a JSON file, use the following command:

```bash
python3 2-export_to_JSON.py <employee_id>
```

Replace `<employee_id>` with the ID of the employee you want to export data for.

### Example usage:

```bash
python3 2-export_to_JSON.py 2
```

### Output example (JSON file content, e.g., 2.json):

```json
{"2": [
    {"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"},
    {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"},
    {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false, "username": "Antonette"},
    {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false, "username": "Antonette"},
    {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true, "username": "Antonette"},
    {"task": "aliquam aut quasi", "completed": true, "username": "Antonette"},
    {"task": "ver

itatis pariatur delectus", "completed": true, "username": "Antonette"},
    {"task": "nesciunt totam sit blanditiis sit", "completed": false, "username": "Antonette"},
    {"task": "laborum aut in quam", "completed": false, "username": "Antonette"},
    {"task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true, "username": "Antonette"},
    {"task": "repudiandae totam in est sint facere fuga", "completed": false, "username": "Antonette"},
    {"task": "earum doloribus ea doloremque quis", "completed": false, "username": "Antonette"},
    {"task": "sint sit aut vero", "completed": false, "username": "Antonette"},
    {"task": "porro aut necessitatibus eaque distinctio", "completed": false, "username": "Antonette"},
    {"task": "repellendus veritatis molestias dicta incidunt", "completed": true, "username": "Antonette"},
    {"task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true, "username": "Antonette"},
    {"task": "sunt cum tempora", "completed": false, "username": "Antonette"},
    {"task": "totam quia non", "completed": false, "username": "Antonette"},
    {"task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false, "username": "Antonette"},
    {"task": "totam atque quo nesciunt", "completed": true, "username": "Antonette"}
]}
```

## Task 3: Generate a summary report

To generate a summary report for all employees, use the following command:

```bash
python3 3-generate_summary_report.py
```

### Example usage:

```bash
python3 3-generate_summary_report.py
```

### Output example:

```plaintext
Employee Report Summary:

1. Leanne Graham is done with tasks(11/20):
   - asperiores alias cupiditate tempore quisquam ut a sapiente
   - ut aut vero repudiandae voluptas ullam in
   - iusto odio dignissimos ducimus qui blanditiis praesentium voluptas irure
   - et doloremque nulla
   - repudiandae totam in est sint facere fuga
   - earum doloribus ea doloremque quis
   - sint sit aut vero
   - porro aut necessitatibus eaque distinctio
   - repellendus veritatis molestias dicta incidunt
   - excepturi deleniti adipisci voluptatem et neque optio illum ad
   - totam atque quo nesciunt

2. Ervin Howell is done with tasks(8/20):
   - distinctio vitae autem nihil ut molestias quo
   - voluptas quo tenetur perspiciatis explicabo natus
   - aliquam aut quasi
   - veritatis pariatur delectus
   - nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
   - repellendus veritatis molestias dicta incidunt
   - excepturi deleniti adipisci voluptatem et neque optio illum ad
   - totam atque quo nesciunt

3. Clementine Bauch is done with tasks(12/20):
   - nihil ut voluptates blanditiis autem odio dicta rerum
   - omnis laborum odio
   - quia et suscipit
   - voluptate aut voluptates sunt at maxime autem
   - et deleniti atque tenetur ut quo ut
   - suscipit repellat esse quibusdam voluptatem incidunt
   - distinctio vitae autem nihil ut molestias quo
   - voluptas quo tenetur perspiciatis explicabo natus
   - aliquam aut quasi
   - veritatis pariatur delectus
   - nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
   - totam atque quo nesciunt

...
```

## Task 4: Perform error handling

In this task, you should add error handling to the script to account for cases where the provided employee ID does not exist in the API.

To use this feature, simply run any of the previous commands with a valid or invalid employee ID.

### Example usage (invalid employee ID):

```bash
python3 0-gather_data_from_an_API.py 999
```

### Output example (error message):

```plaintext
Error: Employee with ID 999 not found in the API.
```

## Authors
This project was realized Christophe Ngan (@Sirothpech).

