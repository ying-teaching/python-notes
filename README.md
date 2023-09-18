# Pragmatic Python Programming

> Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning. - Rick Cook

This is an introductory Python programming book for _knowledge workers_ who are professional data analysts or application developers. Unlike most existing Python programming books, it teaches Python programming in a pragmatic way. Here the word "pragmatic" means practical and professional. Knowledge workers learn Python programming to solve real world problems. The book teaches essential programming concepts and skills to effectively write professional programs that are correct, easy to maintain, easy to test and has reasonable performance. Specifically, in addition to the basic Python programming concepts in Part I, it covers the following topics that are important for a professional programmer:

- best programming practices such as naming, design, documentation, same level abstraction, small functions, separation of concerns, and continues refactoring.
- Python data model.
- advanced but important Python constructs such as property, decorator, descriptor, and metaclass.
- type hints.
- test driven development.
- application tracing.
- Python performance issues and tradeoffs.

## Jupyter Notebook Slides

You can show a slide in a browser by defining the following shell function `s()` and `sto()` in shell initialization script. For example, add it to `~/.zshrc` for `zsh`.

```sh
# convert and show one slide
s() {
  jupyter nbconvert $1 --to slides --post serve --SlidesExporter.reveal_scroll=True
}

# convert all to HTML slides
sto() {
  jupyter nbconvert *.ipynb --to slides --SlidesExporter.reveal_scroll=True
}
```

Then run `s file.ipynb` to do slide show in a browser. Run `sto` to convert all notebook files to HTML slides.

## Part I. Python Programming

### [Ch01: Introduction to Programming](slides/ch01_introduction/crash_course.ipynb)

### [Ch02: Variable and Expression](slides/ch02_variable/)

- [Variables](slides/ch02_variable/variables.ipynb).
- [Expression and Statements](slides/ch02_variable/expression_statement.ipynb)
- [Turtle Introduction](slides/ch02_variable/turtle_introduction.ipynb)

### [Ch03 Branch](slides/ch03_branch/branch.ipynb)

### [Ch04 Loop](slides/ch04_loop/loop.ipynb)

### [Ch05 Function](slides/ch05_function/funciton.ipynb)

### [Ch06 Collection](slides/ch06_collection/collection.ipynb)

### [Ch07 Class](slides/ch07_class/)

### [Ch08 Exception](slides/ch08_exception/)

### [Ch09 Module](slides/ch09_module/)

### [Ch10 File](slides/ch10_file/)

## Part II. Pragmatic Programming

### [Ch11 Test and CI/CD](slides/ch11_test/)

### [Ch12 Python Data Model](slides/ch12/)

### Ch13 Logging (TBC)

### Ch14 Type Hints (TBC)

### Ch15 Performance (TBC)

## Part III. Algorithmic Thinking

### Ch16 Web Application

### Ch17 A Lisp Interpreter

### Ch18 Data Science (TBC)

## [Appendix](appendix/)

- [Command Line Interface](appendix/command-line.md): introduction of command line tool. Please read and learn this first if you don't know CLI. It is must-to-know for a programmer.
- [Install Python Interpreter](appendix/install-python.md): how to install Python.
- [Install and setup VS Code for Python Development](appendix/vscode-python.md): how to install and setup Visual Studo Code (VS Code) for Python development.
- [Git and GitHub](appendix/git-and-github.md): use GitHub to manage your software source code.
- [Misc](appendix/Misc/): additional programming resources, not directly related to Python.
