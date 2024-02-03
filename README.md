# Course Allocation to Students based on preferences
This repository contains the implementation of the algorithm that was used for the allocation of courses (from the Humanities department) to students in IIT Gandhinagar. The Course Allocation System is designed to efficiently allocate courses to students based on their preferences, utilizing a modified version of the hospital resident matching algorithm. To uphold data privacy standards, the data present in this repository (for demonstrative purposes) has been synthetically generated.<br/><br/>
<img align="center" src="https://images.unsplash.com/photo-1545987796-200677ee1011?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)" alt="An abstract art image demonstrating conventional intuition for matching algorithms" title="An abstract art image demonstrating conventional intuition for matching algorithms"/><br/>
*<p align="center">An abstract art image demonstrating conventional intuition for matching algorithms</p>*<br/><br/>

## Features
- **Preference-Based Allocation**: Allocates courses to students strictly based on their ranked preferences.
- **Modified Hospital Resident Matching Algorithm**: Adapts a well-established matching algorithm to the educational domain, ensuring fairness and optimality in allocations.
- **Scalability**: Can handle a large number of student allocations.

## How It Works
The system modifies the hospital resident matching algorithm to suit course allocation. Students rank their preferred courses (a subset of the overall courses), and the algorithm iteratively assigns courses based on these preferences until all courses are allocated or all student preferences are exhausted (and no course has a less prferred student than the current student). This method ensures that allocations are as close to student preferences as possible, within the constraints of course capacities and availability.

## File Structure
- The [data](/data) folder contains files containing the input data, including data about the students and their preferences ([students.csv](/data/students.csv)) and data about the courses and their capacities ([courses.csv](courses.csv)).
- The [alloc_structs.py](/alloc_structs.py) file contains the python classes used to instantiate instances of students and courses for the allocation.
- The [allocation.ipynb](/allocation.ipynb) file contains the Jupyter notebook that contains details about the allocation and the source code for the same.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contact
For any questions or feedback, please open an issue in the GitHub repository, or directly contact the me via [email](mailto:mrigankashekhar.shandilya@iitgn.ac.in).
