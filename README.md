# Course Allocation to Students based on preferences
This repository contains the implementation of the algorithm that was used for the allocation of courses (from the Humanities department) to students in IIT Gandhinagar. The Course Allocation System is designed to efficiently allocate courses to students based on their preferences, utilizing a modified version of the hospital resident matching algorithm. To uphold data privacy standards, the data present in this repository (for demonstrative purposes) has been synthetically generated.<br/><br/>

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
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please open an issue in the GitHub repository, or directly contact the me via [email](mailto:mrigankashekhar.shandilya@iitgn.ac.in).
