<h1>SCAFX: Source Code Automatic Feature eXtraction</h1>

### Research Description 
<p align="justify">
Our main research objective is to automatically group students with similar pro- gramming skills based on the analysis of their submitted source codes. In order to achieve this, we also had to propose novel features for the source code analysis that are related to the learning topics.
</p>

### Source Code Implementation
Our implementation consists of a main file and four other libraries that were all developed by the author. 

:heavy_check_mark: The main file receives input from the user, manages calling the libraries and does the output. 

:heavy_check_mark: Among the libraries, there is one to perform the preprocessing of source codes. 

:heavy_check_mark: Another library extracts features from the processed database. 

:heavy_check_mark: Also, there is a library that concentrates machine learning implementations. 

:heavy_check_mark: Finally, there is a library of various utilities, such as writing files in comma-separated values format.

### Organization of Default Folders and Files

Data input takes place following the 'classroom/topic/student/tasks' structure. All tasks must be in text format.
```
ROOT_INPUT = "db-input"
```
The data output folder corresponds to the result of the tasks preprocessing. They are stored in a single file in text format for each student.
```
ROOT_OUTPUT = "db-output"
```
The output images corresponding to the dendrograms and decision trees are sent to the images folder after finishing the task processing.
```
ROOT_TREE = "images/"
```
The main student cluster file is stored in *.csv format in the root of the project.
```
OUTPUT_FILE = "csv-output-extrator.csv"
```

### How to Run the Application
- To run the application, just store the source code tasks in the ROOT_INPUT folder, following the 'classroom/topic/student/*.c' structure.

- The input parameters for the computational model are configured in a default way, but they can be passed in the function call or changed in the algorithm constants.

- The main function is given the classroom, the learning topic and the number of clusters. Furthermore, it is possible to get a debbuger of the executions by passing "_TRUE_" to "_printador_".
```
main(turma="T1", lista="Lista01", printador=False, num_clusters=4)
```

### Scientific Divulgation
The preliminary results obtained in the execution of our computational model were disclosed to the scientific community.

> BERNARDO SILVA, D.; RIBEIRO CARVALHO, D.; SILLA, C. N.. 2022. A clustering-based computational model to group students with similar programming skills from automatic source code analysis using novel fea- tures. Submitted to Transactions on Learning Technologies (TLT).

### Colaborators

| [<img src="./doc/fotoDavi.png" width=115><br><sub>Davi Bernardo</sub>](https://github.com/davibernardos) | [<img src="./doc/fotoDeborah.png" width=115><br><sub>Deborah Carvalho</sub>]() | [<img src="./doc/fotoSilla.png" width=115><br><sub>Carlos Silla</sub>]() |
| :---: | :---: | :---:
