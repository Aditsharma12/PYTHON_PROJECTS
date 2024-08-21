def jpg_to_pdf_from_local_file():
    from PIL import Image
    # Prompt the user for the image file path
    image_path = input("Enter the image file path: ")
    
    try:
        # Open the image file
        image = Image.open(image_path)
        # Ensure the image is in RGB mode
        image = image.convert('RGB')
        # Save the image as a PDF
        output_path = "output.pdf"
        image.save(output_path, 'PDF', resolution=100.0)
        print(f"PDF saved successfully as {output_path}")
    except Exception as e:
        print(f"Failed to convert image to PDF: {e}")
def qr():
    import qrcode
    print("enter the text to convert")
    str2=input("Enter data to be stored here")
    img = qrcode.make(str2)
    type(img)  # qrcode.image.pil.PilImage
    img.save("some_file.png")
def notes():
    f1=1
    while(f1==1):
     try:
      str=input("Enter data to be stored")
      with open("file.txt","a") as f:
        f.write(str)
        f.write("\n")
        f1=int(input("enter 1 to write and any no. to terminate"))
     except ValueError:
       print("enter values bro no other thing")
def main():
  n=int(input("enter the number what you want to perform \n 1.to convert to qr \n 2.to take notes \n 3.to convert to pdf\nEnter here"))
  if(n==1):
     qr()
  if(n==2):
     notes()
  if(n==3):
     jpg_to_pdf_from_local_file()

if __name__=="__main__":
  main()