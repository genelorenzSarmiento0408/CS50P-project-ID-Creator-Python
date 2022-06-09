from sys import exit
from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont, ImageOps
from rich.console import Console
from rich.prompt import Prompt
import textwrap

console = Console()

class Information():
    def __init__(self, filename, company, company_address, name_of_holder, nickname, department, position,
    emergency_name, emergency_number, approved_by, approved_by_position):
        self._filename = filename
        self._company = company
        self._company_address = company_address
        self._name_of_holder = name_of_holder
        self._nickname = nickname
        self._department = department
        self._position = position
        self._emergency_name = emergency_name
        self._emergency_number = emergency_number
        self._approved_by = approved_by
        self._approved_by_position = approved_by_position

    @property
    def filename(self):
        return self._filename
    @property
    def company(self):
        return self._company
    @property
    def name_of_holder(self):
        return self._name_of_holder
    @property
    def nickname(self):
        return self._nickname
    @property
    def department(self):
        return self._department
    @property
    def position(self):
        return self._position
    @property
    def emergency_name(self):
        return self._emergency_name
    @property
    def emergency_number(self):
        return self._emergency_number
    @property
    def company_address(self):
        return self._company_address
    @property
    def approved_by(self):
        return self._approved_by
    @property
    def approved_by_position(self):
        return self._approved_by_position
class PDF(Information):
    """ This class is inherting the Information class, it creates a pdf out of it """
    def create(self):
        pdf = FPDF()
        pdf.add_page()
        # Add fonts
        pdf.add_font("RobotoB", fname="./fonts/Roboto-Bold.ttf")
        pdf.add_font("RobotoR", fname="./fonts/Roboto-Regular.ttf")
        pdf.add_font("RobotoM", fname="./fonts/Roboto-Medium.ttf")
        # Main content
        # Set the company name
        pdf.set_font("RobotoB", size=13)
        pdf.rect(x=55, y=2, w=95, h=110)
        pdf.cell(0, 15, self.company, align="C")
        # Set the company address
        pdf.set_font("RobotoR", size=11)
        para = textwrap.wrap(self.company_address, width=30)
        padd = 25
        pdf.cell(0, padd, "", new_x="LMARGIN", align="C")
        for par in para:
            pdf.cell(0, padd, par, new_x="LMARGIN", align="C")
            padd += 10
        # Set the department
        pdf.set_font("RobotoB", size=15)
        pdf.cell(0, 50, self.department, new_x="LMARGIN", align="C")
        # Picture here text and box
        pdf.set_font("RobotoR", size=9)
        pdf.cell(0, 100, "Picture here", new_x="LMARGIN", align="C")
        pdf.rect(x=90, y=45, w=30, h=30)
        pdf.set_font("RobotoB", size=13)
        pdf.cell(0, 150, self.nickname, new_x="LMARGIN", align="C")
        pdf.set_font("RobotoR", size=11)
        pdf.cell(0, 160, self.name_of_holder, new_x="LMARGIN", align="C")
        pdf.set_font("RobotoB", size=11)
        pdf.cell(0, 175, self.position, new_x="LMARGIN", align="C")
        pdf.set_font("RobotoR", size=9)
        """ Back page """
        pdf.add_page()
        pdf.set_font("RobotoB", size=13)
        pdf.rect(x=55, y=2, w=95, h=110)
        pdf.cell(0, 15, "IN CASE OF EMERGENCY:", new_x="LMARGIN", align="C")
        pdf.set_font("RobotoR", size=11)
        pdf.cell(0, 25, f"Contact name: {self.emergency_name}", new_x="LMARGIN", align="C")
        pdf.cell(0, 35, f"Contact number: {self.emergency_number}", new_x="LMARGIN", align="C")
        pdf.cell(0, 60, "____________________________________", new_x="LMARGIN", align="C")
        pdf.cell(0, 70, self.name_of_holder.upper(), new_x="LMARGIN", align="C")
        pdf.set_font("RobotoR", size=9)
        para = textwrap.wrap(f"This card is a property of {self.company} \
        and shall be surrendered to the Management if the partnership is terminated", width=30)
        padd = 90
        pdf.cell(0, padd, "", new_x="LMARGIN", align="C")
        for par in para:
            pdf.cell(0, padd, par, new_x="LMARGIN", align="C")
            padd += 10
        pdf.set_font("RobotoB", size=12)
        pdf.cell(0, 150, "Approved by:", new_x="LMARGIN", align="C")
        pdf.set_font("RobotoR", size=12)
        pdf.cell(0, 165, "____________________________________", new_x="LMARGIN", align="C")
        pdf.set_font("RobotoB", size=12)
        pdf.cell(0, 175, self.approved_by.upper(), new_x="LMARGIN", align="C")
        pdf.set_font("RobotoR", size=12)
        pdf.cell(0, 185, self.approved_by_position.upper(), new_x="LMARGIN", align="C")
        pdf.output(f"{self.filename}.pdf")
