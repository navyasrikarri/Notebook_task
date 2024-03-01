class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

class DoubleNode:
    def _init_(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = DoubleNode(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            new_node = DoubleNode(data)
            current.next = new_node
            new_node.prev = current


class Notepad:
    def _init_(self):
        self.documents = DoubleLinkedList()

    def create_document(self, name):
        document = LinkedList()
        self.documents.append({name: document})

    def open_document(self, name):
        current = self.documents.head
        while current:
            if name in current.data:
                return current.data[name]
            current = current.next
        print("Document not found.")
        return None

    def save_document(self, name, document):
        current = self.documents.head
        while current:
            if name in current.data:
                current.data[name] = document
                print("Document saved.")
                return
            current = current.next
        print("Document not found.")

    def edit_document(self, name, operation, data):
        document = self.open_document(name)
        if document:
            if operation == "insert":
                document.append(data)
            
            print("Document edited.")
        else:
            print("Cannot edit document. Document not found.")

    def navigate_document(self, name, direction):
        document = self.open_document(name)
        if document:
            
            print("Cursor moved.")
        else:
            print("Cannot navigate document. Document not found.")

    def search_document(self, name, keyword):
        document = self.open_document(name)
        if document:
           
            print("Search results:")
            
        else:
            print("Cannot search document. Document not found.")

    def copy_paste(self, source_name, destination_name):
        source_document = self.open_document(source_name)
        destination_document = self.open_document(destination_name)
        if source_document and destination_document:
           
            print("Text copied and pasted.")
        else:
            print("Cannot copy and paste. Document not found.")


def main():
    notepad = Notepad()
    while True:
        print("1. Create document")
        print("2. Open document")
        print("3. Edit document")
        print("4. Navigate document")
        print("5. Search document")
        print("6. Copy and paste")
        print("7. Save document")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter document name: ")
            notepad.create_document(name)
        elif choice == "2":
            name = input("Enter document name: ")
            document = notepad.open_document(name)
            if document:
                print("Document opened.")
        elif choice == "3":
            name = input("Enter document name: ")
            operation = input("Enter operation (insert, delete, update): ")
            data = input("Enter data: ")
            notepad.edit_document(name, operation, data)
        elif choice == "4":
            name = input("Enter document name: ")
            direction = input("Enter direction (up, down): ")
            notepad.navigate_document(name, direction)
        elif choice == "5":
            name = input("Enter document name: ")
            keyword = input("Enter keyword to search: ")
            notepad.search_document(name, keyword)
        elif choice == "6":
            source_name = input("Enter source document name: ")
            destination_name = input("Enter destination document name: ")
            notepad.copy_paste(source_name, destination_name)
        elif choice == "7":
            name = input("Enter document name: ")
            document = input("Enter document content: ")
            notepad.save_document(name, document)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if _name_ == "_main_":
    main()
  