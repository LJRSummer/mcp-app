# MCP Image Similarity Application

This project is a Flask-based web application designed to upload images and calculate their similarity scores using perceptual hashing. It is structured to be deployed on Tencent's MCP platform.

## Project Structure

```
mcp-app
├── src
│   ├── app.py               # Entry point of the application, handles routing and requests
│   ├── templates
│   │   └── index.html       # HTML template for rendering the user interface
│   ├── static
│   │   └── style.css        # Stylesheet for the application
│   └── utils
│       └── image_utils.py   # Utility functions for image processing
├── requirements.txt         # Python dependencies for the project
├── README.md                # Documentation for setting up and running the application
└── .mcpconfig               # Configuration file for Tencent MCP platform
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mcp-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the `src` directory:
   ```
   cd src
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

- Upload images using the provided interface.
- The application will calculate and display the similarity scores between the uploaded images.

## Deployment

Follow the Tencent MCP platform documentation to deploy this application using the provided `.mcpconfig` file. Ensure that all necessary configurations are set according to your deployment requirements.