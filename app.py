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
    pages_per_bilan = 6
    total_pages = len(reader.pages)
    
    # Calculer le nombre de bilans
    num_bilans = total_pages // pages_per_bilan
    
    for bilan_index in range(num_bilans):
        # Créer un nouveau writer pour chaque bilan
        writer = PdfWriter()
        
        # Ajouter les 6 pages du bilan actuel
        start_page = bilan_index * pages_per_bilan
        end_page = start_page + pages_per_bilan
        
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
        
        # Convertir en base64
        buffer = io.BytesIO()
        writer.write(buffer)
        encoded_pdf = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        results.append({
            "fileName": f"bilan_{bilan_index + 1}.pdf",
            "data": encoded_pdf
        })

    return JSONResponse(content=results)
