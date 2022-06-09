# ID Creator for Businesses and Employees in Python

## Video demo: https://youtu.be/0g7AS96HeyE

## Description

This is my final project on CS50P named ID Creator for Businesses and Employees, as the name itself implies, it will create an ID for you. It can help businesses and employees to create an ID easily. It is available on 2 formats: png and pdf. Before you use this program, please take note that this program only creates a Business ID, not an individual ID (e.g. national ID), and also it does not generate your signature. The project also has a test, if you want to test it

Tip: you can put your logo on any of the corners

```
Fun fact: My mom's ID was my inspiration for my design
```

### Libraries used

- rich: for the loading (the program is fast enough that you can't see it) and the printing of the status of creating the ID
- fpdf2: for creating and editing PDF Files
- PIL: for creating and manipulating pictures

## Instructions

1. First, you should install Python first, before following these procedures else IT WOULD NOT WORK. To install Python click [this link](https://www.python.org/downloads/) and download the latest version. Then click the green "Code" button, then after that, you will see a dropdown menu, click "Download Zip" then unzip it, after you unzip it and have Python installed, go to the next step
2. Run the program via
   ```
   python project.py
   ```
3. The program will greet you with "This is the ID creator for Businesses and Employees wizard", and will ask you what type of the
   the output will be, that you should type either `image` or `pdf` else the program will say that you typed an invalid format!

4. Type the rest of the credentials needed, then you are done you have created your ID on python, if the program has no errors it would show you that `finished creating your id please check your folder for the (filename) (type of file)`

# Documentation (for devs)

## Classes and its functions

```python
class Information:
    def __init__(self, filename, company, company_address, name_of_holder, nickname, department, position,
    emergency_name, emergency_number, emergency_address):
        ...
```

This class contains the Information the ID needed (this class would be also inherited). I do this because I want the code to be more "DRY-er"

```python
class PDF (Information):
    def create(self)
```

This class is inheriting the Information class, it creates a pdf out of it

```python
class IMAGE (Information):
    def create(self)
    def text_write(self, draw, w, h, text, font)
```

This class is just inheriting from the Information class and creating it. The center_write function centers the text, arguments:

- draw: An argument that takes the canvas
- w: the width of the picture/canvas
- h: the placement position on the y-axis (the placement in heights)
- text: The text that you want to be centered
- font: The font that you want to be rendered

```
It is important to take note that both classes (IMAGE and PDF) have their own created function.
```

## Functions (excluding Main)

```python
def validate_file_format(file_type)
```

As the name itself says, it validates the format if it is either Image or PDF, if either, it returns the format.

```python
def process_information(info)
```

It will process the information that you gave (it should be an array), and it would be running a function

```python
def create_id(info)
```

This function will create the ID, and if successful will return True, if not, will print the Error and return False
