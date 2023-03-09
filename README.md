<p align="center">An AirBnB clone.</p>

---

## Description :house:

AirBnB_clone is a complete web application, integrating database storage, 
a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

## Console (Command Interpreter) :computer:

The console is a command line interpreter that permits management of the backend
of Airbnb_clone. It can be used to handle and manipulate all classes utilized by
the application (achieved by calls on the `storage` object defined above).

### Using the Console

The Airbnb_clone console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The Airbnb_clone console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and
the instance is saved to the file `file.json`.

```
root@2da36855100a:~/AirBnB_clone# ./console.py
(hbnb) create BaseModel
b19cd965-92cb-4a97-8961-64063938aa08
```

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
root@2da36855100a:~/AirBnB_clone# ./console.py
(hbnb) create BaseModel
052b1dde-692e-40f9-ab7d-e988074a589a
(hbnb) show BaseModel 052b1dde-692e-40f9-ab7d-e988074a589a
[BaseModel] (052b1dde-692e-40f9-ab7d-e988074a589a) {'name': 'My_First_Model', 'id': '052b1dde-692e-40f9-ab7d-e988074a589a', 'updated_at': datetime.datetime(2023, 3, 8, 14, 1, 22, 12692), 'created_at': datetime.datetime(2023, 3, 8, 14, 1, 22, 12666), 'my_number': 89}
```

* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id. The storage file `file.json`
is updated accordingly.

```
root@2da36855100a:~/AirBnB_clone# ./console.py
(hbnb) create BaseModel
bf9dedc6-4b11-40c4-8b2d-3c154cab04c3
(hbnb) destroy BaseModel bf9dedc6-4b11-40c4-8b2d-3c154cab04c3
(hbnb) show BaseModel bf9dedc6-4b11-40c4-8b2d-3c154cab04c3
** no instance found **
(hbnb) quit
```

* **all**
  * Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

```
root@2da36855100a:~/AirBnB_clone# ./console.py
(hbnb) create BaseModel
bf9dedc6-4b11-40c4-8b2d-3c154cab04c3
(hbnb) all BaseModel
["[BaseModel] (bf9dedc6-4b11-40c4-8b2d-3c154cab04c3) {'id': 'bf9dedc6-4b11-40c4-8b2d-3c154cab04c3', 'updated_at': datetime.datetime(2023, 3, 9, 12, 3, 56, 798216), 'created_at': datetime.datetime(2023, 3, 9, 12, 3, 56, 798195)}", "[BaseModel] (052b1dde-692e-40f9-ab7d-e988074a589a) {'name': 'My_First_Model', 'id': '052b1dde-692e-40f9-ab7d-e988074a589a', 'updated_at': datetime.datetime(2023, 3, 8, 14, 1, 22, 12692), 'created_at': datetime.datetime(2023, 3, 8, 14, 1, 22, 12666), 'first_name': 'Betty', 'my_number': 89}", "[BaseModel] (1ed6c387-5d3a-4ebc-884d-635db0ba8e84) {'name': 'My_First_Model', 'id': '1ed6c387-5d3a-4ebc-884d-635db0ba8e84', 'updated_at': datetime.datetime(2023, 3, 8, 14, 1, 17, 810941), 'created_at': datetime.datetime(2023, 3, 8, 14, 1, 17, 810912), 'my_number': 89}", "[BaseModel] (b19cd965-92cb-4a97-8961-64063938aa08) {'id': 'b19cd965-92cb-4a97-8961-64063938aa08', 'updated_at': datetime.datetime(2023, 3, 9, 12, 0, 44, 766450), 'created_at': datetime.datetime(2023, 3, 9, 12, 0, 44, 766425)}", "[BaseModel] (c42f257a-ae5a-438b-8044-e5a500734f1e) {'name': 'My_First_Model', 'id': 'c42f257a-ae5a-438b-8044-e5a500734f1e', 'updated_at': datetime.datetime(2023, 3, 8, 14, 1, 47, 505156), 'created_at': datetime.datetime(2023, 3, 8, 14, 1, 47, 505132), 'my_number': 89}"
```

* **count**
  * Usage: `count <class>` or `<class>.count()`

Retrieves the number of instances of a given class.


* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute 
pair or dictionary of attribute pairs. If `update` is called with a single 
key/value attribute pair, only "simple" attributes can be updated (ie. not 
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by 
providing a dictionary.


