import azure.functions as func
import shared_functions.database as db
import shared_functions.auth as auth



def main(req: func.HttpRequest) -> func.HttpResponse:
    token = auth.create_token()
    verif = auth.verify_token(token, "admin")
    
    return func.HttpResponse(
            f"Success: {verif}",
            status_code=200
    )
