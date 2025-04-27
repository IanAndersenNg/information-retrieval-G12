# information-retrieval-G12


## Setup

### Install Java
Java installation instructions may be found here:<br>
https://adoptium.net/temurin/releases/?version=17
<br><br>
As the project was built using JDK 17, JDK 17+ is recommended

### Install Maven
Maven installation instructions may be found here:<br>
https://maven.apache.org/install.html
<br><br>
Maven is a simple package manager which removes the need to manually install packages. To further simplify the execution process, it's suggested to add the maven's bin directory to PATH, as explained in the instructions above.

### Execution
Execute the following commands in succession:
```declarative
mvn clean compile
```
```declarative
mvn exec:java -Dexec.args='index "<path to yelp_academic_dataset_review.json file here>" search_index'
```

## Querying

### Term Query execution with example
![Screenshot from 2025-04-27 18-30-12](https://github.com/user-attachments/assets/e0c15723-4c3f-44c0-9d58-8f0cfa0df927)
