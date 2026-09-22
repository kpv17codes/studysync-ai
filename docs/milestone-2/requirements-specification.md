# StudySync AI
## Software Requirements Specification (SRS)

**Course:** COMP 425 – Software Engineering  
**Milestone:** Milestone 2 – Requirements Specification  
**Team Members:** Kiamely Pereyra and Massiel Montero  
**Semester:** Fall 2026

---

## 1. Introduction and System Scope

### 1.1 Purpose

StudySync AI is an academic planning application designed to help college students organize their academic responsibilities and manage their study time. The system will allow students to keep track of courses, assignments, exams, deadlines, and available study time in one place.

The purpose of this Software Requirements Specification (SRS) is to define the functional and non-functional requirements of StudySync AI. It establishes what the system is expected to do and provides a basis for future design, development, and testing.

### 1.2 System Scope

StudySync AI will provide college students with tools for managing their academic workload. Students will be able to create an account, manage their courses, record assignments and exams, track deadlines, enter their available study time, and view their academic responsibilities through an organized dashboard and calendar.

The system will also provide an AI-powered study planning feature. The study planner will use information provided by the student, including upcoming academic tasks, deadlines, estimated difficulty, estimated time required, and available study time, to generate personalized study recommendations.

### 1.3 In-Scope Capabilities

The initial version of StudySync AI will include:

- User account registration and login
- Course management
- Assignment and exam management
- Deadline and priority tracking
- Academic dashboard
- Calendar-based organization of academic tasks
- Entry and management of available study time
- AI-generated personalized study plans
- Study progress tracking
- Handling of unsuccessful AI study-plan generation

### 1.4 Out-of-Scope Capabilities

The following capabilities will not be included in the initial version:

- Social networking between students
- Sharing study plans between users
- Direct integration with university learning management systems
- Automatic importing of assignments from external academic systems
- Advanced predictive academic analytics
- Features intended for instructors or university administrators

---

## 2. User Roles

### 2.1 Student

The Student is the primary user of StudySync AI. A student will be able to create and access an account, manage courses, assignments and exams, enter available study time, view upcoming academic responsibilities, and request personalized study plans.

For the initial version of StudySync AI, the system will focus on individual student users. Instructor and administrator roles are outside the current project scope.

## 3. Functional Requirements

The functional requirements define the main actions and capabilities that StudySync AI shall provide to student users.

### 3.1 User Account Management

**FR-101:** The system shall allow a student to create an account using the required account information.

**FR-102:** The system shall allow a registered student to log in using valid credentials.

**FR-103:** The system shall reject a login attempt when the provided credentials are invalid and display an appropriate error message.

**FR-104:** The system shall allow an authenticated student to log out of their account.

### 3.2 Course Management

**FR-201:** The system shall allow an authenticated student to create a course with a course name and other available course information.

**FR-202:** The system shall allow an authenticated student to view their saved courses.

**FR-203:** The system shall allow an authenticated student to update information for an existing course.

**FR-204:** The system shall allow an authenticated student to delete an existing course.
### 3.3 Assignment and Exam Management

**FR-301:** The system shall allow an authenticated student to create an assignment or exam associated with one of their courses.

**FR-302:** The system shall allow a student to enter a title, deadline, estimated difficulty, and estimated time required for an assignment or exam.

**FR-303:** The system shall allow an authenticated student to view their saved assignments and exams.

**FR-304:** The system shall allow an authenticated student to update information for an existing assignment or exam.

**FR-305:** The system shall allow an authenticated student to delete an existing assignment or exam.

**FR-306:** The system shall display upcoming assignments and exams according to their deadlines.

**FR-307:** The system shall indicate when an assignment or exam deadline has passed.

### 3.4 Study Availability

**FR-401:** The system shall allow an authenticated student to enter the days and times they are available to study.

**FR-402:** The system shall allow an authenticated student to update their study availability.

**FR-403:** The system shall allow an authenticated student to remove previously entered study availability.

### 3.5 Dashboard and Calendar

**FR-501:** The system shall provide an authenticated student with a dashboard displaying upcoming academic tasks and deadlines.

**FR-502:** The system shall provide a calendar view of assignments and exams based on their deadlines.

**FR-503:** The system shall allow a student to view academic tasks associated with a selected date.

**FR-504:** The system shall reflect changes to assignments, exams, and deadlines in the student's academic views.

### 3.6 AI Study Plan Generation

**FR-601:** The system shall allow an authenticated student to request a personalized study plan.

**FR-602:** The system shall use the student's upcoming academic tasks, deadlines, estimated difficulty, estimated time requirements, and available study time when generating a personalized study plan.

**FR-603:** The system shall provide the student with study recommendations that identify which academic tasks should be studied and suggested study periods.

**FR-604:** The system shall display the generated study plan to the student after successful generation.

**FR-605:** If a study plan cannot be generated, the system shall inform the student that generation was unsuccessful rather than displaying an incomplete plan.

**FR-606:** If required academic or availability information is missing, the system shall inform the student of the missing information before attempting to generate a study plan.