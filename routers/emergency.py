from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from models import EmergencyContact

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# menampilkan halaman
@router.get("/emergency/{user_id}", response_class=HTMLResponse)
def emergency_page(user_id: int, request: Request, db: Session = Depends(get_db)):
    contacts = (
        db.query(EmergencyContact)
        .filter(EmergencyContact.user_id == user_id)
        .all()
    )

    return templates.TemplateResponse(
        request,
        "emergency.html",
        {
            "contacts": contacts,
            "user_id": user_id,
        },
    )

# menambahkan kontak darurat
@router.post("/emergency/{user_id}/add")
def add_contact(
    user_id: int,
    name: str = Form(...),
    relationship_name: str = Form(...),
    phone: str = Form(...),
    db: Session = Depends(get_db),
):
    contact = EmergencyContact(
        user_id=user_id,
        name=name,
        relationship_name=relationship_name,
        phone=phone,
    )

    db.add(contact)
    db.commit()

    return RedirectResponse(url=f"/emergency/{user_id}", status_code=303)

# menghapus kontak darurat
@router.post("/emergency/delete/{id}")
def delete_contact(id: int, db: Session = Depends(get_db)):
    contact = db.query(EmergencyContact).filter(EmergencyContact.id == id).first()

    if not contact:
        raise HTTPException(status_code=404, detail="Kontak darurat tidak ditemukan")

    user_id = contact.user_id

    db.delete(contact)
    db.commit()

    return RedirectResponse(url=f"/emergency/{user_id}", status_code=303)