class IMAGE(Information):
    """ """
    def create(self):
        """ This function creates the Image """
        """The front page"""
        w, h = (250, 320)
        # set the Image bg in initializing "https://www.geeksforgeeks.org/python-pil-image-new-method"
        im = Image.new("RGB", (w, h), color=(255, 255, 255))
        draw = ImageDraw.Draw(im)
        # Add text on image: https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil
        # Draw company name
        font = ImageFont.truetype("./fonts/Roboto-Bold.ttf", 13)
        self.text_center(draw, w, 30, self.company, font)
        # Draw the company address
        font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", 11)
        para = textwrap.wrap(self.company_address, width=30)
        cur_h, pad = 45, 1
        for par in para:
            size = draw.textsize((par), font=font)
            draw.text(((w - size[0]) / 2, cur_h), par, (0, 0, 0), font=font)
            cur_h += size[1] + pad
        # Draw the holder's department
        font = ImageFont.truetype("./fonts/Roboto-Bold.ttf", 15)
        self.text_center(draw, w, 70, self.department, font)
        # Draw the rectangle for the picture of the holder
        draw.rectangle([(w / 2 - 40, h / 2 - 50), (w / 2 + 40, h / 2 + 25)], outline="black")
        font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", 9)
        self.text_center(draw, w, 140, "Picture here", font)
        # Draw the holder's nickname
        font = ImageFont.truetype("./fonts/Roboto-Bold.ttf", 15)
        self.text_center(draw, w, 205, self.nickname, font)
        # Draw the holder's name
        font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", 11)
        self.text_center(draw, w, 220, self.name_of_holder, font)
        # Draw the holder's position
        font = ImageFont.truetype("./fonts/Roboto-Medium.ttf", 12)
        self.text_center(draw, w, 240, self.position, font)
        im.save(f"{self.filename}_front.png")
        """The back page"""
        im = Image.new("RGB", (w, h), color=(255, 255, 255))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("./fonts/Roboto-Bold.ttf", 12)
        self.text_center(draw, w, 30, "IN CASE OF EMERGENCY:", font)
        # Draw emergency contact info
        font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", 11)
        size = draw.textsize((f"Contact Person: {self.emergency_name}"), font=font)
        draw.text((35, 55), f"Contact Person: {self.emergency_name}", (0, 0, 0), font=font)
        draw.text((35, 70), f"Contact Number: {self.emergency_number}", (0, 0, 0), font=font)
        # Sign credentials for the holder
        self.text_center(draw, w, 105, "____________________________________", font)
        self.text_center(draw, w, 120, self.name_of_holder.upper(), font)
        # Information
        para = textwrap.wrap(f"This card is a property of {self.company} \
        and shall be surrendered to the Management if the partnership is terminated", width=30)
        cur_h, pad = 150, 1
        for par in para:
            size = draw.textsize((par), font=font)
            draw.text(((w - size[0]) / 2, cur_h), par, (0, 0, 0), font=font)
            cur_h += size[1] + pad
        # Sign credentials for the approver
        font = ImageFont.truetype("./fonts/Roboto-Bold.ttf", 12)
        self.text_center(draw, w, 225, "Approved by:", font)
        font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", 11)
        self.text_center(draw, w, 255, "____________________________________", font)
        font = ImageFont.truetype("./fonts/Roboto-Bold.ttf", 11)
        self.text_center(draw, w, 270, self.approved_by.upper(), font)
        font = ImageFont.truetype("./fonts/Roboto-Regular.ttf", 11)
        self.text_center(draw, w, 280, self.approved_by_position.upper(), font)
        im.save(f"{self.filename}_back.png")
    def text_center(self, draw, w, h, text, font):
        """
        The center_write function centers the text, arguments:
            - draw: An argument that takes the canvas
            - w: the width of the picture/canvas
            - h: the placement position in y axis (the placement in heights)
            - text: The text that you want to be centered
            - font: The font that you want to be rendered
        """
        # align text center: https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
        size = draw.textsize(text, font=font)
        draw.text(((w - size[0]) / 2, h), text, (0, 0, 0),font=font)

