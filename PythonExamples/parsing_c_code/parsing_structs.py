from pycparser import c_parser, c_ast, plyparser
import glob

class StructVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.in_struct = False

    def visit_Struct(self, node):
        if not self.in_struct:
            print(f"Found struct: {node.name}")
            print("Struct Body:")
            print(node.show())

    def visit_Comment(self, node):
        if self.in_struct:
            print("Comment within struct:")
            print(node.show())

def find_and_copy_structs(directory):
    header_files = glob.glob(directory + '/*.h')

    for file_path in header_files:
        with open(file_path, 'r') as file:
            content = file.read()

            # Use pycparser to parse the C code
            parser = c_parser.CParser()
            try:
                ast = parser.parse(content, filename=file_path)
            except plyparser.ParseError as e:
                print(f"Error parsing {file_path}: {e}")
                continue

            # Manually traverse the AST to find struct definitions
            visitor = StructVisitor()
            for node in ast.ext:
                visitor.visit(node)

if __name__ == "__main__":
    # Replace 'your_directory_here' with the actual directory containing your header files
    directory_to_search = 'D:\\DEV\\GE\\scan-api-exposure\\helios_dev-pet_omni_integ-39\\include'
    find_and_copy_structs(directory_to_search)
