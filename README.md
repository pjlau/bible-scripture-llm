# Find Bible Scripture

A simple locally run webpage built with FastAPI/ReactJS backend/frontend to manage scriptures.

## Directory

   ```
   project/
   ├── backend/
   │   ├── main.py
   │   ├── models.py
   │   ├── database.py
   │   └── ollama_client.py
   └── frontend/
       ├── public/
       │   ├── index.html
       │   └── favicon.ico
       ├── src/
       │   ├── App.js
       │   ├── App.css
       │   ├── components/
       │   │   ├── TaskForm.js
       │   │   └── TaskList.js
       │   ├── index.css
       │   └── index.js
       └── package.json
   ```

## Features
- LLM integration
- Database can be created t save the record
- FastAPI: asynchronous and fast execution
- ReactJS: server-side rendering allows React components to be rendered on the server and sent to the browser as fully rendered HTML

## Prerequisites
- Python 3.8+
- Node.js 18+ and npm
- Ollama installed (https://ollama.com/)
- Git

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/pjlau/bible-scripture-llm.git
   cd bible-scripture-llm
2. Install backend dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
3. Run the Web App:
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
4. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
5. Start the React development server:
   ```bash
   npm start
6. Access the web app at `http://localhost:3000/`.

## Functionality
The app provides the CRUD operations:

- GET /tasks: List all tasks.

- GET /tasks/{id}: Retrieve a specific task.

- POST /tasks: Create a new task with title and optional description.

- PUT /tasks/{id}: Update a task’s title, description, or done status.

- DELETE /tasks/{id}: Delete a task.

## Results

<img src="images/demo_fig1.png" alt="Example1" width="400">
