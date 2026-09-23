from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader, UnstructuredFileLoader
from models .enums.ProcessingEnum import ProcessingEnum
from langchain_text_splitters import RecursiveCharacterTextSplitter

class ProcessController(BaseController):
    def __init__(self, project_id: str):
        super().__init__()
        
        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=project_id)
        
    def get_file_extension(self, file_id: str):
        return os.path.splitext(file_id)[-1]  # Returns the file extension, including the dot (e.g., '.txt', '.csv')
    
    def get_file_loader(self, file_id: str, file_path: str): 
        file_path = os.path.join(self.project_path, file_id)
        if not os.path.isfile(file_path):
            matching_files = [
                name for name in os.listdir(self.project_path)
                if name.startswith(f"{file_id}_")
            ]
            if len(matching_files) == 1:
                file_id = matching_files[0]
                file_path = os.path.join(self.project_path, file_id)
            else:
                raise FileNotFoundError(f"File not found: {file_id}")

        file_ext = self.get_file_extension(file_id=file_id)
        
        if file_ext == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        
        elif file_ext == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding='utf-8')
        else:
            raise ValueError(f"Unsupported file type: {file_ext}")
        
    def get_file_content(self, file_id: str):
        file_path = os.path.join(self.project_path, file_id)
        loader = self.get_file_loader(file_id=file_id, file_path=file_path)
        documents = loader.load()
        return documents
    
    def process_file_content(self, file_id: str, chunk_size: int = 100, overlap_size: int = 20):
        documents = self.get_file_content(file_id=file_id)
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len
        )
        
        chunks = text_splitter.split_documents(documents)
        
        return chunks