def main():
    print("Welcome👋 to the ID creator for Businesses and Employees wizard\nby Gene Lorenz Sarmiento")
    print("")
    file_type = Prompt.ask("✨ What is the file format of your ID?", choices=["image", "pdf"])
    file_type = validate_file_format(file_type)
    if not file_type:
        print("Invalid file type")
        exit(1)
    filename = Prompt.ask("✨ What is the name of your file?")
    company_name = Prompt.ask("✨ What is the ID's company name?")
    company_name = company_name.upper()
    company_address = Prompt.ask("✨ What is the ID's company address?")
    name_of_holder = Prompt.ask("✨ What is the full name of the holder?")
    nickname = Prompt.ask("✨ What is the nickname of the holder?")
    department = Prompt.ask("✨ What is the holder's department?")
    position = Prompt.ask("✨ What is the holder's position?")
    emergency_name = Prompt.ask("✨ In case of emergency who should we contact?")
    emergency_number = Prompt.ask(f"✨ What is the phone number of \"{emergency_name}\"?")
    approved_by = Prompt.ask("✨ This ID is approved by?")
    approved_by_position = Prompt.ask(f"✨ What is the position of {approved_by}")
    essential_info = [file_type, filename, company_name, company_address, name_of_holder, nickname, department, position,
    emergency_name, emergency_number, approved_by, approved_by_position]
    process_information(essential_info)

def validate_file_format(file_type):
    VALID_FILE_TYPES = [
        "IMAGE",
        "PDF"
    ]
    file_type = file_type.strip().upper()
    if file_type in VALID_FILE_TYPES:
        return file_type
    return False

def process_information(info):
    new_arr = []
    for i in range(0, 6):
        new_arr.append(info[i])
    for j in range(7, len(info) - 1):
        new_arr.append(info[j])
    if "" in new_arr:
        console.log("Some of the credentials are blank, please try again")
        return False
    info[2] = info[2].upper()
    info[5] = info[5].upper()
    for i in range(6, 8):
        info[i] = info[i].upper()
    if info[0].upper() == "PDF":
        info = info[1:]
        return create_id(info, PDF)
    info = info[1:]
    return create_id(info, IMAGE)


def create_id(info, classname):
    try:
        with console.status("Creating the id") as _:
            while classname(*info).create():
                console.log("Creating the ID now")
            console.log(f"finished creating your id please check your folder for the {info[0]} {classname.__name__.lower()}")
            return True
    except Exception as e:
        print(f"Creating the ID was not succesful because of {e}")
        return False

if __name__ == "__main__":
    main()