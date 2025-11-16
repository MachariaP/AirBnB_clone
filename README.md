# 🏠 AirBnB Clone - HBnB

## 📜 Table of Contents
* [1. Project Overview](#1-project-overview)
* [2. Team Roles and Responsibilities](#2-team-roles-and-responsibilities)
* [3. Technology Stack Overview](#3-technology-stack-overview)
* [4. Database Design Overview](#4-database-design-overview)
* [5. Feature Breakdown](#5-feature-breakdown)
* [6. API Security Overview](#6-api-security-overview)
* [7. CI/CD Pipeline Overview](#7-cicd-pipeline-overview)
* [8. Resources](#8-resources)
* [9. License](#9-license)
* [10. Created By](#10-created-by)

---

## 1. Project Overview

**Brief Description:**

HBnB is a comprehensive web application clone of AirBnB, designed to replicate the core functionality of the popular vacation rental marketplace. This project serves as an educational implementation demonstrating full-stack development principles, object-oriented programming, and modern software architecture patterns. The current implementation focuses on the backend foundation, featuring a robust command-line interface for data management and a file-based persistence layer.

The project addresses the challenge of building a scalable, maintainable codebase for managing rental property listings, user accounts, reviews, and location-based data. It implements a complete CRUD (Create, Read, Update, Delete) system with an interactive console interface that allows administrators and developers to manage all aspects of the application's data model.

**Project Goals:**

* **Modular Architecture**: Implement a clean, object-oriented design using base classes and inheritance to promote code reusability and maintainability
* **Data Persistence**: Develop a flexible storage engine that serializes and deserializes objects to JSON, with the ability to scale to database backends in future iterations
* **Command-Line Interface**: Build an intuitive, feature-rich console application for managing application data without requiring a web interface
* **Comprehensive Testing**: Establish a robust unit testing framework ensuring code reliability and facilitating continuous integration
* **Scalability Foundation**: Create a modular architecture that can evolve to support RESTful APIs, database integration, and front-end interfaces
* **Educational Excellence**: Provide a clear, well-documented codebase that demonstrates best practices in Python development and software design patterns

**Key Tech Stack:**

* **Language**: Python 3 (object-oriented programming)
* **Data Storage**: JSON-based file storage with serialization/deserialization
* **CLI Framework**: Python's `cmd` module for interactive command-line interface
* **Testing**: Python's `unittest` framework for comprehensive test coverage
* **Version Control**: Git and GitHub for collaborative development

---

## 2. Team Roles and Responsibilities

| Role | Key Responsibility |
|------|-------------------|
| **Backend Developer** | Design and implement core models (BaseModel, User, Place, etc.), develop storage engine, ensure data integrity and proper OOP principles |
| **Console/CLI Developer** | Build and maintain the command-line interface, implement command parsing, create user-friendly interaction patterns and help documentation |
| **Quality Assurance Engineer** | Write comprehensive unit tests, perform integration testing, validate data persistence, ensure code coverage across all modules |
| **DevOps Engineer** | Set up CI/CD pipelines, manage version control workflows, automate testing and deployment processes, maintain development environments |
| **Database Architect** | Design data models and relationships, plan future database migration strategies, optimize data serialization and storage patterns |
| **Technical Documentation Lead** | Maintain comprehensive documentation, create usage guides, document API specifications and code architecture for future developers |
| **Project Manager** | Coordinate development tasks, manage timelines and milestones, facilitate team communication, ensure adherence to project requirements |

---

## 3. Technology Stack Overview

| Technology | Purpose in the Project |
|-----------|----------------------|
| **Python 3.x** | Primary programming language providing object-oriented capabilities, strong typing support, and extensive standard library for application logic |
| **cmd Module** | Python's built-in command-line interpreter framework used to create the interactive HBnB console with command parsing and help system |
| **uuid Module** | Generates unique identifiers (UUID4) for each object instance, ensuring globally unique IDs across the application |
| **datetime Module** | Handles timestamp creation and formatting for `created_at` and `updated_at` attributes, tracking object lifecycle |
| **json Module** | Serializes Python objects to JSON format and deserializes JSON data back to Python objects for file-based persistence |
| **shlex Module** | Provides sophisticated command-line string parsing, handling quoted strings and complex argument structures in console commands |
| **re (Regular Expressions)** | Enables advanced pattern matching for parsing complex console commands with dot notation (e.g., `User.show(id)`) |
| **unittest Framework** | Python's built-in testing framework for writing and executing unit tests, ensuring code quality and preventing regressions |
| **File System (JSON)** | Persistent storage mechanism using `file.json` to save and reload application state between sessions |
| **Git/GitHub** | Version control system for collaborative development, code review, and project history management |

---

## 4. Database Design Overview

**Key Entities:**

The HBnB application implements a comprehensive data model with seven primary entities, each inheriting from a `BaseModel` base class:

* **BaseModel**: Foundation class providing common attributes (`id`, `created_at`, `updated_at`) and methods (`save()`, `to_dict()`) inherited by all other models
* **User**: Represents application users with authentication credentials and personal information (email, password, first_name, last_name)
* **State**: Geographic entity representing states or provinces, used for location hierarchy
* **City**: Urban areas within states, maintaining reference to parent state via `state_id` foreign key
* **Place**: Central entity representing rental properties with detailed attributes (name, description, rooms, price, location coordinates, capacity)
* **Amenity**: Features and facilities that can be associated with places (WiFi, parking, pool, etc.)
* **Review**: User-generated feedback for places, linking users to their reviews of specific properties

**Relationships:**

* **State ↔ City**: One-to-Many relationship where one State contains multiple Cities. City entities reference their parent State through the `state_id` attribute, enabling geographic organization and queries by location.

* **City ↔ Place**: One-to-Many relationship where a City can host multiple rental Places. Each Place is associated with a specific City via `city_id`, allowing users to search and filter properties by location.

* **User ↔ Place**: One-to-Many relationship where a User (as host) can own multiple Places. The `user_id` in Place identifies the property owner, enabling user-specific property management and host profiles.

* **User ↔ Review**: One-to-Many relationship where a User can write multiple Reviews. Each Review is linked to its author through `user_id`, tracking who provided each piece of feedback.

* **Place ↔ Review**: One-to-Many relationship where a Place can receive multiple Reviews. The `place_id` in Review connects feedback to specific properties, enabling rating and review systems.

* **Place ↔ Amenity**: Many-to-Many relationship where Places can have multiple Amenities and Amenities can be associated with multiple Places. The `amenity_ids` list in Place stores references to associated amenities, enabling feature-based property searches.

---

## 5. Feature Breakdown

* **Object Creation and Management**: Dynamically create instances of any model class (User, Place, State, City, Amenity, Review) with automatic ID generation and timestamp tracking. Each object is immediately serialized to persistent storage, ensuring data durability.

* **Interactive Command-Line Console**: Fully-featured REPL (Read-Eval-Print Loop) interface supporting both interactive and non-interactive modes. Commands can be executed via direct console input or piped from scripts, enabling automation and batch operations.

* **Advanced Command Syntax Support**: Implements dual command syntax patterns—traditional space-separated commands (`show User 123`) and object-oriented dot notation (`User.show("123")`), providing flexibility for different user preferences and programming styles.

* **Comprehensive CRUD Operations**: Complete suite of Create, Read, Update, and Delete operations across all model types. Users can create new instances, display existing data, modify attributes, and remove objects through intuitive commands.

* **Persistent JSON Storage Engine**: Abstracted storage layer using the FileStorage class that automatically serializes objects to JSON upon creation or modification and deserializes them on application startup, maintaining state across sessions.

* **Flexible Query and Filtering**: Retrieve all instances of a specific class or all objects across all classes. The `count` command provides quick statistics, while `all` supports both filtered and unfiltered queries.

* **Dynamic Attribute Updates**: Update object attributes individually or in bulk using dictionary-based updates. Supports type preservation for class-defined attributes while allowing dynamic attribute addition.

* **Timestamp Tracking**: Automatic tracking of object creation and modification times using ISO 8601 formatted timestamps, enabling audit trails and time-based queries.

* **Object Serialization and Deserialization**: Seamless conversion between Python objects and JSON representations via the `to_dict()` method, supporting data export, API integration, and cross-platform compatibility.

* **Comprehensive Help System**: Built-in documentation accessible via the `help` command, providing usage instructions and syntax examples for all available commands directly in the console.

* **Instance Counting and Analytics**: Quick statistical queries with the `count` command, allowing administrators to track the number of instances per model class without loading full datasets.

* **Error Handling and Validation**: Robust input validation with clear error messages for missing parameters, invalid class names, non-existent instances, and malformed commands, ensuring data integrity and user guidance.

---

## 6. API Security Overview

While the current implementation focuses on a console-based interface, the architecture is designed with security best practices that will extend to future API development:

* **Input Validation and Sanitization**: All console inputs are parsed and validated before execution, preventing injection attacks and ensuring data type integrity. This pattern will extend to API request validation using frameworks like Flask-RESTful or FastAPI with Pydantic models, preventing SQL injection, XSS, and other input-based vulnerabilities.

* **Authentication and Authorization** (Planned): User model includes password field in preparation for authentication systems. Future implementations will incorporate secure password hashing (bcrypt or Argon2), JWT token-based authentication for stateless API sessions, and role-based access control (RBAC) to restrict operations based on user privileges.

* **Data Encryption** (Planned): Sensitive user data, particularly passwords and personal information, will be encrypted at rest using AES-256 encryption and in transit using TLS/SSL certificates. The file storage system will evolve to support encrypted JSON or migrate to database systems with native encryption support.

* **Rate Limiting** (Planned): To prevent abuse and denial-of-service attacks, API endpoints will implement rate limiting using tools like Flask-Limiter or Redis-based token buckets, restricting the number of requests per user/IP within specified time windows.

* **Session Management** (Planned): Secure session handling with automatic timeout, session invalidation on logout, and prevention of session fixation attacks. Sessions will use cryptographically secure random tokens with short expiration times.

* **CORS Policy Configuration** (Planned): When the web frontend is implemented, Cross-Origin Resource Sharing (CORS) will be strictly configured to allow requests only from trusted domains, preventing unauthorized cross-origin access.

* **Audit Logging**: The existing timestamp tracking (`created_at`, `updated_at`) provides foundation for comprehensive audit logging. Future enhancements will log all data access and modifications with user attribution, IP addresses, and action details for security monitoring and compliance.

* **Principle of Least Privilege**: The modular storage engine abstraction allows for future implementation of granular permissions, ensuring users can only access and modify data they own or are explicitly authorized to access.

---

## 7. CI/CD Pipeline Overview

Continuous Integration and Continuous Deployment (CI/CD) are essential practices for maintaining code quality and streamlining the development workflow in modern software projects. CI/CD automates the process of testing, building, and deploying code changes, ensuring that every commit is validated against quality standards before integration.

For the HBnB project, a CI/CD pipeline would be implemented to:

* **Automated Testing**: Every push to the repository triggers the complete test suite (`unittest discover tests`), ensuring that new changes don't break existing functionality. Unit tests validate individual components (models, storage, console commands) while integration tests verify system-wide behavior.

* **Code Quality Checks**: Automated linting with tools like `pycodestyle` (PEP 8 compliance) and `pylint` ensures consistent code formatting and catches common errors before manual review. Static analysis tools identify potential bugs and security vulnerabilities.

* **Build Validation**: Although Python doesn't require compilation, the CI pipeline validates that all modules import correctly, dependencies are satisfied, and the application can start without errors.

* **Deployment Automation**: Upon successful test completion on the main branch, the application can be automatically deployed to staging or production environments using containerization (Docker) and orchestration tools (Kubernetes, Docker Compose).

**Tools and Technologies for CI/CD:**

* **GitHub Actions**: Integrated CI/CD platform that runs workflows on every push, pull request, or scheduled interval. Configuration via `.github/workflows/` YAML files enables custom testing and deployment pipelines.

* **Docker**: Containerization ensures consistent environments across development, testing, and production. A `Dockerfile` packages the application with all dependencies, eliminating "works on my machine" issues.

* **pytest/unittest**: Automated test execution with coverage reporting (using `coverage.py`) to track which code paths are tested, aiming for >80% coverage.

* **Pre-commit Hooks**: Git hooks that run linting and basic tests before allowing commits, catching issues before they reach the repository.

This approach ensures code quality, reduces manual testing overhead, and enables rapid, confident deployment of new features and bug fixes.

---

## 8. Resources

* **Python Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/) - Official Python 3 documentation for language reference and standard library
* **Python cmd Module**: [https://docs.python.org/3/library/cmd.html](https://docs.python.org/3/library/cmd.html) - Guide to building command-line interpreters
* **Python unittest**: [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html) - Testing framework documentation
* **JSON in Python**: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html) - Working with JSON data serialization
* **PEP 8 Style Guide**: [https://pep8.org/](https://pep8.org/) - Python code style conventions for readable, consistent code
* **Object-Oriented Programming**: [https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/) - Comprehensive OOP guide
* **Git and GitHub**: [https://docs.github.com/](https://docs.github.com/) - Version control best practices and collaboration workflows
* **AirBnB Engineering Blog**: [https://medium.com/airbnb-engineering](https://medium.com/airbnb-engineering) - Insights from the original platform's technical team

---

## 9. License

This project is licensed under the **MIT License**.

The MIT License is a permissive free software license that allows for reuse within proprietary software provided all copies include the license terms and copyright notice. It permits commercial use, modification, distribution, and private use while providing no warranty.

---

## 10. Created By

**Phinehas Macharia**

[![GitHub](https://img.shields.io/badge/GitHub-MachariaP-181717?style=for-the-badge&logo=github)](https://github.com/MachariaP)
[![Email](https://img.shields.io/badge/Email-walburphinehas78%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:walburphinehas78@gmail.com)

*Software Engineer | Full-Stack Developer | Python Enthusiast*

---

**Contributing Authors:**
- **Dinar Wanjiru** - [Dinarwanjiru](https://github.com/Dinarwanjiru)

---

<div align="center">

### ⭐ If you find this project useful, please consider giving it a star! ⭐

**Built with 💙 by Phinehas Macharia**

</div>
