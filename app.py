# app.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader, PdfWriter
import io
import base64


app = FastAPI()


@app.post("/split")
async def split_pdf(file: UploadFile = File(...)):
    content = await file.read()
    reader = PdfReader(io.BytesIO(content))


    results = []
    current_writer = PdfWriter()
    part_index = 1


    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""


        if "édité le" in text.lower() and len(current_writer.pages) > 0:
            buffer = io.BytesIO()
            current_writer.write(buffer)
            encoded_pdf = base64.b64encode(buffer.getvalue()).decode('utf-8')
            results.append({
                "fileName": f"bilan_{part_index}.pdf",
                "data": encoded_pdf
            })
            part_index += 1
            current_writer = PdfWriter()


        current_writer.add_page(page)


    if len(current_writer.pages) > 0:
        buffer = io.BytesIO()
        current_writer.write(buffer)
        encoded_pdf = base64.b64encode(buffer.getvalue()).decode('utf-8')
        results.append({
            "fileName": f"bilan_{part_index}.pdf",
            "data": encoded_pdf
        })


    return JSONResponse(content=results)
