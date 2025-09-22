# Hinge Health Coding Exercise: Task Management API

Welcome, and thank you for taking the time to collaborate with us!

In this exercise, you are onboarding onto a team who is building a greenfield task management service. The team has selected the python [FastAPI](https://fastapi.tiangolo.com/reference/) framework.

Our goal is not to "stump" you but to provide a fair and standardized way for you to demonstrate your coding skills through a realistic problem.

This exercise is designed to be time-limited while still allowing you to showcase your problem-solving approach. Please use AI assistance when solving this problem and document your usage in your project documentation.

If invited to an on-site interview, you'll have the opportunity to extend your implementation with our team. We'd rather see how you evolve a system you're familiar with rather than solving abstract whiteboard puzzles.

## Getting Started

1. Clone this repository and create a new branch named **hh-coding-exercise**.
2. Work off of this branch. Do not merge your changes into the main branch.
3. Avoid squashing commits; we want to see how your solution evolves over time.
4. Timebox your work to **no more than 2 hours**. It's okay not to get through the entire exercise - focus on implementing a quality solution in the time period that you have.
5. Make sure your service is functioning and all changes are pushed.
6. Email the recruiting team to notify them.

## The Task Management API

Your goal is to develop a **collaborative task management API** that allows multiple users to create and manage tasks.

### **Requirements**

Your API should support the following functionality:

- **Task Operations**:

  - Create a new task → `POST /tasks`
  - Retrieve all tasks → `GET /tasks`
  - Update an existing task → `PATCH /tasks/{id}`
  - Delete a task → `DELETE /tasks/{id}`

- **Scalability & Performance Considerations**: Design with efficiency and future growth in mind.

## Onsite Extension Tasks (Do Not Implement for Take-Home)

If you are invited to an onsite interview, we will work together to extend your implementation. Please **do not** implement the following features as part of your take-home submission. These are reserved for the onsite portion:

- **Authentication & Authorization**: Ensure that users can authenticate and access only their tasks or those shared with them.
- **Task Ownership & Shared Access**: Users should have control over their tasks and be able to share them with others.
- **Optimistic Concurrency Control**: Prevent accidental overwrites when multiple users update the same task.

During the onsite, we may focus on designing and implementing these features collaboratively. Your take-home should focus on the core requirements above.

## Deliverables

1. **Your branch** with:

   - Implementation code
   - Test cases
   - Documentation

2. **Updated README**, including:

   - Any key design decisions you made (including AI-assisted enhancements, if applicable).
   - An architecture document explaining trade-offs in your code and database design/organization.

3. **API Documentation**:
   - FastAPI's automatic OpenAPI documentation (Swagger UI and ReDoc)

## Running this application

### Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Docker (version 27 or higher)
- Docker Compose (version 2.31 or higher)
- Python (3.11 or higher)

### Starting using Docker Compose

1. Start the services using Docker Compose:

   ```bash
   docker-compose up --build
   ```

2. The application will be available at `http://localhost:3000`
3. Access the automatically generated API documentation:
   - Swagger UI: `http://localhost:3000/docs`
   - ReDoc: `http://localhost:3000/redoc`

## Key Design Decisions

This project implements the task management API using FastAPI (Python) with the following technologies:

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM for database operations
- **Pydantic**: Data validation and settings management
- **PostgreSQL**: Robust relational database
- **JWT**: For secure authentication
- **Docker & Docker Compose**: For containerization and deployment

## Project Documentation

_(Include your documentation here, explaining additional setup, design choices, and usage instructions.)_
