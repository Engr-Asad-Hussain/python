## Registry Pattern
The Registry Pattern in Python is a design pattern that provides a centralized mechanism for managing and accessing objects or classes within an application. It acts as a central repository where items (classes, functions, or instances) are registered with a unique key, allowing for their dynamic retrieval and use throughout the codebase.

## Example1: Walk through
- If you have multiple `if/else` conditions which are handling different conditions as illustrated in example `example1/01.py` - you can improve code using registry pattern.

- We have created centralized machanism for tracking different exporting options (called as registry of exporter functions) in example `example1/02.py`. Now you don't actually need to write multiple `if/else` conditions in the `export_data` function. That way, when you create other exporters like `export_xml` you only have to populate your registry dictionary only. This is not perfect yet because you have to manually added the exporter function in the registry. If you have many exporter options then this would be become huge dictionary - which can be simplified.

- One thing you can do is, let your exporter functions register themselves as illustrated in example `03.py` via decorators.

- Execute the example scripts:
```sh
cd patters/registry/example1

python 01.py
python 02.py
python 03.py
```

## Example2: Walk through
- It is an illustration of configuring commandline functions and text dynamically using registry pattern. The good thing about this pattern is you can dynamically create new cli commands without chaning any existing file.

- In the example `example2/registry.py` - we have created registry with List of Tuple as data type.

- The `example2/commands` and `example2/plugins` are the directly where actual cli is created as a separate module. Each function is registered dynamically using the decorator created in `registry.py`.

- The main file load `commands` and `plugins`. Then configure the cli using `typer` python package.

- Execute the example scripts:
```sh
cd patters/registry/example2

python main.py text count "Asad Hussain"
python main.py text reverse "Asad Hussain"
python main.py text shout "plugin power"
python main.py text whisper "PLSlugin power"
```