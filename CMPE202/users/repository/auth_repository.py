from fastapi import status, HTTPException
from .. import schemas, models, token
from sqlalchemy.orm import Session
from ..hashing import Hash


def logIn(request: schemas.Login, db: Session):

    user = db.query(models.User).filter(models.User.username == request.username).first()


    if not user or not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username/Password incorrect")


    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.username},
        # expires_delta=access_token_expires
    )


    return {"access_token": access_token, "token_type": "bearer"}