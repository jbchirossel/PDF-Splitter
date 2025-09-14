# app.py
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader, PdfWriter
import io
import base64

app = FastAPI()

SECRET_TOKEN = "lacsurcsecur1423@@"

@app.post("/split")
async def split_pdf(request: Request, file: UploadFile = File(...)):
    token = request.query_params.get("token")
    if token != SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Unauthorized")

    content = await file.read()
    reader = PdfReader(io.BytesIO(content))

    results = []
    pages_per_bilan = 6
    total_pages = len(reader.pages)

    num_bilans = total_pages // pages_per_bilan

    for bilan_index in range(num_bilans):
        writer = PdfWriter()
        start_page = bilan_index * pages_per_bilan
        end_page = start_page + pages_per_bilan

        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])

        buffer = io.BytesIO()
        writer.write(buffer)
        encoded_pdf = base64.b64encode(buffer.getvalue()).decode('utf-8')

        results.append({
            "fileName": f"bilan_{bilan_index + 1}.pdf",
            "data": encoded_pdf
        })

    return JSONResponse(content=results)
