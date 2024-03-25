## Flask Application Design for Synthetic Data Generation

### HTML Files
- **index.html:**
    - The main page of the application where users can specify the parameters for data generation.
    - Contains a form with input fields for specifying the number of rows, columns, and data types for the synthetic data.
    - A submit button to generate the data.
- **results.html:**
    - Displays the generated synthetic data in a tabular format.
    - Includes options for downloading the data as a CSV file.

### Routes
- **`/` (GET):**
    - Renders the `index.html` page where users can input parameters for data generation.
- **`/generate` (POST):**
    - Handles the form submission from `index.html`.
    - Parses the form input to extract data generation parameters.
    - Uses a Flask extension like Flask-Faker to generate synthetic data.
    - Redirects to the `/results` page with the generated data.
- **`/results` (GET):**
    - Renders the `results.html` page and passes the generated data to the template.
- **`/download` (GET):**
    - Handles the download request for the generated data.
    - Writes the data to a CSV file and sends it to the user as a downloadable attachment.