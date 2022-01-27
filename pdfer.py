from fpdf import FPDF  # pip install fpdf2 (pillow/PIL installed as depencancy)
from pathlib import Path

in_path = Path("/home/curt/Documents/these_pics/")
out_path = Path("/home/curt/Documents/")
kobo = (1072,1448)
reduction = 4
size = tuple(d/reduction for d in kobo)


pdf = FPDF()

for ch in range(60, 100):
    chapter = in_path / f"chapter {ch}/"
    print(chapter)
    for image in chapter.glob("*.png"):
        print(image)
        pdf.add_page(format=size)
        pdf.image(image, x = 10, y = 0,  w=pdf.epw)

pdf.output(out_path / f"Chapter60to99.pdf")
