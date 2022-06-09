from project import *

def test_validate_file_format():
    assert validate_file_format("image") == "IMAGE"
    assert validate_file_format("iMAge") == "IMAGE"
    assert validate_file_format("img") == False
def test_process_information():
    assert process_information(["image", "test", "LORENZ SARMIENTO LLC", "Test address", "Gene Lorenz Sarmiento", "lorenz",
     "Information Technology", "Manager", "test contact", "(012)345-6789", "Grl", "gtg"]) == True
    assert process_information(["pdf", "test", "LORENZ SARMIENTO LLC", "Test address", "Gene Lorenz Sarmiento", "lorenz",
     "Information Technology", "Manager", "test contact", "(012)345-6789", "Grl", "gtg"]) == True
    assert process_information(["image", "test", "LORENZ SARMIENTO LLC", "Test address", "Gene Lorenz Sarmiento", "lorenz",
     "Information Technology", "Manager", "", ""]) == False
def test_create_id():
    assert create_id([], PDF) == False
    assert create_id([], IMAGE) == False